# Check to see if a string has the same amount of 'x's and 'o's.
# # The method must return a boolean and be case insensitive. The string can contain any char.
from operator import truediv


# Examples input/output:

# XO("ooxx") => true
# XO("xooxx") => false
# XO("ooxXm") => true
# XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
# XO("zzoo") => false

def xo(s):
    s = s.lower()
    numos = 0
    numxs = 0
    arexsos = True
    for letter in s:
        if letter == "o":
            numos = numos + 1
        elif letter == "x":
            numxs = numxs + 1
    if numos == numxs:
        return arexsos
    else:
        arexsos = False
        return arexsos

