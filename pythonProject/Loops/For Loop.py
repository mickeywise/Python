fruits = ['Mango', 'Grapes', 'Apple']

for fruit in fruits:
    print("Current fruits:", fruit)

print("Goodbye!")


num = int(input("Enter number: "))
factorial = 1
if num < 0:
    print("Number must be positive")
elif num == 0:
    print("Factorial = 1")
else:
    for i in range(1, num + 1):
        factorial = factorial*i
print(factorial)