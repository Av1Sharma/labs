def clamp(alist,min,max):
    """
    MODIFIES the list so that every element is between min and max.
    
    Any number in the list less than min is replaced with min.  Any number
    in the list greater than max is replaced with max. Any number between
    min and max is left unchanged.
    
    This is a PROCEDURE. It modifies alist, but does not return a new list.
    
    Example: if alist is [-1, 1, 3, 5], then clamp(thelist,0,4) changes
    alist to have [0,1,3,4] as its contents.
    
    Parameter alist: the list to modify
    Precondition: alist is a list of numbers (float or int)
    
    Parameter min: the minimum value for the list
    Precondition: min <= max is a number
    
    Parameter max: the maximum value for the list
    Precondition: max >= min is a number
    """
    for x in range(len(alist)):
        if alist[x] < min:
            alist[x] = min
        elif alist[x] > max:
            alist[x] = max
