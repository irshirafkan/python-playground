# Chained Operators Exercise
#
# In Python, comparison operators can be used in a chain (Chaining).
# For example, the expression a < b <= c is equivalent to two separate
# comparisons: a < b and b <= c. This allows you to perform multiple
# comparisons in a single expression.
#
# Your task: Write a program that receives three numbers as input
# and checks whether the first number is less than the second number
# and the second number is less than or equal to the third number.
#
# Inputs:
#
# Three integers named a, b, and c.
#
# Outputs:
#
# If the condition a < b <= c is true, display True.
# Otherwise, display False.
#
# Sample Input:
#
# 5
# 10
# 15
#
# Sample Output:
#
# True
#
# Hint:
# To receive input from the user, you can use:
#
# a = input()
#
# If you want to convert the input to an integer at the same time:
#
# a = int(input())

a = int(input())
b = int(input())
c = int(input())

if a<b<=c :
    print(True)
else :
    print(False)