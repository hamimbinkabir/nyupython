def isleapyear(year: int) -> bool:
    if year==2000:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 400 == 0:
        return True
    else:
        return False