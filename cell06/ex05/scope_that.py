#!/usr/bin/env python3

# Method that adds 1 to the parameter passed
def add_one(x):
    x += 1
    return x

# Main program body
if __name__ == "__main__":
    # Initialize a variable
    num = 5
    print("Before calling add_one:", num)

    # Call the method add_one
    num = add_one(num)

    # Display the value of the variable after calling the method
    print("After calling add_one:", num)
