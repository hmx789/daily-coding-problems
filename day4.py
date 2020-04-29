# Good morning! Here's your coding interview problem for today.

# This problem was asked by Stripe.

# Given an array of integers, find the first missing positive integer in linear time and constant space.

# In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

# You can modify the input array in-place


def findMissingPositiveNum(arr):
    containsOne = False
    arrLength = len(arr)

    # Update all the values that are
    # greater than N or less than 0
    # to be 1
    for i in range(arrLength):
        if arr[i] is 1:
            containsOne = True
        elif arr[i] < 1 or arr[i] > arrLength:
            arr[i] = 1

    # We know 1 is the smallest number possible and if it is not seen
    # that means we have to return 1
    if not containsOne:
        return 1

    # Mark all elements in the array that are within our range of 1->N
    # to be a negative number
    for i in range(arrLength):
        indexToUpdate = abs(arr[i]) - 1
        if arr[indexToUpdate] >= 0:
            arr[indexToUpdate] = -1

    # The first index that is not negative means, we have not seen it yet
    # is our smallest positive number
    for i in range(arrLength):
        if arr[i] > 0:
            return i+1

    # If we have seen all the numbers then that means we are missing the max number
    return arrLength + 1


print("result: " + str(findMissingPositiveNum([2, 3, -1])))
