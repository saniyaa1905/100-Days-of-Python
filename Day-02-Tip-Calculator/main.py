print("Welcome to the Tip Calculator!")

bill = float(input("What is your total bill? ₹"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

total_tip = bill * tip / 100
total_bill = bill + total_tip
bill_per_person = total_bill / people

print(f"Each person should pay: ₹{bill_per_person:}")
