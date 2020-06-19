import math

AB = int(input())
BC = int(input())

# To apply Tan, we'll have to actually have a right angle in the selected triangle
# So, using the property. Median to hypotenuse makes two isosceles triangles. AMB and BMC 
# So, AM = BM = MC => MBC = BCM
print(str(int(round(math.degrees(math.atan(AB/BC)), 0))) + '°')
