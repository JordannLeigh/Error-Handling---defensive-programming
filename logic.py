while True:
    try:
        number = int(input("Enter a number: "))  # Convert input to integer
        if number % 2 == 0:
            print("The number is even.")
        else:
            print("The number is odd.")
        break
    except ValueError:
        print("Please enter a valid number.")
