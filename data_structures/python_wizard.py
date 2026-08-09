# The Python Wizard Exercise
#
# A wizard has two magical sets named SetA and SetB.
# Each set contains several different numbers.
#
# SetA = {1, 2, 3, 4}
# SetB = {3, 4, 5, 6}
#
# - Find the union of all elements in both sets.
# - Find the intersection shared by SetA and SetB.
#
# Your task is to:
#
# - Find the union of SetA and SetB and represent it with u.
# - Find the intersection of SetA and SetB and represent it with i.
# - Display the outputs of items 1 and 2 in two lines, respectively,
#   in the following format.

SetA = {1, 2, 3, 4}
SetB = {3, 4, 5, 6}

u = SetA | SetB
i = SetA & SetB

print(u)
print(i)