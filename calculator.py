"""
enter numbers into the caclulator with the format 'num1,num2,operation' as detailed in the first prompt.
This script uses functions for each operation, with arguments being the input numbers.
"""

# A funtion that starts the calculator running at the start of the script.
def run():
    # The initial prompt, which is not repeated if it has already run once.
    # The iterations variable is used for this purpose.
    intake = input("Input 2 numbers and an operation. Ex: '38,17,*'. Operations can be */+- or % for remainder. Enter here: ")
    iterations = 0
    
    # Runs the calculator until the user types 'exit' which closes the program.

    while True:
        if intake == 'exit':
            break
            
        iterations += 1

        if iterations > 1:
            intake = input("Enter here: ")
        
        try:
            # Handle input parsing
            parts = intake.split(',')
            if len(parts) != 3 and intake != 'exit':
                raise ValueError("Input must have exactly 3 parts separated by commas")
   
            num1 = int(parts[0].strip())
            num2 = int(parts[1].strip())
            operation = parts[2].strip()
            
            # Perform operations
            if operation == '*':
                multiply(num1, num2)
            elif operation == '/':
                divide(num1, num2)
            elif operation == '+':
                add(num1, num2)
            elif operation == '-':
                subtract(num1, num2)
            elif operation == '%':
                remainder(num1, num2)
            else:
                print(f"Error: '{operation}' is not a valid operation. Use */+- or %")
                
        except ValueError as e:
            if "invalid literal for int()" in str(e):
                print("Error: Please enter valid numbers (integers only)")
            else:
                print(f"Error: {e}")
        except ZeroDivisionError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
    
    print("Thank you for using our calculator!")


def multiply(temp1, temp2):
    print(temp1 * temp2)


def divide(temp1, temp2):
    if temp2 == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    print(temp1 / temp2)


def add(temp1, temp2):
    print(temp1 + temp2)


def subtract(temp1, temp2):
    print(temp1 - temp2)


def remainder(temp1, temp2):
    if temp2 == 0:
        raise ZeroDivisionError("Cannot calculate remainder when dividing by zero")
    print(temp1 % temp2)


if __name__ == "__main__":
    run()
