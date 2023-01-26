"""
Write a function 'canSum(targetSum, numbers)' that takes in
a targetSum and an array of numbers as arguments.

The function should return a boolean indicating whether or not it is possible to generate
the targetSum using numbers from the array.

You may use an element of the array as many times as needed.

You may assume that all input numbers are nonnegative.

"""

# example: canSum(7, [5, 3, 4 , 7]) --> True

def canSum(targetSum: int, numbers: list)->bool:
    if(targetSum == 0):
        return True
    
    if(targetSum < 0): 
        return False
    
    for number in numbers:
        remainder = targetSum - number
        if (canSum(remainder, numbers) == True):
            return True
        
    return False


def memoizedCanSum(targetSum: int, numbers: list, memo: hash = {})->bool:
    if(targetSum in memo):
        return memo[targetSum]

    if(targetSum == 0):
        return True
    
    if(targetSum < 0): 
        return False
    
    for number in numbers:
        remainder = targetSum - number
        if (memoizedCanSum(remainder, numbers, memo) == True):
            memo[targetSum] = True
            return True
        
    memo[targetSum] = False
    return False


# print(canSum(7, [2, 3]))        # True
# print(canSum(7, [5, 3, 4, 7]))  # True
# print(canSum(7, [2, 4]))        # False
# print(canSum(8, [2, 3, 5]))     # True
# print(canSum(300, [7, 14]))     # False


print(memoizedCanSum(7, [2, 3]))        # True
print(memoizedCanSum(7, [5, 3, 4, 7]))  # True
print(memoizedCanSum(7, [2, 4]))        # False
print(memoizedCanSum(8, [2, 3, 5]))     # True
print(memoizedCanSum(300, [7, 14]))     # False
        
    
        
