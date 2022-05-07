print("Welcome to the tip calculator.")

total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input(
    "What percentage tip would you like to give? 10, 12 or 15? "))
number_of_people = input("How many people to split the bill? ")

total_tip = tip_percentage / 100 * total_bill
total_bill = total_tip + float(total_bill)

# calculate bill for each person
bill_per_person = total_bill / int(number_of_people)

# round to 2 decimal places
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)

print(f"Each person should pay: ${final_amount}")
