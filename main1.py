import random

def get_valid_integer(prompt):
    """Helper function to get valid integer input from user."""
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid integer.")

def get_yes_no_choice(prompt):
    """Helper function to get yes/no input from user."""
    while True:
        choice = input(prompt).lower().strip()
        if choice in ['yes', 'no', 'y', 'n']:
            return choice.startswith('y')
        print("Please enter 'yes' or 'no' (or 'y'/'n').")

def generate_and_process_numbers():
    """Generate random numbers and handle shuffling option."""
    print("\n=== Random Number Generator ===")
    
    # Get number of random numbers needed
    while True:
        count = get_valid_integer("How many numbers do you want to generate? ")
        if count > 0:
            break
        print("Please enter a number greater than 0.")
    
    # Get range values
    min_value = get_valid_integer("Enter the minimum value: ")
    while True:
        max_value = get_valid_integer("Enter the maximum value: ")
        if max_value >= min_value:
            break
        print(f"Maximum must be >= minimum ({min_value}).")
    
    # Generate initial random numbers
    numbers = [random.randint(min_value, max_value) for _ in range(count)]
    
    # Show original numbers
    print("\nOriginal numbers:")
    for i, num in enumerate(numbers, 1):
        print(f"Number {i}: {num}")
    
    # Ask about shuffling
    if get_yes_no_choice("\nWould you like to shuffle these numbers? (yes/no): "):
        random.shuffle(numbers)
        print("\nShuffled numbers:")
        for i, num in enumerate(numbers, 1):
            print(f"Number {i}: {num}")
    else:
        print("\nKeeping original order.")

    print(f"\nGenerated {count} numbers between {min_value} and {max_value}")

def main():
    """Main CLI program loop."""
    print("Welcome to the Random Number Generator CLI!")
    print("===========================================")
    
    while True:
        generate_and_process_numbers()
        
        # Ask to continue
        if not get_yes_no_choice("\nGenerate more numbers? (yes/no): "):
            print("\nThank you for using the Random Number Generator CLI!")
            break

if __name__ == "__main__":
    main()