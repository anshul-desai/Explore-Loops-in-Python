# Task 1
start = int(input("Give me a starting number: "))
while start != 0:
    print(start, "")
    start = start - 1
print("Blast off!")


# Task 2
num = int(input("Enter a number: "))
for i in range(10):
    print(str(num) + " x " + str((i+1)) + " = " + str(num*(i+1)))

# Task 3
fact = input("Enter a number: ")
total = 1
for i in range(2, int(fact)+1):
    total = total * i
print("The factorial of " + str(fact) + " is", total)
