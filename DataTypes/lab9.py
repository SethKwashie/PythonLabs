numbers = []

while True:
    number = input("Enter numbers between 1 and  >>> ")
    if int(number) in range (1,9):
        numbers.append(number)
        if len(numbers) == 10:
            break
    

print(numbers)
x = numbers.count(6)
print(x)