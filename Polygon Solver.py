import math
# this is the area solver for a square
print("*"*70) # helps to keep things easier to read
print("Square area solver")
side = float(input("What is the side length of the square? (in cm): "))
print(f"The area of the sqaure is {round(side**2,6)} cm^2, and {round((side**2)/10000,6)} m^2") # area
print("*"*70)
# this is the area solver for a rectangle
print("Rectangle area solver")
print("*"*70)
leng = float(input("What is the length of the retangle? (in cm): ")) # gets length
wid = float(input("What is the width of the rectangle? (in cm): ")) # gets width
print(f"The area of the rectangle is {round(leng * wid,6)} cm^2, and {round((leng*wid)/10000,6)} m^2") # area
print("*"*70)
# this is the area solver for a circle
print("Circle area solver")
print("*"*70)
r = float(input("What is the radius of the circle? (in cm): "))
print(f"The area of the circle is {round(math.pi * r**2,6)} cm^2, and {round((math.pi * r**2)/10000,6)} m^2")
print("*"*70)
# this is the all shapes solver
print("Square/Circle area and volume solver")
print("*"*70)
sr = float(input("What is the measurement of side/radius you want solved? (in cm): "))
print(f"The area of the square is {round(sr**2,6)} cm^2, and {round((sr**2)/10000,6)} m^2")
print(f"The area of the circle is {round(math.pi*sr**2,6)} cm^2, and {round((math.pi*sr**2)/10000,6)} m^2")
print(f"The volume of the cube is {round(sr**3)} cm^3, and {round((sr**3)/10000)} m^3")
print(f"The volume of the sphere is {round(math.pi*(4/3)*sr**3, 6)} cm^3, and {round((math.pi*(4/3)*sr**3/10000),6)} m^3")
print("*"*70)