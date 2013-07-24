
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
0.00241494178772

np.select output: 
[ 0  1  2  0  0  0 36 49 64 81]

numpy.select time is: 
0.00252509117126

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
0.570708990097

np.select output: 
[2 2 0 ..., 1 1 1]

numpy.select time is: 
1.97568917274

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
0.449014902115

np.select output: 
[2 2 0 ..., 1 1 1]

numpy.select time is: 
2.04051089287

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
3.14280986786

np.select output: 
[2 2 0 ..., 1 1 1]

numpy.select time is: 
16.6164679527

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
3.03392696381

np.select output: 
[2 2 0 ..., 1 1 1]

numpy.select time is: 
17.4547951221

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
0.91486287117

np.select output: 
[   0    1    0 ..., 9997 9998 9999]

numpy.select time is: 
2.02632594109

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
0.818386077881

np.select output: 
[      0       1       0 ..., 9999997 9999998 9999999]

numpy.select time is: 
2.00318002701

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
5.94291210175

np.select output: 
[   0    1    0 ..., 9997 9998 9999]

numpy.select time is: 
16.6462669373

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
6.69624686241

np.select output: 
[      0       1       0 ..., 9999997 9999998 9999999]

numpy.select time is: 
17.5204050541

Matching: ss and np matched.


Test name: scalar_cond
innerloops =  100
size =  10
condlist =  [array([ True,  True,  True, False, False, False, 
choicelist =  [array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), array([ 0,
setupline =  import sys; import numpy as np; import simple_sel as ss; import test_ss; test_ss.scalar_cond()
ss.select output: 
[ 0  1  2  9 16 25 36 49 64 81]

ss.select time is: 
0.00542902946472

np.select output: 
[ 0  1  2  9 16 25 36 49 64 81]

numpy.select time is: 
0.00258088111877

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
0.00117707252502

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
0.00124216079712

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
0.000169038772583

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
24.9998121262

np.select output: 
