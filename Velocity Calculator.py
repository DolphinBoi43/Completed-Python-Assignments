'''
Speed of a Falling Object
By: DolphinBoi43
'''
from math import exp, sqrt

# All variables to be used
print("This is the Velocity Calculator 1.0.1")
print("~" * 40)
print("Please enter the following:")
m = float(input("Mass of object (in kg): "))
g = float(input("Acceleration due to Gravity (in m/s^2)(Earth = 9.8, Jupiter = 24): "))
t = float(input("How long is object falling (in seconds): "))
p = float(input("Density of fluid/air (air = 1.3, water = 1000): "))
a = float(input("Area of cross section (in m^2): "))
dc = float(input("Drag constant (sphere = 0.5, cylinder = 1.1): "))
# Calculating c
c = (1/2) * p * a * dc
#  Calculating Velocity
v = sqrt((m * g) / c) * (1 - exp( - ((sqrt(m * g * c)) / m) * t))
print()
print(f"The inner value for c is {c:.3f}")
print()
print(f"The Velocity of the object at {t} seconds is {v:.3f} m/s")
# Calculating terminal velocity after a certian amount of time which is solved by using t = v / a
v_terminal = sqrt((m * g) / c)
t_terminal = v_terminal / a
t_min = t_terminal // 60
t_sec = t_terminal % 60
print()
# If terminal velocity is reached sooner than one minuter we get the answer in seconds, if > than 60 seconds it's give in minutes and seconds
if t_terminal > 60:
    print(f"The object will reach a terminal velocity of {v_terminal:.3f} m/s after {round(t_min)} minutes and {t_sec:.1f} seconds")
if t_terminal < 60:
    print(f"The object will reach a terminal velocity of {v_terminal:.3f} m/s after {t_sec:.1f} seconds")
print()