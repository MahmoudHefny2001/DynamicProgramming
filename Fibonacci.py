"""

Write a function Fibonacci(n) that takes in a number as an argumnet.
The function should return the n-th number of the Fibonacci sequence.
------------------------------------------------------------------
The 1st and 2nd number of the sequence is 1.
To generate the next number of the sequence, we sum the previous two.

n:            1, 2, 3, 4, 5, 6, 7,  8,  9,  ...
Fibonacci(n): 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

"""

import sys
sys.setrecursionlimit(1500)



# Exponential Time Algorithm
def Fibonacci(number: int)->int:
    if(number <= 0):
        return "Invalid input"
    else:
        if(number == 1 or number == 2):
            return 1

        else:
            return Fibonacci(number-1) + Fibonacci(number-2)
    

# Memoization
def Fibonacci_2(number: int, memoization: hash = {})->int:
    if (number < 1):
        return "Invalid input"
    
    else:
        if (number == 1 or number == 2):
            return 1
    
        elif (number in memoization):
            return memoization[number]

        memoization[number] = Fibonacci_2(number-1, memoization) + Fibonacci_2(number-2, memoization)
        return memoization[number]



# result = Fibonacci(50)
# print(result)

# result = Fibonacci_2(1000)
# print(result)