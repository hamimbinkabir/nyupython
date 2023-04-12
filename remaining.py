def remainingwords(data: str) -> str:
    s = data.split()
    ret=" "
    for x in s:
        if x!=s[0]:
          ret +=x + " "

    ret=ret.rstrip()
    ret=ret.lstrip()
    return ret