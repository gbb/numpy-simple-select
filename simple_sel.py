import numpy as np

# Simple select (replacement for numpy.select) v1.0

# Graeme B Bell, Norwegian Forest & Landscape Institute. grb@skogoglandskap.no

# NOTES
# 1. Fixes two bugs (ARG_MAX 32 limit, return value/type for input of ([],[]))
# 2. Improved detection of bad input parameters.
# 3. Faster than np.select when given scalar condlist parameters. 
# 4. Similar or slightly slower where condlist are equally shaped ndarrays.
# 5. Slower for mixed scalar/ndarray condlist.
# 6. Does not support advanced broadcasting in condlist/choicelist, only scalar/one size ndarray.
#    (how many use cases actually need this?)
# 7. Improved internal documentation.
# 8. The function description is derived from numpy.select()

def select(condlist, choicelist, default=0):
    """
    Return an array drawn from elements in choicelist, depending on conditions.

    Parameters
    ----------
    condlist : list of bool ndarrays
        The list of conditions which determine from which array in `choicelist`
        the output elements are taken. When multiple conditions are satisfied,
        the first one encountered in `condlist` is used.
    choicelist : list of ndarrays and/or scalars.
        The list of arrays from which the output elements are taken. It has
        to be of the same length as `condlist`. Scalars will be cast to ndarrays.
    default : scalar, optional
        The element inserted in `output` when all conditions evaluate to False.

    Returns
    -------
    output : ndarray
        The output at position m is the m-th element of the array in
        `choicelist` where the m-th element of the corresponding array in
        `condlist` is True.

    See Also
    --------
    numpy.select : Original version. 
    numpy.where : Return elements from one of two arrays depending on condition.
    numpy.take, numpy.choose, numpy.compress, numpy.diag, numpy.diagonal

    Examples
    --------
    >>> x = np.arange(10)
    >>> condlist = [x<3, x>5]
    >>> choicelist = [x, x**2]
    >>> ss.select(condlist, choicelist)
    array([ 0,  1,  2,  0,  0,  0, 36, 49, 64, 81])

    """

    # Clone the input lists to prevent side effects to the parameter lists:
    condlist = list(condlist)
    choicelist = list(choicelist)

    # Check that the inputs are acceptable.

    # Check the size of condlist and choicelist are the same, or abort.
    if len(condlist) != len(choicelist):
        raise ValueError('list of cases must be same length as list of conditions')

    # If condlist/choicelist are empty, return the default value immediately.
    if len(condlist)==0:
        return np.array([]) 

    # If cond array is not an ndarray in boolean format or scalar bool, abort.
    for index,item in enumerate(condlist):
        if type(item) is not np.ndarray:
            if type(item) is not bool:
                raise ValueError('invalid entry in choice array: should be boolean ndarray')
        else:
            if item.dtype != 'bool':
                raise ValueError('invalid entry in choice array: should be boolean ndarray')

    # Pre-process any scalar list items into ndarray scalars. 
    for index, item in enumerate(condlist):
        if type(item) is not np.ndarray:
            condlist[index]=np.array(item) 

    for index, item in enumerate(choicelist):
        if type(item) is not np.ndarray:
            choicelist[index]=np.array(item) 

    # Create dictionaries noting the sizes of the items in the lists. 
    cond_sizes = {} ; choice_sizes = {}    

    for i in range(0,len(condlist)):
        cond_sizes[condlist[i].shape]=True 
        choice_sizes[choicelist[i].shape]=True 
     
    sizes=cond_sizes.copy() 
    sizes.update(choice_sizes)

    # Test for ndarrays with no data.
    if (0,) in sizes.keys():
        raise ValueError('ndarray containing no items is present')

    # Test that there is not more than one shape of array present, excluding ()s.
    if len(sizes.keys())>2 or (len(sizes.keys())==2 and () not in sizes):
        raise ValueError('cannot operate with mixed ndarray shapes. Sizes:', sizes.keys())

    # calculate the shape of the arrays (if we have two shapes, then exclude ()).
    if len(sizes.keys())==1:    
        target_shape=(sizes.keys())[0]    
    else:         
        del sizes[()]    
        target_shape=(sizes.keys())[0]    
        sizes[()]=True

    # Reverse the condlist to put lowest priority (end of condlist) conditions at the beginning.
    condlist.reverse()
    choicelist.reverse()

    # Add the default condition as item zero, so that if no condition matches, we get the default.
    condlist = [True] + condlist    # true never gets used, just here to synchronize the sizes.
    choicelist = [np.ones_like(choicelist[0])*default] + choicelist    # fill with default value.

    # This is the main loop that selects the matching condition for each data item.
    # Iterate from start to end, noting the highest priority matching condition with maximum().
    # N.b. because of the use of multiplication here, the condlist *must* be boolean, not int.
    result=np.array([0]);         

    for i in range(1,len(condlist)):
        tmpresult=condlist[i]*i 
        result=np.maximum(result,tmpresult)        

    # Finally index into choicelist according to the condition number that was matched. 

    # If all choices are scalar we can do the indexing faster this way
    # Flatten the choicelist's ndarrays into one big ndarray and index into it.
    if len(choice_sizes.keys()) and () in choice_sizes.keys():
         npcl = np.array(choicelist).flatten()
         return npcl.take(result)
     
    # Otherwise standardise the choicelist output shapes, stack them and fancy index in.
    for i in range(len(choicelist)): 
        if choicelist[i].shape != target_shape:
            choicelist[i]=np.resize(choicelist[i],target_shape)

    npcl=np.column_stack(choicelist)

    return npcl.take(result+np.arange(0, len(result) * npcl.shape[1], npcl.shape[1]))
