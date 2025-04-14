import random
import argparse

def generate_single_digit_addition_text():
    num1 = random.randint(1, 9)
    num2 = random.randint(1, 9)
    return f"Operator 1 : {num1} +  Operator 2 : {num2}"

def generate_single_digit_subtraction_text():
    num1 = random.randint(1, 9)
    num2 = random.randint(1, num1) # Ensure non-negative result
    return f"Operator 1 : {num1} -  Operator 2 : {num2}"

def generate_single_digit_multiplication_text():
    num1 = random.randint(1, 9)
    num2 = random.randint(1, 9)
    return f"Operator 1 : {num1} x  Operator 2 : {num2}"

def generate_single_digit_division_text():
    num2 = random.randint(1, 9)
    result = random.randint(1, 9)
    num1 = num2 * result # Ensure exact division within single digits
    return f"Operator 1 : {num1} /  Operator 2 : {num2}"

def generate_mixed_single_digit_questions_text(num_questions):
    questions = []
    operations = [
        generate_single_digit_addition_text,
        generate_single_digit_subtraction_text,
        generate_single_digit_multiplication_text,
        generate_single_digit_division_text,
    ]
    for _ in range(num_questions):
        operation = random.choice(operations)
        questions.append(operation())
    return "\n".join(questions)

def generate_two_digit_addition_text():
    if random.choice([True, False]):
        num1 = random.randint(10, 99)
        num2 = random.randint(1, 9)
        return f"Operator 1 : {num1} +  Operator 2 : {num2}"
    else:
        num1 = random.randint(10, 99)
        num2 = random.randint(10, 99)
        return f"Operator 1 : {num1} +  Operator 2 : {num2}"

def generate_two_digit_subtraction_text():
    choices = [1, 2, 3, 4]
    choice = random.choice(choices)
    if choice == 1: # Two Digits - Single Digit (no borrowing)
        num2 = random.randint(1, 9)
        num1 = random.randint(num2, 99)
        return f"Operator 1 : {num1} -  Operator 2 : {num2}"
    elif choice == 2: # Two Digits - Single Digit (with borrowing)
        num2 = random.randint(1, 9)
        num1 = random.randint(10 + num2, 99) # Ensure borrowing is possible
        return f"Operator 1 : {num1} -  Operator 2 : {num2}"
    elif choice == 3: # Two Digits - Two Digits (no borrowing)
        num2 = random.randint(10, 99)
        num1 = random.randint(num2, 99)
        return f"Operator 1 : {num1} -  Operator 2 : {num2}"
    else: # Two Digits - Two Digits (with borrowing)
        num2 = random.randint(10, 99)
        num1 = random.randint(num2 + 1, 99) # Ensure borrowing is possible
        return f"Operator 1 : {num1} -  Operator 2 : {num2}"

def generate_two_digit_multiplication_text():
    num1 = random.randint(10, 99)
    num2 = random.randint(1, 9)
    return f"Operator 1 : {num1} x  Operator 2 : {num2}"

def generate_two_digit_division_text():
    num2 = random.randint(1, 9)
    result = random.randint(2, 10) # Keep results reasonable for 2 digits
    num1 = num2 * result
    if 10 <= num1 <= 99:
        return f"Operator 1 : {num1} /  Operator 2 : {num2}"
    else:
        return generate_two_digit_division_text() # Try again if out of range

def generate_mixed_two_digit_questions_text(num_questions):
    questions = []
    operations = [
        generate_two_digit_addition_text,
        generate_two_digit_subtraction_text,
        generate_two_digit_multiplication_text,
        generate_two_digit_division_text,
    ]
    for _ in range(num_questions):
        operation = random.choice(operations)
        questions.append(operation())
    return "\n".join(questions)

def generate_three_digit_addition_text():
    if random.choice([True, False]):
        num1 = random.randint(100, 999)
        num2 = random.randint(10, 99)
        return f"Operator 1 : {num1} +  Operator 2 : {num2}"
    else:
        num1 = random.randint(100, 999)
        num2 = random.randint(100, 999)
        return f"Operator 1 : {num1} +  Operator 2 : {num2}"

def generate_three_digit_subtraction_text():
    if random.choice([True, False]): # Three Digits - Two Digits
        num2 = random.randint(10, 99)
        num1 = random.randint(num2, 999)
        return f"Operator 1 : {num1} -  Operator 2 : {num2}"
    else: # Three Digits - Three Digits
        num2 = random.randint(100, 999)
        num1 = random.randint(num2, 999)
        return f"Operator 1 : {num1} -  Operator 2 : {num2}"

def generate_three_digit_multiplication_text():
    num1 = random.randint(100, 999)
    num2 = random.randint(1, 9)
    return f"Operator 1 : {num1} x  Operator 2 : {num2}"

def generate_three_digit_division_text():
    num2 = random.randint(1, 9)
    result = random.randint(12, 111) # Keep results in a reasonable 2-3 digit range
    num1 = num2 * result
    if 100 <= num1 <= 999:
        return f"Operator 1 : {num1} /  Operator 2 : {num2}"
    else:
        return generate_three_digit_division_text() # Try again if out of range

def generate_mixed_three_digit_questions_text(num_questions):
    questions = []
    operations = [
        generate_three_digit_addition_text,
        generate_three_digit_subtraction_text,
        generate_three_digit_multiplication_text,
        generate_three_digit_division_text,
    ]
    for _ in range(num_questions):
        operation = random.choice(operations)
        questions.append(operation())
    return "\n".join(questions)

def main():
    parser = argparse.ArgumentParser(description="Generate mixed math questions (single, two, and three digits in one file).")
    parser.add_argument("-n", "--num_questions", type=int, default=30, help="Number of questions to generate per section.")
    parser.add_argument("-p", "--num_pages", type=int, default=1, help="Number of pages for each section.")
    parser.add_argument("-o", "--output", type=str, default="mixed_math_all.txt", help="Output file to save the questions.")

    args = parser.parse_args()

    all_questions_text = []

    # Generate Single Digit Questions
    all_questions_text.append("--- Single Digit Questions ---")
    for page in range(args.num_pages):
        page_questions = generate_mixed_single_digit_questions_text(args.num_questions)
        all_questions_text.append(f"--- Page {page + 1} ---")
        all_questions_text.append(page_questions)
        all_questions_text.append("")

    # Generate Two Digit Questions
    all_questions_text.append("\n--- Two Digit Questions ---")
    for page in range(args.num_pages):
        page_questions = generate_mixed_two_digit_questions_text(args.num_questions)
        all_questions_text.append(f"--- Page {page + 1} ---")
        all_questions_text.append(page_questions)
        all_questions_text.append("")

    # Generate Three Digit Questions
    all_questions_text.append("\n--- Three Digit Questions ---")
    for page in range(args.num_pages):
        page_questions = generate_mixed_three_digit_questions_text(args.num_questions)
        all_questions_text.append(f"--- Page {page + 1} ---")
        all_questions_text.append(page_questions)
        all_questions_text.append("")

    output_content = "\n".join(all_questions_text)

    with open(args.output, "w") as f:
        f.write(output_content)
    print(f"Generated single, two, and three digit questions saved to {args.output}")

if __name__ == "__main__":
    main()