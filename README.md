numpy-simple-select
===================

This is a drop-in replacement for the 'select' function in numpy. It has been reimplemented to fix long-standing bugs, improve speed in a common use case and improve internal documentation. It does not support advanced broadcasting, but many people may not require that for their own use of select(). 

It is a follow-up to my posts in the numpy repository:

https://github.com/numpy/numpy/issues/3259

https://github.com/numpy/numpy/issues/3254

I have also included a test harness which demonstrates the faults and allows a performance comparison.

Pros:

- Fixes the bugs highlighted in 3259/3254 by removing the .choose() dependency.
- Handles large condlist/choicelist inputs.
- 2-3x faster typically on scalar classification (e.g. select([...],[2,5,13,20]).
- Better internal documentation.
- Better detection/reporting of bad input.
- Test harness included.
- Similar speed to np.select for ndarray classification with all elements the same shape.

Cons:

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
