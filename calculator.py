# calculator.py

def calculate(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error! Division by zero."
    else:
        return "Invalid operator."

def main():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            operator = input("Enter operator (+, -, *, /): ")
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue
        result = calculate(num1, operator, num2)
        print("Result:", result)

        again = input("Do you want to calculate again? (yes/no): ").strip().lower()
        if again != 'yes':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
