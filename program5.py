# welcome to the tip calculator!
# What was the total bill?
# How much tip would you like to give? 10, 12, or 15?
# How many people to split the bill?
# Each person Should pay:

# print("Welcome to the tip Calculator!")
# bill = float(input("What was the total bill? $" ))
# tip = int(input("What percentage tip would you like to give? 10, 12 , or 15"))
# people = int(input("How many people to split the bill?"))
# bill_with_tip = tip/100 * bill + bill
# print(bill_with_tip)

print("Welcome to the tip Calculator!")
bill = float(input("What was the total bill? $" ))
tip = int(input("What percentage tip would you like to give? 10, 12 , or 15"))
people = int(input("How many people to split the bill?"))
bill_with_tip = bill * ( 1+tip/100 )
print(bill_with_tip)



