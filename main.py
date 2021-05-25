def menu():
     
    # Asking the user to choose one of the following options.
    print("\nPlease choose an option from the menu:\n")
    # Menu of options
    print("1-Load Data\n2-Process Data\n3-Visualize Data\n4-Save Data\n5-Exit")

    option = int(input())
    #if..else if...else if...else structure to display the menu of options
    if option == 1:
        print("Load Data")
    elif option == 2:
        print("Process Data")
    elif option == 3:
        print("Visualize Data")
    elif option == 4:
        print("Save Data")
    elif option == 5:
        print("Exit")
    else:
        print("Invalid number for any other option!")

menu()