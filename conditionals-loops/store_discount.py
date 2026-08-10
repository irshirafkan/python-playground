# Store Discount Exercise
#
# A store offers special discounts to its customers.
# The discount rules are as follows:
#
# If the purchase amount is more than 50,000 tomans, a 20% discount is applied.
# If the purchase amount is between 20,000 and 50,000 tomans, a 10% discount is applied.
# If the purchase amount is less than 20,000 tomans, no discount is applied.
#
# Write a program that receives the purchase amount from the user
# and displays the final amount.
#
# Sample Input:
#
# 55000
#
# Sample Output:
#
# 44000

price = int(input())

if price > 50000:
    final_price = price * 0.8
elif price >= 20000:
    final_price = price * 0.9
else:
    final_price = price

print(int(final_price))