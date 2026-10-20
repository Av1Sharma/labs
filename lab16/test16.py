"""
Unit test script for Lab 16

Authors: Walker M. White (wmw2), Lillian Lee (ljl2)
Date:    October 17, 2024
"""
import introcs
import person
import lab16


def test_remove_dups():
    """
    Tests for function remove_dups
    """
    print('Testing remove_dups')
    mylist = [1,2,2,3,3,3,4,5,1,1,1]
    introcs.assert_equals([],  lab15.remove_dups([]))
    introcs.assert_equals([3], lab15.remove_dups([3,3]))
    introcs.assert_equals([4], lab15.remove_dups([4]))
    introcs.assert_equals([5], lab15.remove_dups([5, 5]))
    introcs.assert_equals([1,2,3,4,5,1], lab15.remove_dups(mylist))

    # test for whether the code is really returning a copy of the original list
    introcs.assert_equals([1,2,2,3,3,3,4,5,1,1,1], mylist)
    introcs.assert_equals(False, mylist is lab15.remove_dups(mylist))


def test_oddsevens():
    """
    Tests for function oddsevens
    """
    print('Testing oddsevens')
    mylist = [1,2,3,4,5,6]
    introcs.assert_equals([],     lab16.oddsevens([]))
    introcs.assert_equals([3],    lab16.oddsevens([3]))
    introcs.assert_equals([3,4],  lab16.oddsevens([4,3]))
    introcs.assert_equals([-1,1,2,0],    lab16.oddsevens([-1,0,1,2]))
    introcs.assert_equals([1,3,5,6,4,2], lab16.oddsevens(mylist))

    # test for whether the code is really returning a copy of the original list
    introcs.assert_equals([1,2,3,4,5,6], mylist)
    introcs.assert_equals(False, mylist is lab16.oddsevens(mylist))


### OPTIONAL EXERCISES ###

def test_replace():
    """
    Tests for function replace
    """
    print('Testing replace')
    mylist = [5, 3, 3455, 74, 74, 74, 3]
    introcs.assert_equals([],  lab16.replace([], 1, 2))
    introcs.assert_equals([4], lab16.replace([5],5,4))
    introcs.assert_equals([5, 20, 3455, 74, 74, 74, 20], lab16.replace(mylist,3, 20))
    introcs.assert_equals([5, 3, 3455, 74, 74, 74, 3],   lab16.replace(mylist, 1, 3))

    # test for whether the code is really returning a copy of the original list
    introcs.assert_equals([5, 3, 3455, 74, 74, 74, 3], mylist)
    introcs.assert_equals(False, mylist is lab16.replace(mylist, 1, 3))


def test_remove_first():
    """
    Tests for function remove_first
    """
    print('Testing remove_first')
    introcs.assert_equals([],  lab15.remove_first([],3))
    introcs.assert_equals([],  lab15.remove_first([3],3))
    introcs.assert_equals([3], lab15.remove_first([3],4))
    introcs.assert_equals([3, 4, 4, 5],    lab15.remove_first([3, 4, 4, 4, 5],4))
    introcs.assert_equals([3, 5, 4, 4, 4], lab15.remove_first([3, 4, 5, 4, 4, 4],4))


def test_num_digits():
    """
    Tests for function sum_digits
    """
    print('Testing sum_digits')
    introcs.assert_equals(0,  lab16.sum_digits(0))
    introcs.assert_equals(1,  lab16.sum_digits(3))
    introcs.assert_equals(2,  lab16.sum_digits(34))
    introcs.assert_equals(3, lab16.sum_digits(345))


def test_into():
    """
    Tests for function into
    """
    print('Testing into')
    introcs.assert_equals(0, lab16.into(5, 3))
    introcs.assert_equals(1, lab16.into(6, 3))
    introcs.assert_equals(2, lab16.into(9, 3))
    introcs.assert_equals(2, lab16.into(18, 3))
    introcs.assert_equals(4, lab16.into(3*3*3*3*7,3))


def test_separate():
    """
    Tests for function separate
    """
    print('Testing separate')
    introcs.assert_equals(([],[]), lab16.separate([]))

    nlist = [1]
    result = lab16.separate(nlist)
    introcs.assert_equals(([],[1]), result)
    introcs.assert_not_equals(id(nlist),id(result[1]))

    nlist = [-1]
    result = lab16.separate(nlist)
    introcs.assert_equals(([-1],[]), result)
    introcs.assert_not_equals(id(nlist),id(result[0]))
    
    nlist = [1, 2, 0]
    result = lab16.separate(nlist)
    introcs.assert_equals(([],[1,2,0]), result)

    nlist = [-1, -5, -3]
    result = lab16.separate(nlist)
    introcs.assert_equals(([-1, -5, -3],[]), result)
    
    nlist = [1, -1, 2, -5, -3, 0]
    result = lab16.separate(nlist)
    introcs.assert_equals(([-1, -5, -3], [1, 2, 0]), result)
    introcs.assert_not_equals(nlist,result[0])


def test_flatten():
    """
    Tests for function flatten
    """
    print('Testing flatten')
    introcs.assert_equals([],  lab16.flatten([]))
    introcs.assert_equals([3], lab16.flatten([3]))
    introcs.assert_equals([3], lab16.flatten([[3]]))
    introcs.assert_equals([1,2,3,4], lab16.flatten([[1,2],[3,4]]))
    introcs.assert_equals([1,2,3,4,5,6,7], lab16.flatten([[1,[2,3]],[[4,[5,6]],7]]))
    introcs.assert_equals([1,2,3], lab16.flatten([1,2,3]))
    introcs.assert_equals([],  lab16.flatten([[[]],[]]))


def test_namelist():
    """
    Tests for function namelist
    """
    print('Testing name list')
    # GRANDPARENTS
    # John Smith Jr.
    gd1 = person.Person('John','Smith')
    gm1 = person.Person('Jane','Dare')

    gd2 = person.Person('John','Evans')
    gm2 = person.Person('Ellen',"O'Reilly")

    # PARENTS & Uncles
    # John Smith III
    d = person.Person('John','Smith',gm1,gd1)
    m = person.Person('Pamela','Evans',gm2,gd2)
    u = person.Person('Roger','Smith',gm1,gd1)

    # FINAL GENERATION
    # John Smith IV
    p = person.Person('John','Smith',m,d)
    s = person.Person('Ellen','Smith',m,d)
    c = person.Person('Douglas','Smith',None,u)
    
    introcs.assert_equals(['Ellen', 'Jane', 'John', 'John', 'John', 'Pamela'],lab16.namelist(p))
    introcs.assert_equals(['Ellen', 'Jane', 'John', 'John', 'John', 'Pamela'],lab16.namelist(s))
    introcs.assert_equals(['Jane', 'John', 'Roger'],lab16.namelist(c))
    introcs.assert_equals(['Jane', 'John'],lab16.namelist(d))
    introcs.assert_equals(['Jane', 'John'],lab16.namelist(u))
    introcs.assert_equals([],lab16.namelist(gd1))


# Script Code
if __name__ == '__main__':
    test_replace()
    test_oddsevens()

    # UNCOMMENT ANY OPTIONAL ONES YOU DO
    #test_remove_dups()
    #test_remove_first()
    #test_num_digits()
    #test_into()
    #test_separate()
    #test_flatten()
    #test_namelist()
    print('Module lab16 passed all tests.')