from os import system
import sys

mainMenu = """                   Name Organizer
######################################################
##                                                  ##
##   Type the number of an option, then hit ENTER   ##
##                                                  ##
##   1 - Add a name                                 ##
##   2 - Change a name                              ##
##   3 - Delete a name                              ##
##   4 - List all names                             ##
##   5 - Delete all names                           ##
##   6 - Quit                                       ##
##                                                  ##
######################################################
"""

names = []

def addName():
    system("clear")
    newName = input("Enter new name: ")
    
    print(f"Adding name {newName}...")
    names.append(newName)
    print("Done!")

def changeName():
    system("clear")
    if len(names) == 0:
        print("There are no names to change!")
        return
    
    for i in names:
        print(i)
    oldName = input("\nEnter old name you wish to change: ")
    
    if oldName not in names:
        print("Old name does not exist!")
        return
    else:
        newName = input("Enter new name: ")
    
    print("Changing name...")
    names.remove(oldName)
    names.append(newName)
    print("Done!")
    
def deleteName():
    system("clear")

    for i in names:
        print(i)
    oldName = input("\nEnter name you wish to delete: ")
    if oldName not in names:
        print("Name does not exist!")
        return
    else:
        print("Deleting name...")
        names.remove(oldName)
        print("Done!")

def listNames():
    system("clear")
    names.sort()
    
    for i in names:
        print(i)

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

def debug(): # add names to 'names' so I don't have to type a bunch in
    system("clear")
    
    names.append("Tim")
    names.append("John")
    names.append("Katie")
    names.append("Maria")
    names.append("Jessie")

    print("Names added")

def main():
    while True:
        system("clear")
        print(mainMenu)
        choice = input(">").strip()
        match choice:
            case "1":
                addName()
            case "2":
                changeName()
            case "3":
                deleteName()
            case "4":
                listNames()
            case "5":
                deleteAllNames()
            case "6":
                userExit()
            case "7": # for debugging, not shown in 'mainMenu'
                debug()
            case "8": # for debugging, not shown in 'mainMenu'
                system("clear")
                print(names)
            case default:
                print("Not a valid input!")
                return

        input("Press ENTER to continue...")

if __name__ == "__main__":
    main()
