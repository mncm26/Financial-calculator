# Capstone Project
# Creation of a program that allows the user to access two different financial calculators

import math

# I have added print("") to help check the output

print("FINANCE CALCULATOR")
print("")
print("MENU:")
print("Investment - to calculate the amount of interest you'll earn on your investment.")
print("Bond - To calculate the amount you'll have to pay on your home loan.")
print("")

choice_1 = input("Enter either 'Investment' or 'Bond' from the menu above to proceed:  ")

"Investment calculator"

if(choice_1 == "investment" or choice_1 == "Investment" or choice_1 == "INVESTMENT"):
    mon_amount = int(input("Enter the amount of monney you are depositing: "))
    int_rate = float(input("Enter the interest rate number (no percentage sign):"))
    year_num = int(input("Enter the number of years you are planning on investing: "))
    rate = int_rate/100

    print("")
    print("MENU:")
    print("Simple interest - calculated on the principal amount invested.")
    print("Compound interest - calculated on the principal amount and on interest already accumulated. ")
    print("")

    choice_2 = input("Enter either 'simple' or 'compound' interest from the menu above to proceed: ")
    if (choice_2 =="simple"  or choice_2=="Simple" or choice_2=="SIMPLE"):

        "Simple interest calculation"

        total_1 = mon_amount*(1 + rate * year_num)
        print("")
        print("The total amount at the end of your investment = ", total_1,"GBP")

    elif(choice_2 == "compound" or choice_2 == "Compound" or choice_2 == "COMPOUND"):

        "Compound interest calculation"

        total_2 = mon_amount*math.pow((1 + rate), year_num)
        total_3 = round(total_2 , 2)
        print("")
        print("The total amount at the end of your investment = ", total_3,"GBP")

    else:
        print("ERROR!, please start again.")

elif (choice_1 == "bond" or choice_1 == "Bond" or choice_1 == "BOND"):

    "Bond calculator"

    house_val = int(input("enter the present value of the house: "))
    interest_1 = float(input("Enter the interst rate (no percentage sign): "))
    month_num = int(input("Enter the length of the loan in months: "))
    r = (interest_1/100)/12

    "Repayment calculation"

    rep_num = (r * house_val)/( 1 - (1 + r) ** (-month_num))
    rep_num1 = round(rep_num,2)
    print("")
    print("Your monthly repayments are = ", rep_num1,"GBP")

else :
    print("ERROR!, please start again")
