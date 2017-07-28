def main():
    filename = input("Welcom, please enter file name:\t")
    menu()
    choice= int(input("Enter menu choice:\t"))

    while choice != 5:
        #get file choice from user
        if choice == 1:
            #create file
            create(filename)
        elif choice == 2:
            #read file
            read(filename)
        elif choice == 3:
            #append file
            append(filename)
        elif choice == 4:
            #get total
            get_total(filename)

        choice = int(input("Enter menu choice:\t"))

    print("\nApplication Complete")

def menu():

    #user chooses a number from list
    print("Choose a number to continue:\t\n\
    Select 1 to create a file\n\
    Select 2 to read a file\n\
    Select 3 to append to a file\n\
    Select 4 to calculate the total of a file\n\
    Select 5 to exit programme")


#call main
main()
