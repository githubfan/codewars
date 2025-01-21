# Welcome. In this kata, you are asked to square every digit of a number and concatenate them.
# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1. (81-1-1-81)
# Example #2: An input of 765 will/should return 493625 because 72 is 49, 62 is 36, and 52 is 25. (49-36-25)
# Note: The function accepts an integer and returns an integer.
import math

def square_digits(num):
    num = str(num)
    finalnum = ""
    prenumlist = []
    for item in num:
        prenumlist.append(int(int(item)*int(item)))
    for item in prenumlist:
        finalnum = finalnum + str(item)
    finalnum = int(finalnum)
    return finalnum

square_digits(9119)

def square_digits(num):
    num = str(num)
    ans = ''
    for i in num:
        ans += str(int(i)**2)
    return int(ans)