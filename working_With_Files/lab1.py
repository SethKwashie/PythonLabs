
f = open('test.txt','a')
while True:
    value = input("User input >>>")
    if value != "end":
        f.write(f'{value}\n')
    else:
        break


f.close()