import random

def get_valid_integer(prompt):
    """Helper function to get valid integer input from user."""
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid integer.")

def generate_random_numbers():
    """Main function to generate random numbers based on user input."""
    print("Welcome to the Random Number Generator!")
    print("========================================\n")
    
    # Get number of random numbers needed
    while True:
        count = get_valid_integer("How many random numbers do you want to generate? ")
        if count > 0:
            break
        print("Please enter a number greater than 0.")
    
    # Get minimum range
    min_value = get_valid_integer("Enter the minimum value for the range: ")
    
    # Get maximum range with validation
    while True:
        max_value = get_valid_integer("Enter the maximum value for the range: ")
        if max_value >= min_value:
            break
        print(f"Maximum value must be greater than or equal to minimum value ({min_value}).")
    
    # Generate random numbers
    random_numbers = [random.randint(min_value, max_value) for _ in range(count)]
    
    # Display results
    print("\nGenerated Random Numbers:")
    print("------------------------")
    for i, num in enumerate(random_numbers, 1):
        print(f"{i}: {num}")
    print(f"\nGenerated {count} numbers between {min_value} and {max_value}")

def main():
    """Main program loop with option to generate more numbers."""
    while True:
        generate_random_numbers()
        
        # Ask if user wants to generate more numbers
        while True:
            again = input("\nWould you like to generate more numbers? (yes/no): ").lower().strip()
            if again in ['yes', 'no']:
                break
            print("Please enter 'yes' or 'no'.")
        
        if again == 'no':
            print("Thank you for using the Random Number Generator!")
            break

if __name__ == "__main__":
    main()