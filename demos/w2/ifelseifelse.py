print("What is your name?")
n = input()
#print("Do you have a dog?(Types True or False)")
#dog =input()
#bool is boolean datatype- only stores True/Flase

if len(n) >= 9: #allow lenghth of exactly 9 or greater
  print("You have a very loooooong name!")
  print("Your name contains {} letters".format(len(n)))
elif len(n) >6:
  print("Your name is a bit long. Consider you nickname")
elif len(n) <3:
  print("Your name is very short")
else:
  print("Your name is quite okay")
print("This is the END of the program!!")