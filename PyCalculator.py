print("Welcome to my Python Calculator!\n")

num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))

print("\nPlease select which operation you would like to use from the list below by selecting a number:\n")
print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n")

opnum = int(input("Select your operation: "))
answer = None


if opnum == 1:
    answer = num1 + num2

if opnum == 2:
    answer = num1 - num2

if opnum == 3:
    answer = num1 * num2

if opnum == 4:
    answer = num1 / num2

print("\nYour final answer is: " + str(answer))




