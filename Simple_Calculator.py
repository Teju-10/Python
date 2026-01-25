num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))
operand = input("choose(+, -, *, /, //, %): ")

if operand == '+':
    print("Sum:", num1 + num2)

elif operand == '-':
    print("Subtraction:", num1 - num2)

elif operand == '*':
    print("Multiplication:", num1 * num2)

elif operand in ('/', '//', '%'):
    if num2 == 0:
        print("Error: Division by zero")
    else:
        ops = {
            '/': num1 / num2,
            '//': num1 // num2,
            '%': num1 % num2
        }
        print("Result:", ops[operand])

else:
    print("Invalid operator")
