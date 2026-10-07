def removeall(alist,n):
    """
    Returns a copy of alist, removing all instances of n
    
    Example: removeall([1,2,2,3,1],1) returns [2,2,3]
    Example: removeall([1,2,2,3,1],2) returns [1,3,1]
    Example: removeall([1,2,2,3,1],4) returns [1,2,2,3,1]
    Example: removeall([1,1,1],1) returns []
    Example: removeall([],1) returns []
    
    Parameter alist: the list to copy
    Precondition: alist is a list of numbers (float or int)
    
    Parameter n: the number to remove
    Precondition: n is a number
    """
    res = []

    for num in alist:
      if num != n:
        res.append(num)
    return res