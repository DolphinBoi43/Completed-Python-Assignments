'''
Meal Price Calculator: 04 Prove Assignment
By: DolphinBoi43
Program must be able to:
- Get price of child meals from user (float)
- Get price of adult meals from user (float)
- number of children and adults (int)
- and computate sales tax (float)

Streach Goals
- added tipping input and commutation (insults add if no tipping)
- Payment type Cash or Card (Richie Rich if given too much money)
- gives change back to user
'''
#Payment Type Function
def Payment_Type():
    pay = int(input('Would you like to pay with (1)Card or (2)Cash : '))
    if pay == 1: #Pay withcard
        print()
        Card()
    if pay == 2: #Pay in Cash
        print()
        Bills()
# Tip function if selecting card payment option
def Tipper_Card():
    tip = int(input('Would you like to tip: (1)Yes or (2)No : '))
    print()
    if tip == 1:
        tip_per = float(input("How much would you like to tip? (%) : "))
        print()
        tip_per = (tip_per/100)*grat
        R_total = grat + tip_per
        print(f"Payment Total: $ {R_total:.2f}")
        print()
        print("- Payment Recieved -")
    if tip == 2:
       print()
       print("- Cheapskate -")
       print()
       R_total = grat
       print(f"Payment Total: $ {R_total:.2f}")
       print()
       print("- Payment Recieved -")
# Card Payment function
def Card():
    print()
    print("- Card payment is selected -")
    print()
    Tipper_Card()
#  Tip function for Cash Payment
def Tipper_Cash():
    tip = int(input('Would you like to tip: (1)Yes or (2)No : '))
    print()
    if tip == 1:
        ones = int(input("How many $1's? : "))
        fives = int(input("$5's? : "))
        tens = int(input("$10's? : "))
        twenty = int(input("$20's? : "))
        fifty = int(input("$50's? : "))
        hund = int(input("$100's? : "))
        print()
        print("- Payment Recieved -")
        print()
        cash_t = float((ones*1) + (fives*5) + (tens*10) + (twenty*20) + (fifty*50) + (hund*100))
        can_tip = cash_t - grat
        tip_per = float(input(f"How much would you like to tip? (${can_tip:.2f}) : "))
        print()
        R_total = cash_t - tip_per
        print(f"Payment Total: $ {R_total:.2f}")
        print()
        print(f"Change : ${R_total - grat:.2f}")
        print()
        print("- Payment Confirmed -")
    if tip == 2:
        print("- Cheapskate -")
        print()
        ones = int(input("How many $1's? : "))
        fives = int(input("$5's? : "))
        tens = int(input("$10's? : "))
        twenty = int(input("$20's? : "))
        fifty = int(input("$50's? : "))
        hund = int(input("$100's? : "))
        print()
        print("- Payment Recieved -")
        cash_t = float((ones*1) + (fives*5) + (tens*10) + (twenty*20) + (fifty*50) + (hund*100))
        print(f"Payment Total: $ {cash_t:.2f}")
        print()
        print(f"Change : ${cash_t - grat:.2f}")
        print()
        print("- Payment Confirmed -")
# Cash Payment Function
def Bills():
    print("- Cash Payment is selected -")
    print()
    Tipper_Cash()
print("Welcome to the Meal Price Calculatoe (1.1.1.1.1.1.1.1)")
print()
print("Lets Start Ordering!")
print()
# setting meal prices for kid and adult meals
kid = float(input("What is the price of a kids meals? : $ "))
adult = float(input("what is the price of adult meals? : $ "))
# setting amount of kids and adults
num_k = int(input("How many kids are ordering? : "))
num_a = int(input("How many adults are ordering? : "))
# get sales tax from user
tax = float(input("What is the sales tax rate? (%) : "))
tax = tax/100
print()
# printing subtotal, tax and total
subt = (kid*num_k) + (adult*num_a)
print(f"Subtotal: $ {subt:.2f}")
tax = subt * tax
print(f"Tax : $ {tax:.2f}")
grat = subt + tax
print(f"Total : $ {grat:.2f}")
print()
# ask for payment type
Payment_Type()
print()
print("Thank you for your patronage and have a nice day!")
print()