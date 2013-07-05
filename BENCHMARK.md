
Benchmarks/test output for simplesel.select

Numpy version:1.7.1
Python version:2.7.3 (default, Aug  9 2012, 17:23:57) 
[GCC 4.7.1 20120720 (Red Hat 4.7.1-5)]

Please see test_ss.py for explanations of tests


Test name: example1
innerloops =  100
size =  10
condlist =  [array([ True,  True,  True, False, False, False, 
choicelist =  [array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), array([ 0,
setupline =  import sys; import numpy as np; import simple_sel as ss; import test_ss; test_ss.example1()
ss.select output: 
[ 0  1  2  0  0  0 36 49 64 81]

ss.select time is: 
0.00465703010559

np.select output: 
[ 0  1  2  0  0  0 36 49 64 81]

numpy.select time is: 
0.00251603126526


Test name: test1a
innerloops =  10000
size =  10000
condlist =  [array([False, False, False, ...,  True,  True,  T
choicelist =  [1, 2]
setupline =  import sys; import numpy as np; import simple_sel as ss; import test_ss; test_ss.test1a()
ss.select output: 
[2 2 0 ..., 1 1 1]

ss.select time is: 
1.35395908356

np.select output: 
[2 2 0 ..., 1 1 1]

numpy.select time is: 
2.00951981544


Test name: test1b
innerloops =  10
size =  10000000
condlist =  [array([False, False, False, ...,  True,  True,  T
choicelist =  [1, 2]
setupline =  import sys; import numpy as np; import simple_sel as ss; import test_ss; test_ss.test1b()
ss.select output: 
[2 2 0 ..., 1 1 1]

ss.select time is: 
1.92386889458

np.select output: 
[2 2 0 ..., 1 1 1]

numpy.select time is: 
3.54009604454


Test name: test1c
innerloops =  10000
size =  10000
condlist =  [array([False, False, False, ...,  True,  True,  T
choicelist =  [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1
setupline =  import sys; import numpy as np; import simple_sel as ss; import test_ss; test_ss.test1c()
ss.select output: 
[2 2 0 ..., 1 1 1]

ss.select time is: 
6.72405004501

np.select output: 
[2 2 0 ..., 1 1 1]

numpy.select time is: 
17.2564620972


Test name: test1d
innerloops =  10
size =  10000000
condlist =  [array([False, False, False, ...,  True,  True,  T
choicelist =  [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1
setupline =  import sys; import numpy as np; import simple_sel as ss; import test_ss; test_ss.test1d()
ss.select output: 
[2 2 0 ..., 1 1 1]

ss.select time is: 
13.6574349403

np.select output: 
[2 2 0 ..., 1 1 1]

numpy.select time is: 
28.7878341675


Test name: test2a
innerloops =  10000
size =  10000
condlist =  [array([False, False, False, ...,  True,  True,  T
choicelist =  [array([   0,    1,    2, ..., 9997, 9998, 9999]),
setupline =  import sys; import numpy as np; import simple_sel as ss; import test_ss; test_ss.test2a()
ss.select output: 
[   0    1    0 ..., 9997 9998 9999]

ss.select time is: 
1.96070718765

np.select output: 
[   0    1    0 ..., 9997 9998 9999]

numpy.select time is: 
2.02650904655


Test name: test2b
innerloops =  10
size =  10000000
condlist =  [array([False, False, False, ...,  True,  True,  T
choicelist =  [array([      0,       1,       2, ..., 9999997, 9
setupline =  import sys; import numpy as np; import simple_sel as ss; import test_ss; test_ss.test2b()
ss.select output: 
[      0       1       0 ..., 9999997 9999998 9999999]

ss.select time is: 
2.79668188095

np.select output: 
[      0       1       0 ..., 9999997 9999998 9999999]

numpy.select time is: 
2.22040700912


Test name: test2c
innerloops =  10000
size =  10000
condlist =  [array([False, False, False, ...,  True,  True,  T
choicelist =  [array([   0,    1,    2, ..., 9997, 9998, 9999]),
setupline =  import sys; import numpy as np; import simple_sel as ss; import test_ss; test_ss.test2c()
ss.select output: 
[   0    1    0 ..., 9997 9998 9999]

ss.select time is: 
14.0220549107

np.select output: 
[   0    1    0 ..., 9997 9998 9999]

numpy.select time is: 
17.2801048756


Test name: test2d
innerloops =  10
size =  10000000
condlist =  [array([False, False, False, ...,  True,  True,  T
choicelist =  [array([      0,       1,       2, ..., 9999997, 9
setupline =  import sys; import numpy as np; import simple_sel as ss; import test_ss; test_ss.test2d()
ss.select output: 
[      0       1       0 ..., 9999997 9999998 9999999]

ss.select time is: 
34.7718720436

np.select output: 
[      0       1       0 ..., 9999997 9999998 9999999]

numpy.select time is: 
20.561207056


Test name: bug1
innerloops =  10
size =  10
condlist =  [array([False, False, False, False,  True,  True, 
choicelist =  [array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), array([0, 
setupline =  import sys; import numpy as np; import simple_sel as ss; import test_ss; test_ss.bug1()
ss.select output: 
[0 0 0 0 4 5 6 7 8 9]

ss.select time is: 
0.00232815742493

np.select output: 
Need between 2 and (32) array objects (inclusive).


Test name: bug2
innerloops =  10
size =  10
condlist =  [array([False, False, False, False,  True,  True, 
choicelist =  [array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), array([0, 
setupline =  import sys; import numpy as np; import simple_sel as ss; import test_ss; test_ss.bug2()
ss.select output: 
[0 0 0 0 4 5 6 7 8 9]

ss.select time is: 
0.00243902206421

np.select output: 
Need between 2 and (32) array objects (inclusive).


Test name: bug3
innerloops =  10
size =  10
condlist =  []
choicelist =  []
setupline =  import sys; import numpy as np; import simple_sel as ss; import test_ss; test_ss.bug3()
ss.select output: 
[]

ss.select time is: 
4.79221343994e-05

np.select output: 
0

numpy.select time is: 
0.000169992446899


Test name: bug4
innerloops =  1
size =  4
condlist =  [array([ True,  True,  True, False], dtype=bool), 
choicelist =  [array([0, 1, 2, 3]), array([0, 1, 4, 9]), array([
setupline =  import sys; import numpy as np; import simple_sel as ss; import test_ss; test_ss.bug4()
ss.select output: 
[0 1 2 0]

ss.select time is: 
52.2690601349

np.select output: 
Need between 2 and (32) array objects (inclusive).

