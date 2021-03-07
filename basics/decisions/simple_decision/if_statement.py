print("Welcome to the Program!\n")

print("Enter the first number")#ask the user to enter first number
first_number= input()

print("Enter the second number")#ask the user to enter second number
second_number=input()

#check whether the first number is bigger than second number.
#Assume first_number and second_number are existing variables.
if (first_number > second_number):
  print("First number is bigger!")
#check whether the second_number is bigger than first_number.  
elif(second_number > first_number):
  print("Second number is bigger!")
else:
  print("Both numbers are equal!")  
print("Done!")#Dispay a message 

