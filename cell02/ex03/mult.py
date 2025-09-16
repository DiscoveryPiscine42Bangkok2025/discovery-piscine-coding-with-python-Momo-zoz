x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

result = x * y
print(f"{x} x {y} = {result}")

if result < 0:
    print("The result is negative.")
elif result == 0:
    print("The result is positive and negative.")
else:
    print("The result is positive.")