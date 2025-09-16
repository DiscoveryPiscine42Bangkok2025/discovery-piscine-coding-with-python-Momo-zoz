x = int(input("Enter a number less than 25"))

if x > 25 :
    print("Error")
else:
    while x <= 25 and x >= 0:
        print("Inside the loop, my variable is " + str(x))
        x += 1