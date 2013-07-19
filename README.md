numpy-simple-select
===================

This is a drop-in replacement for the 'select' function in numpy. It has 
been reimplemented to fix long-standing bugs, improve speed 
substantially in all use cases, and improve internal documentation. It 
now supports broadcasting. It also performs some extra validation of 
input.

It is a follow-up to my posts in the numpy repository:

https://github.com/numpy/numpy/issues/3259

https://github.com/numpy/numpy/issues/3254

I have also included a test harness which demonstrates the faults in the 
original numpy.select and allows a performance comparison.

Version 2.0
----

V2.0 Pros:

- Refactored and simplified the code, added full broadcasting. 
- Execution with scalar choicelists is around 5x faster than np.select
- Non-scalar & broadcast execution is around 2-3x faster than np.select
- No new bugs detected, and known bugs in numpy.select fixed and tested.
- Fully backwards compatible with v1.0 simplesel and numpy 1.7.1 select.
- Test harness improved to detect regressions.
- Processes select() with 2^23 ndarrays in around 25 seconds, 2012 hardware.

Hopefully this will get added to standard numpy  :-) 

V2.0 Cons:

None observed so far.

Version 1.0
-----

V1.0 Pros:

- Fixes the bugs highlighted in 3259/3254 by removing the .choose() dependency.
- Handles large condlist/choicelist inputs (e.g.  2^22 conditions in around 50 seconds).
- 2-3x faster typically on scalar classification (e.g. select([...],[2,5,13,20]).
- Better internal documentation.
- Better detection/reporting of bad input.
- Test harness included.
- Similar speed to np.select for ndarray classification with all elements the same shape.

V1.0 Cons:

- Slower speed with mixed ndarray/scalar condlists. Not sure this is a problem (why would you use True instead of default? why would you use False?). 
- I don't think it will support broadcasting, but I don't have a suitable real-world test case to try out.


Numpy devs: you are very welcome to include all or part of this code into numpy.

USAGE
=====

1. Download.

2. Add this line to your code: 
  import simplesel as ss

Then you can use ss.select anywhere that you would use np.select.

ACKNOWLEDGEMENTS
================

Thank you to the Norwegian Forest and Landscape Institute for allowing me to tidy up and share this work. 

LICENSE
=======

Published under the MIT license with permission. Copyright (C) 2013 Norwegian Forest and Landscape Institute (contact: Graeme B Bell), except the function definition re-used from numpy.select. 

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
