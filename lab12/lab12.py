def put_in(alist,value):
    """
    MODIFIES the sorted list to include value, resorting as necessary.
    
    This function is a PROCEDURE.  It does not return a new list.  Instead,
    it modifies the existing list.
    
    Examples:
        If a = [0,2,3,4], put_in(a,1) makes a = [0,1,2,3,4]
        If a = [0,2,3,4], put_in(a,2) makes a = [0,2,2,3,4]
        If a = [], put_in(a,3) makes a = [3]
    
    Parameter a: The list to append to
    Precondition: a is a sorted list of ints
    
    Parameter value: The value to append
    Precondition: value is an int
    """
    if len(alist) == 0:
        alist.append(value)
    elif index == len(alist):
        alist.append(value)
    elif alist[index] < value:
        put_in(alist, value, index + 1)
    else:
        alist.insert(index, value)
    


# a = []
# put_in(a, 3)
# print(a)
# a = [0, 2, 3, 4]
# put_in(a, 1)
# print(a)
# a = [0, 2, 3, 4]
# put_in(a, 2)
# print(a)
# a = []
# put_in(a, 3)
# print(a)
a = [0, 1, 2, 3, 4]
put_in(a, -1)
print(a)
