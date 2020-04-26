# Good morning! Here's your coding interview problem for today.

# This problem was recently asked by Google.

# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

# Bonus: Can you do this in one pass?


def twoSum(arr, k):
    numberSet = set()
    for num in arr:
      # num + X = k or in other words x = k - num
        if (k - num) in numberSet:
            return True
        numberSet.add(num)
    return False


print(twoSum([10, 18, 15, 3], 18))
