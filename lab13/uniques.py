def uniques(alist):
    """
    Returns: The number of unique elements in the list. 
    
    Example: uniques([5, 9, 5, 7]) returns 3
    Example: uniques([5, 5, 1, 'a', 5, 'a']) returns 3
    
    Parameter alist: the list to check (WHICH SHOULD NOT BE MODIFIED)
    Precondition: alist is a list.
    """
    unique_items = []
    
    for item in alist:
        if item not in unique_items:
            unique_items.append(item)
            
    return len(unique_items)
