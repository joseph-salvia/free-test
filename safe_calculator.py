# I made the user choice which is operation to be a text(str)
#So there is no need to catch any error there
#An else statement would just have solved that

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("\nThat's not a valid number. Try again.")

def calc():
    num1 = get_number("\nEnter the first number:\t")
    num2 = get_number("\nEnter the second number:\t")
    return num1 , num2


    
try:    
    while True:
        operation = input("""\n=== SAFE CALCULATOR ===
1. Add
2. Subtract
3. Multiply
4. Divide
5. Quit:\t""")

        if operation == "1":
            num1, num2 = calc()
            add_result = num1 + num2
            print(f"\nThe Addition result is {add_result}")
        elif operation == "2":
            num1, num2 = calc()
            subtract_result =  num1 - num2
            print(f"\nThe Subtraction result is {subtract_result}")
        elif operation == "3":
            num1 , num2 = calc()
            multiply_result  = num1 * num2
            print(f"\nThe Multiplication result is {multiply_result}")
        elif operation == "4":
            try:
                num1, num2 = calc()
                divide_result = num1 / num2
                print(f"\nThe Division result is {divide_result}")
            except ZeroDivisionError:
                print("\nError: Cannot divide by zero!")    
        elif operation == "5":
            print("\nCalculator closed")
            break
        else:
            print("\nInvalid choice")
            print("Enter either 1, 2, 3, 4, 5.")

except KeyboardInterrupt:
    print("\nGoodbye!")

