#conditional statements:

#if-else:
a=input("Enter the value of a: ")
b=input("Enter the value of b: ")
if(a > b):
    print("Hello, a is greater then b.")
else:
    print("Hi, b is greater then the a.")

#Another Example:
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible for voting and Driving.")
else:
    print("You are not eligible for voting and Driving.")

#Another Example:
num = int(input("Enter the value of num: "))
if(num%2==0):
    print("The number is even.")
else:
    print("The number is odd.")

#Another Example:
num = int(input("Enter the value of num: "))
if(num%3==0):
    print("The number is divisible by 3.")
else:
    print("The number is not divisible by 3.")

#Another Example:
num = int(input("Enter the value of num: "))
if(num%5==0):
    print("The number is divisible by 5.")
else:
    print("The number is not divisible by 5.")

#Another Example:
num = int(input("Enter the value of num: "))
if(num%7==0):
    print("The number is divisible by 7.")
else:
    print("The number is not divisible by 7.")

#if-elif-else:

light = input("Enter the value of light: ")
if(light == "red"):
    print("Stop")
elif(light == "yellow"):
    print("Ready")
elif(light == "green"):
    print("Go")
else:
    print("Invalid light")


#Another Example:

marks = int(input("Enter the value of marks: "))
if marks>=90:
    print("Grade A")
elif marks>=80:
    print("Grade B")
elif marks>=70:
    print("Grade C")
elif marks>=60:
    print("Grade D")
else:
    print("Grade F")

#Nested if-else:

# Example 1: Check if a number is positive, negative, or zero
num = int(input("Enter a number: "))
if num >= 0:
    if num == 0:
        print("The number is Zero")
    else:
        print("The number is Positive")
else:
    print("The number is Negative")

# Example 2: Check eligibility for a loan based on age and income
age = int(input("Enter your age: "))
if age >= 18:
    income = int(input("Enter your monthly income: "))
    if income >= 20000:
        print("You are eligible for the loan.")
    else:
        print("You are not eligible for the loan due to low income.")
else:
    print("You are not eligible for the loan due to age.")
