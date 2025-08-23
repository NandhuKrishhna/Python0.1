try:
    first_number = float(input("Enter first number: "))  # Convert to float for broader compatibility
    second_number = float(input("Enter second number: "))

    if first_number > second_number:
        print("True")
    else:  # Use else instead of elif since no additional condition is needed
        print("False")
except ValueError:
    print("Error: Please enter valid numbers!")