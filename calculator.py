"""
Simple Calculator
A basic calculator with arithmetic operations (+, -, *, /)
"""


class Calculator:
    """A simple calculator class for basic arithmetic operations"""
    
    def __init__(self):
        """Initialize the calculator"""
        self.result = 0
    
    def add(self, num1, num2):
        """Add two numbers"""
        self.result = num1 + num2
        return self.result
    
    def subtract(self, num1, num2):
        """Subtract two numbers"""
        self.result = num1 - num2
        return self.result
    
    def multiply(self, num1, num2):
        """Multiply two numbers"""
        self.result = num1 * num2
        return self.result
    
    def divide(self, num1, num2):
        """Divide two numbers"""
        if num2 == 0:
            return "❌ Error: Cannot divide by zero!"
        self.result = num1 / num2
        return self.result
    
    def modulo(self, num1, num2):
        """Get remainder of division"""
        if num2 == 0:
            return "❌ Error: Cannot divide by zero!"
        self.result = num1 % num2
        return self.result
    
    def power(self, num1, num2):
        """Raise num1 to the power of num2"""
        self.result = num1 ** num2
        return self.result


def display_menu():
    """Display the calculator menu"""
    print("\n" + "="*60)
    print("🧮 SIMPLE CALCULATOR 🧮")
    print("="*60)
    print("\nAvailable Operations:")
    print("1️⃣  Addition (+)")
    print("2️⃣  Subtraction (-)")
    print("3️⃣  Multiplication (*)")
    print("4️⃣  Division (/)")
    print("5️⃣  Modulo (remainder)")
    print("6️⃣  Power (exponent)")
    print("7️⃣  Exit")
    print("="*60)


def get_numbers():
    """Get two numbers from user"""
    try:
        num1 = float(input("\nEnter first number: "))
        num2 = float(input("Enter second number: "))
        return num1, num2
    except ValueError:
        print("❌ Invalid input! Please enter valid numbers.")
        return None, None


def main():
    """Main calculator loop"""
    calculator = Calculator()
    
    print("\n" + "="*60)
    print("Welcome to Simple Calculator!")
    print("="*60)
    
    while True:
        display_menu()
        choice = input("\nChoose an operation (1-7): ").strip()
        
        if choice == '7':
            print("\n👋 Thank you for using the calculator! Goodbye!\n")
            break
        
        if choice not in ['1', '2', '3', '4', '5', '6']:
            print("\n❌ Invalid choice! Please select 1-7.\n")
            continue
        
        # Get numbers from user
        num1, num2 = get_numbers()
        if num1 is None:
            continue
        
        # Perform calculation based on choice
        result = None
        
        if choice == '1':
            result = calculator.add(num1, num2)
            operation = "+"
        
        elif choice == '2':
            result = calculator.subtract(num1, num2)
            operation = "-"
        
        elif choice == '3':
            result = calculator.multiply(num1, num2)
            operation = "*"
        
        elif choice == '4':
            result = calculator.divide(num1, num2)
            operation = "/"
        
        elif choice == '5':
            result = calculator.modulo(num1, num2)
            operation = "%"
        
        elif choice == '6':
            result = calculator.power(num1, num2)
            operation = "^"
        
        # Display result
        print("\n" + "-"*60)
        if isinstance(result, str):  # Error message
            print(result)
        else:
            print(f"✅ Result: {num1} {operation} {num2} = {result}")
        print("-"*60)


if __name__ == "__main__":
    main()
