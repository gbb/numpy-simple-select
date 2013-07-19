
<PRE>
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
0.00236010551453

np.select output: 
[ 0  1  2  0  0  0 36 49 64 81]

numpy.select time is: 
0.00252604484558

Matching: ss and np matched.


Test name: test1a
innerloops =  10000
size =  10000
condlist =  [array([False, False, False, ...,  True,  True,  T
choicelist =  [1, 2]
setupline =  import sys; import numpy as np; import simple_sel as ss; import test_ss; test_ss.test1a()
ss.select output: 
[2 2 0 ..., 1 1 1]

ss.select time is: 
0.570926904678

np.select output: 
[2 2 0 ..., 1 1 1]

numpy.select time is: 
1.99994802475

Matching: ss and np matched.


Test name: test1b
innerloops =  10
size =  10000000
condlist =  [array([False, False, False, ...,  True,  True,  T
choicelist =  [1, 2]
setupline =  import sys; import numpy as np; import simple_sel as ss; import test_ss; test_ss.test1b()
ss.select output: 
[2 2 0 ..., 1 1 1]

ss.select time is: 
0.453832149506

np.select output: 
[2 2 0 ..., 1 1 1]

numpy.select time is: 
2.01832699776

Matching: ss and np matched.


Test name: test1c
innerloops =  10000
size =  10000
condlist =  [array([False, False, False, ...,  True,  True,  T
choicelist =  [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1
setupline =  import sys; import numpy as np; import simple_sel as ss; import test_ss; test_ss.test1c()
ss.select output: 
[2 2 0 ..., 1 1 1]

ss.select time is: 
3.02462792397

np.select output: 
[2 2 0 ..., 1 1 1]

numpy.select time is: 
16.2374591827

Matching: ss and np matched.


Test name: test1d
innerloops =  10
size =  10000000
condlist =  [array([False, False, False, ...,  True,  True,  T
choicelist =  [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1
setupline =  import sys; import numpy as np; import simple_sel as ss; import test_ss; test_ss.test1d()
ss.select output: 
[2 2 0 ..., 1 1 1]

ss.select time is: 
3.03344893456

np.select output: 
[2 2 0 ..., 1 1 1]

numpy.select time is: 
17.5852000713

Matching: ss and np matched.


Test name: test2a
innerloops =  10000
size =  10000
condlist =  [array([False, False, False, ...,  True,  True,  T
choicelist =  [array([   0,    1,    2, ..., 9997, 9998, 9999]),
setupline =  import sys; import numpy as np; import simple_sel as ss; import test_ss; test_ss.test2a()
ss.select output: 
[   0    1    0 ..., 9997 9998 9999]

ss.select time is: 
0.898550033569

np.select output: 
[   0    1    0 ..., 9997 9998 9999]

numpy.select time is: 
1.99836301804

Matching: ss and np matched.


Test name: test2b
innerloops =  10
size =  10000000
condlist =  [array([False, False, False, ...,  True,  True,  T
choicelist =  [array([      0,       1,       2, ..., 9999997, 9
setupline =  import sys; import numpy as np; import simple_sel as ss; import test_ss; test_ss.test2b()
ss.select output: 
[      0       1       0 ..., 9999997 9999998 9999999]

ss.select time is: 
0.823184013367

np.select output: 
[      0       1       0 ..., 9999997 9999998 9999999]

numpy.select time is: 
2.03614592552

Matching: ss and np matched.


Test name: test2c
innerloops =  10000
size =  10000
condlist =  [array([False, False, False, ...,  True,  True,  T
choicelist =  [array([   0,    1,    2, ..., 9997, 9998, 9999]),
setupline =  import sys; import numpy as np; import simple_sel as ss; import test_ss; test_ss.test2c()
ss.select output: 
[   0    1    0 ..., 9997 9998 9999]

ss.select time is: 
5.99375319481

np.select output: 
[   0    1    0 ..., 9997 9998 9999]

numpy.select time is: 
16.2316129208

Matching: ss and np matched.


Test name: test2d
innerloops =  10
size =  10000000
condlist =  [array([False, False, False, ...,  True,  True,  T
choicelist =  [array([      0,       1,       2, ..., 9999997, 9
setupline =  import sys; import numpy as np; import simple_sel as ss; import test_ss; test_ss.test2d()
ss.select output: 
[      0       1       0 ..., 9999997 9999998 9999999]

ss.select time is: 
6.67919492722

np.select output: 
[      0       1       0 ..., 9999997 9999998 9999999]

numpy.select time is: 
17.8270070553

Matching: ss and np matched.


Test name: bug1
innerloops =  10
size =  10
condlist =  [array([False, False, False, False,  True,  True, 
choicelist =  [array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), array([0, 
setupline =  import sys; import numpy as np; import simple_sel as ss; import test_ss; test_ss.bug1()
ss.select output: 
[0 0 0 0 4 5 6 7 8 9]

ss.select time is: 
0.00119686126709

np.select output: 
Need between 2 and (32) array objects (inclusive).

Matching: WARNING! ss and np didn't match. This is normal for bug cases.


Test name: bug2
innerloops =  10
size =  10
condlist =  [array([False, False, False, False,  True,  True, 
choicelist =  [array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), array([0, 
setupline =  import sys; import numpy as np; import simple_sel as ss; import test_ss; test_ss.bug2()
ss.select output: 
[0 0 0 0 4 5 6 7 8 9]

ss.select time is: 
0.00125789642334

np.select output: 
Need between 2 and (32) array objects (inclusive).

Matching: WARNING! ss and np didn't match. This is normal for bug cases.


Test name: bug3
innerloops =  10
size =  10
condlist =  []
choicelist =  []
setupline =  import sys; import numpy as np; import simple_sel as ss; import test_ss; test_ss.bug3()
ss.select output: 
[]

ss.select time is: 
4.81605529785e-05

np.select output: 
0

numpy.select time is: 
0.000167846679688

Matching: WARNING! ss and np didn't match. This is normal for bug cases.


Test name: bug4
innerloops =  1
size =  4
condlist =  [array([ True,  True,  True, False], dtype=bool), 
choicelist =  [array([0, 1, 2, 3]), array([0, 1, 4, 9]), array([
setupline =  import sys; import numpy as np; import simple_sel as ss; import test_ss; test_ss.bug4()
ss.select output: 
[0 1 2 0]

ss.select time is: 
25.5437982082

np.select output: 
Need between 2 and (32) array objects (inclusive).

Matching: WARNING! ss and np didn't match. This is normal for bug cases.

Number of non-matching tests:  4
Check this matches the number of bug cases. (4)
Thanks for checking the test output :)
</PRE>
