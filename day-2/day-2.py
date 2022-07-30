print ("Welcome to the Tip Calculator!")
total_bill = float(input("What was the total bill? $"))
input_tip_percentage = float(input("How much tip would you like to give? "))
num_of_people = float(input("How many people to split the bill? "))

adjusted_tip_percentage = input_tip_percentage / 100
tip_amount = adjusted_tip_percentage * total_bill
payment = (total_bill + tip_amount) / num_of_people
#Rounding to 2 decimal places
total_payment = (round(payment, 2))
#Formatting to two decimal places regardless of input
total_payment_pretty = "{:.2f}".format(total_payment)
print(f"Each person should pay $" + total_payment_pretty)