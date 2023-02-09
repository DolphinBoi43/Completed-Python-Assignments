'''
Conditional Favorite Animal
by: DolphinBoi43

Objective:
- if numbers entered meet certain conditions, the output tells user if that is or isn't its favorite animal
'''

title = 'This Is A Test'
fav_ani = 0
print(f'{title:_^30}')
print()
x = float(input("Whats the first number? : "))
y = float(input("Whats the second numbber? : "))

if x > y:
    print("The first number is bigger")
    fav_ani = 1
elif x < y:
    print("The second number is bigger")
    fav_ani = 1
elif x == y:
    print("They are equal")
    fav_ani = 0
print()
ani = (input("What is your favorite animal? : "))

if fav_ani == 1:
    print(f"The {ani.title()} is also my favorite animal!")
if fav_ani == 0:
    print(f"The {ani.title()} is not my favorite animal...")
