#asking the user to enter their name
print("What is your name?")
name = input()

#asking the user to enter the age
print("How old are you(in years)?")
age = int(input())

print("How tall are you(in meters)?")
height = float(input())

print("How much do you weigh(in kilograms)?")
weigh = float(input())
#Note that the bmi can be calculated by dividing the weight (kg) by the height squared.  To work out the square of the height you can multiply the height by itself or use the power operator (**) e.g. height ** 2.
print("{} you are {} years old and you bmi is {:.2f}".format(name, age, weigh/height**2))