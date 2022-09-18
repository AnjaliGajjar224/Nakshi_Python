print("Welcome to the HOTEL!!")
print("1---> South Indian")
print("2---> Italian")
print("3---> Mexican")

choice = int(input("Enter your Choice: "))

if choice == 1:
    print("You have selected South Indian")

    print("----------------------------")

    print("1 ---> Dosa")
    print("2 ---> Idli,Menduvada")
    print("3 ---> Uttapam")

    subchoice = int(input("Enter your choice: "))

    if subchoice == 1:
        print("You have selected Dosa")
    elif subchoice == 2:
        print("You have selected Idli, Menduvada")
    elif subchoice == 3:
        print("You have selected Uttapam")
    else:
        print("Invalid Choice")

elif choice == 2:
    print("You have selected Italian")
elif choice == 3:
    print("You have selected Mexican")
else:
    print("Invalid Choice")