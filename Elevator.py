# After making a floor request, must wait 10 seconds for door to begin closing, 2 seconds for the door to shut, and 5 seconds travel time per floor #
# Can prematurely close door during 10 second wait time with no consequences by typing "close door" after requesting floor #
# Can hold door open 5 seconds longer during 10 second wait time by typing "hold door" after requesting floor #
# Elevator will make stops at other floors if elevator requested at those floors - depending on direction of travel #
# There are 5 floors in this building. #

# Modules
from time import sleep

# Functions
def howToUse():
    print("")
    print("Enter the floor you need when prompted.")
    print("If you need 2 floors, hit 'ctrl + c', and enter when prompted.")
    print("")

def reqFloor(): # Receives and returns user's input
    return input("Which floor do you need?: ")

def closeDoor(): # Can be interrupted
    print("Closing door in 10 seconds...")
    sleep(10)

def isValidFloor(floorNum): # Makes sure the number provided is anywhere from 1 to 5 (inclusive)
    if floorNum < 1 or floorNum > 5:
        return False
    else:
        return True

def isValidWord(word): # Makes sure the word provided is the word "quit"
    if word != "quit":
        return False
    else:
        return True

def isValidNumber(num):
    if not int(num):
        return False
    else:
        return True

def switchingFloors(currentFloor, floorNeeded): # Sends elevator to floor needed and returns the current floor
    while currentFloor < floorNeeded:
        print("Currently at floor", currentFloor,". Going up...")
        sleep(5)
        currentFloor += 1
    else:
        while currentFloor > floorNeeded:
            print("Currently at floor", currentFloor,". Going down...")
            sleep(5)
            currentFloor -= 1
    return currentFloor

# This function takes one floor request
def floorReq(floorNeeded, currentFloor): # Sends user to appropriate floor
    print("Closing doors...")
    sleep(2)
    while currentFloor != floorNeeded:
        currentFloor = switchingFloors(currentFloor, floorNeeded)
    else:
        print("You have arrived at floor", currentFloor)
    return currentFloor

# This function takes two floor requests
def doubleFloorReq(floorNeeded1, floorNeeded2, currentFloor):
    print("Closing doors...")
    sleep(2)
    while currentFloor != floorNeeded1:
        currentFloor = switchingFloors(currentFloor, floorNeeded1)
    else:
        print("Arrived at floor", currentFloor,"; opening doors...")
        sleep(4)
        print("Closing doors...")
        sleep(2)
        currentFloor = switchingFloors(currentFloor, floorNeeded2)
    print("You have arrived at floor", currentFloor,".")
    return currentFloor

def main():
    howToUse()
    keepGoing = True
    while keepGoing:
        floor = reqFloor() # Receive user input
        currentFloor = 1
        if not isValidWord(floor): # While input is not the word quit...
            if not isValidNumber(floor):# ...make sure it's a number.
                print("Enter either a floor number (1 - 5), or enter 'quit'.")
                keepGoing = True
                continue
            else: # If it is a number...
                intFloor = int(floor)
                if not isValidFloor(intFloor): # ...then make sure it's between 1 and 5 (inclusive)
                    print("Enter a valid floor number (1 - 5).")
                    print("")
                    keepGoing = True
                    continue
                else: # Now all is well. Continue with the program.
                    try: # Only one floor request
                        closeDoor()
                        currentFloor = floorReq(intFloor, currentFloor)
                        floor = reqFloor()
                    except KeyboardInterrupt: # If user hits 'ctrl + c'...
                        floor2 = reqFloor() # ...receive the 2nd request...
                        intFloor2 = int(floor2)
                        currentFloor = doubleFloorReq(intFloor, intFloor2, currentFloor) #...and fulfill it.
        else:
            print("Elevator shutting down...")
            keepGoing = False

main()