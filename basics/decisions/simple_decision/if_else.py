#ask the user to enter an activity
print("\nPlease enter the activity to be performed.")

activity = input()
#check if the activity enter by user is calculate  
if (activity == "calculate"):
  print("Performing calculations...")
#else will be executed if the user enter other activities  
else:
  print("Performing activity...")

print("Activity Completed!")#Dispay a message to the user