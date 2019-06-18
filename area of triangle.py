import math
print("Enter all values in SI Unit(Metre)")
Side1=int(input("Enter first side of triangle"))
Side2=int(input("Enter the second side"))
Side3=int(input("Enter the third side"))

semiperimeter=(Side1+Side2+Side3)//2
Area=(semiperimeter*(semiperimeter-Side1)*(semiperimeter-Side2)*(semiperimeter-Side3))**(1/2)
print("The area of the triangle with given values is"+str(Area)+"sq.m")