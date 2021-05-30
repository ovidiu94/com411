
# print("Please enter the first whole number.")
# num1 = int(input())
# print("Please enter the second whole number.")
# num2 = int(input())
# print("Please enter the third whole number.")
# num3 = int(input())


# even_count, odd_count = 0, 0

# for num in (num1,num2,num3):

#     if num % 2:
#        even_count += 1
#     else:
#        odd_count += 1    
# print("There were {} even and {} odd numbers.".format(even_count,odd_count))

# Ask user for numbers 
print("Please enter the first whole number?")
first_number = int(input())

print("Please enter the second whole number?")
second_number = int(input())

print("Please enter the third whole number?")
third_number = int(input()) 

even_numbers = 0
odd_numbers = 0 

# Determine which numbers are even and which are odd
if (first_number % 2 == 0):
    even_numbers = even_numbers + 1
else:
    odd_numbers = odd_numbers + 1

if (second_number % 2 == 0):
    even_numbers = even_numbers + 1
else:
    odd_numbers = odd_numbers + 1

if (third_number % 2 == 0):
    even_numbers = even_numbers + 1
else:
    odd_numbers = odd_numbers + 1

# Display result
print("There were {} even and {} odd numbers.".format(even_numbers, odd_numbers))