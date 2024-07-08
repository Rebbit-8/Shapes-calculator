print("Welcome to the rectangle calculator")
try:
    name = str(input("Enter your name: "))
    print("Hello " + name + "!")
except NameError:
    print("Sorry, that name is invalid!")
    print("Try again!")
    name = str(input("Enter your name: "))
    print("Hello " + name + "!")

try:
    length = int(input("Enter length: "))
except ValueError:
    print("Sorry, that length is invalid!")
    print("Try again!")
    length = int(input("Enter length: "))

try:
    height = int(input("Enter height: "))
except ValueError:
    print("Sorry, that height is invalid!")
    print("Try again!")
    height = int(input("Enter height: "))

print("Enter number 1 to calculate perimeter, number 2 to calculate area, number 3 to calculate volume")
perimeter = int(input("Enter perimeter: "))

if perimeter == 1:
    print("You are calculating the environment")
    Environment = (length + height) * 2
    print("Your shape environment:", Environment)
elif perimeter == 2:
    print("You are calculating the area")
    Area = (length * height)
    print("The area of your shape: ", Area)
elif perimeter == 3:
    print("You are calculating the volume")
    try:
        Height = int(input("Enter height: "))
    except ValueError:
        print("Sorry, that height is invalid!")
        print("Try again!")
        Height = int(input("Enter height: "))
    volume = (length * Height * height)
    print("The area of your height: ", volume)

print("Thank you!")
