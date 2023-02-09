'''
Meal Price Calculator: 03 Prove Assignment
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

IF I COULD
- add function request more funds if cash short or card is not authorized
- add function in no money is recieved at all and call the police
- Prevent crashes if no input recieved
'''
def Bills():
    ones = int(input("How many $1 bills? : "))
    fives = int(input("$5 bills? : "))
    tens = int(input("$10 bills? : "))
    twenty = int(input("$20 bills? : "))
    fifty = int(input("$50 bills? : "))
    hund = int(input("$100 bills? : "))
    print()
    print("- Payment Recieved -")
    cash_t = float((ones*1) + (fives*5) + (tens*10) + (twenty*20) + (fifty*50) + (hund*100))
    print(f"Cash Total: $ {cash_t}")
    print()
    print("- Payment Confirmed - ")
    print()
    R_total = round(grat, 2)
    change = round(cash_t - R_total,2)
    print(f"Change : $ {change}")    
    
# setting meal prices for kid and adult meals
kid = input("What is the price of a kids meals? : $ ")
adult = input("what is the price of adult meals? : $ ")
# convert string to float for meal prices
kid = float(kid) 
adult = float(adult)
# setting amount of kids and adults
num_k = input("How many kids are ordering? : ")
num_a = input("How many adults are ordering? : ")
# convert num_k and num_a to int
num_k = int(num_k)
num_a = int(num_a)
# get sales tax from user
tax = input("What is the sales tax rate? (%) : ")
# convert to float and decimal 
tax = float(tax)
tax = tax/100
print()
# printing subtotal, tax and total
subt = round((kid*num_k) + (adult*num_a), 2)
print(f"Subtotal: $ {subt}")
tax = round(subt * tax, 2)
print(f"Tax : $ {tax}")
grat = round(subt + tax, 2)
print(f"Total : $ {grat}")
print()
# ask for payment type
pay = ''
while True:
    pay = input('Would you like to pay with (1)Card or (2)Cash : ')
    pay = int(pay)
    if pay == 1: #Pay withcard
        print()
        print("- Card payment is selected -")
        print()
        tip = ''
        while True: #Tipping
            tip = input('Would you like to tip: (1)Yes or (2)No : ')
            print()
            tip = int(tip)
            if tip == 1:
                tip_per = input("How much would you like to tip? (%) : ")
                print()
                tip_per = float(tip_per)
                tip_per = (tip_per/100)*grat
                R_total = round(grat + tip_per, 2)
                print(f"Payment Total: $ {R_total}")
                print()
                print("- Payment Recieved -")
                break
            if tip == 2:
                print()
                print("Cheapskate")
                print()
                R_total = round(grat,2)
                print(f"Payment Total: $ {R_total}")
                print()
                print("- Payment Recieved -")
                break
        break

    if pay == 2: #Pay in Cash
        print()
        print("- Cash payment is selected -")
        print()
        tip = ''
        while True:
            tip = input('Would you like to tip: (1)Yes or (2)No : ')
            print()
            tip = int(tip)
            if tip == 1:
                tip_per = input("How much would you like to tip? (%) : ")
                print()
                tip_per = float(tip_per)
                tip_per = (tip_per/100)*grat
                R_total = round(grat + tip_per, 2)
                print(f"Payment Total: $ {R_total}")
                print()
                while True:
                    cash = input("Can you pay in (1)exact change or (2)use bills: ")
                    print()
                    cash =int(cash)
                    if cash == 1:
                        print("- Payment Recieved -")
                        print()
                        print("- Payment Confirmed -")
                        break
                    if cash == 2:
                        Bills()
                        break      
                break       
            if tip == 2:        
                print("Cheapskate")
                print()
                while True:
                    cash = int(input("Can you pay in (1)exact change or (2)use bills: "))
                    print()
                    if cash == 1:
                        print("- Payment Recieved -")
                        print()
                        print("- Payment Confirmed -")
                        break
                    if cash == 2:
                        Bills()
                        break
                break
        break
#End of Payment/Tipping Processing
print()
print("Thank you for your patronage and have a nice day!")
print()