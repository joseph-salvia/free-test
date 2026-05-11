#I want to display casing

user_name = input("Hello, what may we address you as?\n\n")

print("\nThank you for coming in " + user_name + ", Our Mocha is priced at $13.24\n")
order_quantity = input("How many Mocha should we get you\n\n")

mocha = 13.24

print("\nAlright " + user_name + ", your order of " + str(order_quantity) + " Mocha will be ready soon\n")
tip_amount = input("And how much tip will you like to give?\n\n")

total = mocha * float(order_quantity) + float(tip_amount)

print("Alright " + user_name + ", Your total will be $" + str(total) + ".\n" + "Kindly Proceed to the counter to pay and you'll get your order shortly" )

print("\nProgram run has ended.")
