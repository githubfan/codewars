# The maximum sum subarray problem consists in finding the maximum sum of a contiguous
# subsequence in an array or list of integers:
#
# max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# # should be 6: [4, -1, 2, 1]
# Easy case is when the list is made up of only positive numbers and
# the maximum sum is the sum of the whole array. If the list is made up of only
# negative numbers, return 0 instead.
#
# Empty list is considered to have zero greatest sum. Note that the empty list or
# array is also a valid sublist/subarray.


def max_sequence(arr):
    if arr == []:
        return 0
    subtractVal = 1
    currentHighestOutput = 0
    for distance in range(1, len(arr)):
        distanceVal = 0
        for position in range (0, len(arr)):
            outputNum = 0
            currentPos = position
            distanceVal = 0
            currentArray = []
            while distanceVal < distance + 1:
                try:
                    outputNum = outputNum + arr[currentPos]
                    currentArray.append(arr[currentPos])
                except IndexError:
                    pass
                distanceVal += 1
                currentPos += 1
            if outputNum > currentHighestOutput:
                currentHighestOutput = outputNum
    return currentHighestOutput



print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
