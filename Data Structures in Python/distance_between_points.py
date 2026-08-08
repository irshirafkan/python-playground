# Distance Between Two Points with a Tuple Exercise
#
# Create a tuple named coordinates that contains the coordinates
# of point A on the plane ((4, 3) = A).
# Then write code to calculate the distance from this point
# to the origin (0, 0).
#
# To calculate the distance between two points on the coordinate plane,
# use the Euclidean distance formula:
#
# distance = √((x₂ - x₁)² + (y₂ - y₁)²)

coordinates  = (4, 3)

x = coordinates[0]
y = coordinates[1]

origin_x = 0
origin_y = 0

distance = ((x - origin_x) ** 2 + (y - origin_y) ** 2) ** 0.5

print(distance)