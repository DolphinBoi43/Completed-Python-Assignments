'''
Fahrenheit to Celsius
By: DolphinBoi43

Program must be able to:
- Convert Fahrenheit to Celsius
- Print to 1 decimal place without rounding. That's dumb
'''
f = input("What is the Temperature (in Fahrenheit): ")
f = float(f)
c = (f - 32) * (5 / 9)
print()
print(f"The Temprature is {c:.1f} Degrees Celsius")
print()