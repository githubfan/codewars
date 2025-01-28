# Complete the solution so that the function will break up camel casing, using a space between words.

# Example
# "camelCasing"  =>  "camel Casing"
# "identifier"   =>  "identifier"
# ""             =>  ""


def solution(s):
    i = 0
    newOutput = ""
    splittingPoints = []
    splittingNeeded = False
    for letter in s:
        if letter == letter.upper():
            splittingPoints.append(i)
            splittingNeeded = True
        i += 1

    if splittingNeeded:
        lastItem = 0
        firstIteration = True
        for item in splittingPoints:
            if firstIteration:
                newOutput = newOutput + s[lastItem:item]
                lastItem = item
                firstIteration = False
            else:
                newOutput = newOutput + " " + s[lastItem:item]
                lastItem = item
        newOutput = newOutput + " " + s[lastItem:]

    else:
        newOutput = s
    return newOutput

