def europeanize(date):
    """
    Returns a European version of this date (type is a string).
    
    Days and months are padded (if necessary) to become two digits each.
    
    Examples:
        europeanize('3/6/12') is '06/03/12'
        europeanize('01/29/11') is '29/01/11'
    
    Parameter date: the date to convert
    Precondition: date a string representing a US date.
    """


    index = date.find('/')

    monthyear = date[index+1:]

    stop = monthyear.find('/')

    month = monthyear[:stop]

    if len(month) < 2:
        month = '0' + month

    day = date[: index]
    if len(date[: index]) < 2:
        day = '0' + date[: index]

    print(month + '/' + day + monthyear[stop:])

europeanize('12/4/18')

