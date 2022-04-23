from os import system
import sys

names = {} # dictionary to store the names in

# the main menu of the program, tells user to make a choice
mainMenu = """Name Organizer
=====================

Type the number of an option, then hit ENTER

1 - Add a name
2 - Change a name
3 - Delete a name
4 - List all names
5 - Delete all names
6 - Quit

=====================
"""

# These functions get called in main() when the user makes a choice
def addName():
    system("clear")
    newName = input("Enter new name: ")
    if newName in names:
        print("Name already exists!")
    else:
        print(f"Adding name {newName}...")
        names[newName] = newName
        print("Done!")

def changeName():
    system("clear")
    oldName = input("Enter old name you wish to change: ")
    if oldName not in names:
        print("Old name does not exist!")
        return
    else:
        newName = input("Enter new name: ")

    if newName == oldName:
        print("New name already exists!")
        return
    elif newName in names:
        print("Name already exists!")
    else:
        print("Changing name...")
        del names[oldName]
        names[newName] = newName
        print("Done!")
    
def deleteName():
    system("clear")
    oldName = input("Enter name you wish to delete: ")
    if oldName not in names:
        print("Name does not exist!")
    else:
        print("Deleting name...")
        del names[oldName]
        print("Done!")
    

def listNames(): # maybe find a way to sort names more elegantly?
    system("clear")
    sortedNames = sorted(names, key=str.lower)
    for i in sortedNames:
        print(i)

def deleteAllNames():
    system("clear")
    userIsSure = input("Are you sure you want to DELETE ALL NAMES? Y or N: ")
    if userIsSure == "Y" or userIsSure == "y":
        print("Deleting all names...")
        for name in list(names):
            del names[name]
        print("Done!")
    elif userIsSure == "N" or userIsSure == "n":
        print("Action cancelled!")
    else:
        print("Not a valid input!")

def userExit():
    system("clear")
    userExitChoice = input("Are you sure you want to exit? Y or N: ")
    if userExitChoice == "Y" or userExitChoice == "y":
        sys.exit(0)
    elif userExitChoice == "N" or userExitChoice == "n":
        print("Action cancelled!")
    else:
        print("Not a valid input!")

# debug function, quick way to add names to the dictionary
def debug():
    system("clear")
    names.update({'Tim': 'Tim', 'John': 'John', 'Katie': 'Katie', 'Maria': 'Maria', 'Jessie': 'Jessie'})
    print("Names added")

# Main method, gets called at the start of the program
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