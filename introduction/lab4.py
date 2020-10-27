import random


value = input("Enter a random number >>> ")
rand_value = random.randint(0,9)
while int(value) != rand_value:
     value = input("Enter a random number >>> ")
     if int(value) == rand_value:
         print("Viola!!! You have won")
         break;


