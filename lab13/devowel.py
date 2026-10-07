def devowel(word):
    """
    Returns a copy of word with all vowels removed.
    
    The vowels are 'a', 'e', 'i', 'o', and 'u'.
    
    Example: devowel('apple') returns 'ppl'
    Example: devowel('yearn') returns 'yrn'
    Example: devowel('amplify') returns 'mplf'
    
    Parameter word: the string to devowel
    Precondition: word is a string of lowercase letters
    """
    vowels = ['a', 'e', 'i', 'o', 'u']
    res = ''
    for x in range(len(word)):
        if word[x] in vowels:
            continue
        else:
            res += word[x]

    return res
