def lesser_than(alist, value):
    count = 0
    for num in alist:
      if num < value:
         count +=1
    return count