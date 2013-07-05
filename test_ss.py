import numpy as np
import simple_sel as ss
import timeit
import sys

# simplesel.select test harness v1.0

print
print "Benchmarks/test output for simplesel.select"
print
print "Numpy version:"+str(np.version.version)
print "Python version:"+str(sys.version)
print
print "Please see test_ss.py for explanations of tests"
print


# Not the most elegant test-harness implementation, but it will do.
global innerloops, size, condlist, choicelist
innerloops=0; size=0; condlist=[]; choicelist=[]

# Number of times to run tests, when taking the fastest result.
outerloops=5

def benchmark(setup_num):

    setup_num()
    setupline="import sys; import numpy as np; import simple_sel as ss; import test_ss; test_ss."+setup_num.__name__+"()"

    print
    print "Test name: "+setup_num.__name__
    print "innerloops = ", innerloops
    print "size = ", size
    print "condlist = ", str(condlist)[0:50]
    print "choicelist = ", str(choicelist)[0:50]
    print "setupline = ", setupline

    t = timeit.Timer("ss.select(test_ss.condlist, test_ss.choicelist)", setup=setupline)
    try: 
        print "ss.select output: "
        print ss.select(condlist, choicelist)
        print
        print "ss.select time is: "
        print min(t.repeat(outerloops,innerloops))
    except Exception, e: 
        sys.exc_info()[0]        
        t.print_exc();
        print e
    print

    t = timeit.Timer("np.select(test_ss.condlist, test_ss.choicelist)", setup=setupline)
    try: 
        print "np.select output: "
        print np.select(condlist, choicelist)
        print
        print "numpy.select time is: "
        print min(t.repeat(outerloops,innerloops))
    except Exception, e: 
        sys.exc_info()[0]        
        t.print_exc();
        print e
    print


## Tests below

# Original test case for np.select from documentation/code.
# correct output: 
# array([ 0,    1,    2,    0,    0,    0, 36, 49, 64, 81])
def example1():  
    global innerloops, size, condlist, choicelist
    innerloops = 100
    size = 10
    x = np.arange(size)
    condlist = [x<3, x>5]
    choicelist = [x,x**2]


## Speed comparison tests. 

# Scalar choicelist test. 
def test1a():
    global innerloops, size, condlist, choicelist
    innerloops = 10000
    size = 10000
    x = np.arange(size)
    y = np.arange(size)
    condlist = [x>4, y<2] 
    choicelist = [1, 2]  

# Scalar choicelist test, larger size. 
def test1b():
    global innerloops, size, condlist, choicelist
    innerloops = 10
    size = 10000000
    x = np.arange(size)
    y = np.arange(size)
    condlist = [x>4, y<2]  
    choicelist = [1, 2] 

# Scalar choicelist test, larger list 
def test1c():
    global innerloops, size, condlist, choicelist
    innerloops = 10000
    size = 10000
    x = np.arange(size)
    y = np.arange(size)
    condlist = [x>4, y<2] * 10   
    choicelist = [1, 2] * 10

# Scalar choicelist test, larger list & size. 
def test1d():
    global innerloops, size, condlist, choicelist
    innerloops = 10
    size = 10000000
    x = np.arange(size)
    y = np.arange(size)
    condlist = [x>4, y<2] * 10   
    choicelist = [1, 2] * 10


# ndarray choicelist test. 
def test2a():
    global innerloops, size, condlist, choicelist
    innerloops = 10000
    size = 10000
    x = np.arange(size)
    y = np.arange(size)
    condlist = [x>4, y<2] 
    choicelist = [x, y]  

# ndarray choicelist test, larger size. 
def test2b():
    global innerloops, size, condlist, choicelist
    innerloops = 10
    size = 10000000
    x = np.arange(size)
    y = np.arange(size)
    condlist = [x>4, y<2]  
    choicelist = [x, y] 

# ndarray choicelist test, larger list 
def test2c():
    global innerloops, size, condlist, choicelist
    innerloops = 10000
    size = 10000
    x = np.arange(size)
    y = np.arange(size)
    condlist = [x>4, y<2] * 10   
    choicelist = [x, y] * 10

# ndarray choicelist test, larger list & size. 
def test2d():
    global innerloops, size, condlist, choicelist
    innerloops = 10
    size = 10000000
    x = np.arange(size)
    y = np.arange(size)
    condlist = [x>4, y<2] * 10   
    choicelist = [x, y] * 10


## BUG EXAMPLES

# numpy.select fails on 31 or 32 items while claiming to support them.
def bug1():
    global innerloops, size, condlist, choicelist
    innerloops = 10
    size = 10
    x = np.arange(size)
    y = np.arange(size)
    condlist = [x>3] * 31
    choicelist = [x] * 31

# numpy.select fails on >32 items.
def bug2():
    global innerloops, size, condlist, choicelist
    innerloops = 10
    size = 10
    x = np.arange(size)
    y = np.arange(size)
    condlist = [x>3] * 33
    choicelist = [x] * 33

# numpy.select creates a scalar value instead of an empty ndarray
# when given empty ndarray inputs
def bug3():
    global innerloops, size, condlist, choicelist
    innerloops = 10
    size = 10
    x = np.arange(size)
    y = np.arange(size)
    condlist = []    
    choicelist = [] 

# Test case for extremely large ndarray lists
# inspired by http://mail.scipy.org/pipermail/numpy-discussion/2011-July/057831$
def bug4():
    global innerloops, size, condlist, choicelist
    innerloops = 1
    size = 4
    x = np.arange(size)
    condlist = [x<3, x>5] * 2**22
    choicelist = [x,x**2] * 2**22

# This test disabled by default. Takes around 80-300 seconds to complete one call in ss.select.
# will not run at all in np.select (July 2013). 



if __name__ == "__main__": 

    benchmark(example1)

    benchmark(test1a)
    benchmark(test1b)
    benchmark(test1c)
    benchmark(test1d)

    benchmark(test2a)
    benchmark(test2b)
    benchmark(test2c)
    benchmark(test2d)

    benchmark(bug1)
    benchmark(bug2)
    benchmark(bug3)
    benchmark(bug4)
