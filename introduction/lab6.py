age  =  int(input("Enter your age >>> "))
total = 0
start = 1

while start <= age:
        total += start
        start +=1

month = total * 12
days = total * 365
hours = total * 8760

print(f"{total} years ----> {month} months ----> {days} days ----> {hours} hours")
