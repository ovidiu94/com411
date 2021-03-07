
print("Please enter the first whole number.")
num1 = int(input())
print("Please enter the second whole number.")
num2 = int(input())
print("Please enter the third whole number.")
num3 = int(input())


even_count, odd_count = 0, 0

for num in (num1,num2,num3):

    if num % 2:
       even_count += 1
    else:
       odd_count += 1    
print("There were {} even and {} odd numbers.".format(even_count,odd_count))