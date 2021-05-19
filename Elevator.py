# Time separations:
#     10 seconds before beginning to close door (after requesting one floor)
#        This turns into 5 seconds if requesting another floor
#     2 seconds to close the door
#     5 seconds to travel to each floor
#     2 seconds to open door
#     4 seconds to hold door when second floor requested
#     +5 seconds before closing the doors by typing 'hold door'
#
# Can prematurely close door during 10 second wait time by typing "close door" after requesting floor 
# There are 5 floors in this building. 
# Elevator will make stops at other floors if elevator requested at those floors - depending on direction of travel 
"""
The above is being worked on for efficient travel, but it does currently travel
to the first requested floor, then to the second requested floor
"""

# Modules
from time import sleep
from re import search

# Functions
def howToUse():
    print("Enter the floor you need when prompted.")
    print("If you need 2 floors, hit 'ctrl + c', and enter when prompted.")
    print("")

def reqFloor(): # Receives and returns user's input
    return input("Which floor do you need?: ")

def closeDoor(sec=2): # Closes the doors
    if sec == 2:
        print(f"Closing doors...")
        sleep(2)
    else: # Overload: This part can be interrupted
        print(f"Closing doors in {sec} seconds...")
        sleep(sec)

def openDoor(currentFloor):
    print(f"Arrived at floor {currentFloor}; Opening doors...")
    sleep(4)

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

def isWord(word):
    if not str.isalpha(word):
        return False
    else:
        return True

def isValidNumber(num): # Makes sure input is a number
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

def areOppositeDirections(currentFloor, floorNeeded, floorNeeded2):
    global current1Dif, current2Dif
    current1Dif = currentFloor - floorNeeded # Current floor above first floor needed
    current2Dif = currentFloor - floorNeeded2 # Current floor above second floor needed
    below2Above1 = (current1Dif > 0) and (current2Dif < 0)
    below1Above2 = (current1Dif < 0) and (current2Dif > 0)
    if not below1Above2 and not below2Above1: # If floors needed not opposite directions from current floor
        return False
    else:
        return True

def inOrder(currentFloor, floorNeeded, floorNeeded2):
    closeDoor()
    while currentFloor != floorNeeded:
        currentFloor = switchingFloors(currentFloor, floorNeeded)
    else:
        openDoor(currentFloor)
        closeDoor()
        currentFloor = switchingFloors(currentFloor, floorNeeded2)
    openDoor(currentFloor)
    return currentFloor

def efficient(currentFloor, floorNeeded, floorNeeded2):
    oneCurrentDif = floorNeeded - currentFloor
    twoCurrentDif = floorNeeded2 - currentFloor
    if (current1Dif < 0) and (current2Dif < 0):
        if oneCurrentDif > twoCurrentDif:
            currentFloor = inOrder(currentFloor, floorNeeded2, floorNeeded)
        elif oneCurrentDif < twoCurrentDif:
            currentFloor = inOrder(currentFloor, floorNeeded, floorNeeded2)
    elif (current1Dif > 0) and (current2Dif > 0):
        if current1Dif > current2Dif:
            currentFloor = inOrder(currentFloor, floorNeeded2, floorNeeded)
        elif current1Dif < current2Dif:
            currentFloor = inOrder(currentFloor, floorNeeded, floorNeeded2)
    return currentFloor

def floorReq(currentFloor, floorNeeded, floorNeeded2=None):
    if floorNeeded2 == None: # One floor request
        closeDoor()
        while currentFloor != floorNeeded:
            currentFloor = switchingFloors(currentFloor, floorNeeded)
        else:
            print(f"You have arrived at floor {currentFloor}.")

    else: # Two floor reqeusts
        closeDoor()
        are = areOppositeDirections(currentFloor, floorNeeded, floorNeeded2)
        if not are:
            currentFloor = inOrder(currentFloor, floorNeeded, floorNeeded2)
        else:
            currentFloor = efficient(currentFloor, floorNeeded, floorNeeded2)
        
    return currentFloor

def main():
    howToUse()
    keepGoing = True
    currentFloor = 1
    while keepGoing:
        floor = reqFloor() # Receive user input
        if not isValidWord(floor): # While input is not the word quit...
            isWord = search('[a-zA-Z]', floor)
            if isWord: # ...check for any letters...
                print("Enter either a floor number (1 - 5), or enter 'quit'.")
                print("")
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
                        closeDoor(10)
                        currentFloor = floorReq(currentFloor, intFloor)
                    except KeyboardInterrupt: # If user hits 'ctrl + c'...
                        floor2 = reqFloor() # ...receive the 2nd request...
                        intFloor2 = int(floor2)
                        currentFloor = floorReq(currentFloor, intFloor, intFloor2) #...and fulfill it.
        else:
            print("Elevator shutting down...")
            keepGoing = False

main()