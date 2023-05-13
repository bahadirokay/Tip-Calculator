"""#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Round the result to 2 decimal places."""
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? Exp; %10, %12, or %15? "))
people = int(input("How many people to split the bill?"))

percentage_tip = (tip / 100)
new_bill = bill + bill * percentage_tip
total = round(new_bill / (float(people)), 2)
print(f"Each person should pay: ${total}")
