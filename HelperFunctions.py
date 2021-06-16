from time import sleep
from re import search

# Describes how to use the program
def howToUse():
    print("Enter the floor you need when prompted.")
    print("If you need more floors, hit 'ctrl + c', and enter when prompted. Repeat up to 3 times.")
    print("")

# Prints user input error message
def userError():
    print("Enter either a floor number (1 - 5) or 'quit'.")
    print("")

# Closes the door
def closeDoor(sec=2):
    if sec == 2:
        print("Closing doors...")
        sleep(2)
    else: # Overload: This part can be interrupted
        print(f"Closing doors in {sec} seconds...")
        sleep(sec)

# Opens the door
def openDoor(currentFloor):
    print(f"Arrived at floor {currentFloor}; Opening doors...")
    sleep(4)

# Picks up the person
def pickUp(currentFloor):
    print(f"Picked up person from {currentFloor}.")
    sleep(1)

# Makes sure the number provided is anywhere from 1 to 5 (inclusive)
def isValidFloor(floorNum):
    if floorNum < 1 or floorNum > 5:
        return False
    else:
        return True

# Makes sure the word provided is the word "quit"
def isValidWord(word):
    if word != "quit":
        return False
    else:
        return True

# Makes sure input is a number
def isValidNumber(num):
    if not int(num):
        return False
    else:
        return True

# Runs user input through all validation
def isValidUserInput(userInput):
    if not isValidWord(userInput):
        isWord = search("[A-Za-z]", userInput)
        if isWord:
            return False
        elif userInput == "":
            return True
        else:
            intInput = int(userInput)
            if not isValidFloor(intInput):
                return False
            else:
                return True
    else:
        return True