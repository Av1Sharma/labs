"""
A module with several recursive functions

YOUR NAME AND NETID HERE
THE DATE COMPLETED HERE
"""


# IMPLEMENT BOTH OF THESE FUNCTIONS

def remove_dups(thelist):
    """
    Returns a COPY of thelist with adjacent duplicates removed.
    
    Example: for thelist = [1,2,2,3,3,3,4,5,1,1,1]
    the answer is [1,2,3,4,5,1]
    
    Parameter thelist: The list to modify
    Precondition: thelist is a list of ints
    """
    return [] # Stub return.  Replace this.


def oddsevens(thelist):
    """
    Returns a COPY of the list with odds at front, evens in the back.

    Odd numbers are in the same order as thelist. Evens are reversed.

    Example:
        oddsevens([3,4,5,6]) returns [3,5,6,4].
        oddsevens([2,3,4,5,6]) returns [3,5,6,4,2].
        oddsevens([1,2,3,4,5,6]) returns [1,3,5,6,4,2].

    Parameter thelist: The list to modify
    Precondition: thelist is a list of ints (may be empty)
    """
    # HINT: How you break up the list is important.  A bad division will
    # make it almost impossible to combine the answer together.
    # However, if you look at all three examples in the specification you
    # will see a pattern that should help you define the recursion.
    return [] # Stub return.  Replace this.


### OPTIONAL EXERCISES ###

def replace(thelist,a,b):
    """
    Returns a COPY of thelist but with all occurrences of a replaced by b.

    Example: replace([1,2,3,1], 1, 4) = [4,2,3,4].

    Parameter thelist: The list to count from
    Precondition: thelist is a list of ints

    Parameter a: The value to replace
    Precondition: a is an int

    Parameter b: The value to replace with
    Precondition: b is an int
    """
    # HINT: Divide and conquer only applies to one of the arguments, not all three
    return [] # Stub return.  Replace this.


def remove_first(thelist, v):
    """
    Returns a COPY of thelist but with the FIRST occurrence of v removed (if present).
    
    Note: This can be done easily using the method index. Don't do that.
    Do it recursively.
    
    Parameter thelist: the list to search
    Precondition: thelist is a list of ints
    
    Parameter v: the value to search for
    Precondition: v is an int
    """
    return [] # Stub return.  Replace this.


def num_digits(n):
    """
    Returns the number of the digits in the decimal representation of n.
    
        Example: num_digits(0) = 1
        Example: num_digits(3) = 1
        Example: num_digits(34) = 2
        Example: num_digits(1356) = 4
    
    Parameter n: the number to analyze
    Precondition: n >= 0 is an int
    """
    return 0 # Stub return.  Replace this.


def into(n, c):
    """
    Returns the number of times that c divides n,

        Example: into(5,3) = 0 because 3 does not divide 5.
        Example: into(3*3*3*3*7,3) = 4.

    Parameter n: the number to analyze
    Precondition: n >= 1 is an int

    Parameter c: the number to divide by
    Precondition: c > 1 are ints.
    """
    return 0 # Stub return.  Replace this.


def separate(nlist):
    """
    Returns: A tuple separating nlist into negative and non-negative portions
    
    This function returns a tuple (neg,pos). The value neg is a list of all of
    the negative elements of nlist (in their order from nlist), while pos is a
    list of all the positive elements of nlist (in their order from nlist).
    
    Examples: 
        separate([1, -1, 2, -5, -3, 0]) returns ([-1, -5, -3], [1, 2, 0])
        separate([-1, -5, -3]) returns ([-1, -5, -3],[])
        separate([1, 2, 0]) returns ([],[1, 2, 0])
        
    Parameter nlist: The list to separate
    Precondition: nlist is a (possibly empty) list of numbers
    """
    return ([],[]) # Stub return.  Replace this.


def flatten(thelist):
    """
    Returns a COPY of thelist flattened to remove all nested lists

    Flattening takes any nested list and recursively dumps its contents into the
    parent list.

    Examples:
        flatten([[1,2],[3,4]]) is [1,2,3,4]
        flatten([[1,[2,3]],[[4],[5,[6,7]]]]) is [1,2,3,4,5,6,7]
        flatten([1,2,3]) is [1,2,3]

    Parameter thelist: the list to flatten
    Precondition: thelist is a list of either ints or lists which satisfy the precondition
    """
    return [] # Stub return.  Replace this


def namelist(p):
    """
    Returns a SORTED list of the first names any ancestor of p.
    
    We say that some is an ancestor of p if
        
        (1) They are either the mother or father of Persin p
        (2) They are an ancestor of the mother or father of p
    
    If Person p has no known ancestors, this function returns the empty list
    
    Parameter p: a person to
    Precondition: p is a Person object
    """
    return [] # Stub return.  Replace this.