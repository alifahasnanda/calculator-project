"""
Simple Calculator
"""
print("Calculator is running!")

#addition
def add(a, b):
    return a + b

#substraction
def subtract(a, b):
    return a - b

#Multiplication
def multiply(a, b):
    return a * b

#Division
def divide(a, b):
    if b == 0:
        print("Error: Cannot divide by zero!")
        return None
    return a / b

# Function to show menu
def show_menu():
    print("\n=== Calculator ===")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    print("==================")

# Function to request numeric input from user
def get_number(prompt):
    while True:
        try:
            number = float(input(prompt))
            return number
        except:
            print("Invalid input! Please enter a number.")

# Main Program
def main():
    print("Welcome to Calculator!")
    
    while True:
        show_menu()
        choice = input("Choose (1-5): ")
        
        # if choose exit
        if choice == "5":
            print("Goodbye!")
            break
        
        # Kalau pilihan tidak valid
        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice!")
            continue
        
        # Ask user for 2 numbers
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")
        
        # Calculate based on selection
        if choice == "1":
            result = add(num1, num2)
            print(f"Result: {num1} + {num2} = {result}")
        
        elif choice == "2":
            result = subtract(num1, num2)
            print(f"Result: {num1} - {num2} = {result}")
        
        elif choice == "3":
            result = multiply(num1, num2)
            print(f"Result: {num1} * {num2} = {result}")
        
        elif choice == "4":
            result = divide(num1, num2)
            if result is not None:
                print(f"Result: {num1} / {num2} = {result}")

# Start Program
if __name__ == "__main__":
    main()