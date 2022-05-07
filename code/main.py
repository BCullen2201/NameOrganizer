from os import system
import sys

names = [] # list to store the names in

# the main menu of the program, tells user to make a choice
mainMenu = """                   Name Organizer
######################################################
#                                                    #
#    Type the number of an option, then hit ENTER    #
#                                                    #
#    1 - Add a name                                  #
#    2 - Change a name                               #
#    3 - Delete a name                               #
#    4 - List all names                              #
#    5 - Delete all names                            #
#    6 - Quit                                        #
#                                                    #
######################################################
"""

# These functions get called in main() when the user makes a choice

### Asks user for a name, and stores it in list 'names' ###
def addName():
    system("clear")
    newName = input("Enter new name: ")
    if newName in names:
        print("Name already exists!")
        return
    else:
        print(f"Adding name {newName}...")
        names.append(newName)
        print("Done!")

### User selects a name to change, and what to change it to ###
def changeName():
    system("clear")
    if len(names) == 0:
        print("There are no names to change!")
        return
    
    oldName = input("Enter old name you wish to change: ")
    if oldName not in names:
        print("Old name does not exist!")
        return
    else:
        newName = input("Enter new name: ")
    
    if newName in names:
        print("Name already exists!")
        return
    else:
        print("Changing name...")
        names.remove(oldName)
        names.append(newName)
        print("Done!")
    
### User selects a name to delete, chosen name gets removed from list 'names' ###
def deleteName():
    system("clear")
    oldName = input("Enter name you wish to delete: ")
    if oldName not in names:
        print("Name does not exist!")
        return
    else:
        print("Deleting name...")
        names.remove(oldName)
        print("Done!")
    

### Lists all items in list 'names' in alphabetical order ###
def listNames():
    system("clear")
    names.sort()
    
    for i in names:
        print(i)

### Delets all items from list 'names', if user is sure they want to ###
def deleteAllNames():
    system("clear")
    userIsSure = input("Are you sure you want to DELETE ALL NAMES? Y or N: ")
    if userIsSure == "Y" or userIsSure == "y":
        print("Deleting all names...")
        names.clear()
        print("Done!")
    elif userIsSure == "N" or userIsSure == "n":
        print("Action cancelled!")
        return
    else:
        print("Not a valid input!")
        return

### Exits from program if user is sure they want to ###
def userExit():
    system("clear")
    userExitChoice = input("Are you sure you want to exit? Y or N: ")
    if userExitChoice == "Y" or userExitChoice == "y":
        sys.exit(0)
    elif userExitChoice == "N" or userExitChoice == "n":
        print("Action cancelled!")
        return
    else:
        print("Not a valid input!")
        return

### Quick way to add items to list 'names' ###
def debug():
    system("clear")
    
    names.append("Tim")
    names.append("John")
    names.append("Katie")
    names.append("Maria")
    names.append("Jessie")

    print("Names added")

### Main method, gets called at the start of the program ###
def main():
    print(mainMenu)
    choice = input().strip()
    if choice == "1":
        addName()
    elif choice == "2":
        changeName()
    elif choice == "3":
        deleteName()
    elif choice == "4":
        listNames()
    elif choice == "5":
        deleteAllNames()
    elif choice == "6":
        userExit()
    elif choice == "7":
        debug()
    else:
        print("Not a valid input")
    

# infinite loop keeps program open
while True:
    system("clear") # clears the screen before calling main() so the screen isnt cluttered
    main()
    input("\nPress enter to continue: ") # global 'reset', so i dont have to do it at the end of each function