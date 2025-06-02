from openscad import *

# Create two cubes
c1 = cube([5,5,5])
c2 = cube([3,3,10])

# Translate the cube by 7 units up
c2 = c2.translate([0,0,7])

# Display the result
result = c1 | c2
show(result)
