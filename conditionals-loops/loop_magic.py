# A wizard chooses n (number of steps) and x (initial number).
# If x is odd, double it and subtract 1.
# If x is even, divide it by 2.
# Repeat the operation exactly n times.
# Input: 1 <= n <= 20, 1 <= x <= 1000



n = int(input())
x = int(input())

for i in range(n):
    if x % 2 == 1:
        x = 2 * x - 1
    else:
        x = x // 2

print(x)