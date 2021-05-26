# Time separations:
#     10 seconds before beginning to close door (after requesting one floor)
#        This turns into 5 seconds if requesting another floor
#     2 seconds to close the door
#     5 seconds to travel to each floor
#     4 seconds to open door
#     4 seconds to hold door when second floor requested (after hitting ctrl + c)
#     +5 seconds before closing the doors by typing 'hold door' (after hitting ctrl + c)
#
# Can prematurely close door during 10 second wait time by typing "close door" after requesting floor 
# There are 5 floors in this building. 
# Elevator will make stops at other floors if elevator requested at those floors - depending on direction of travel 

# Modules
from time import sleep
from re import search

# Helper Functions
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

# Processing Functions
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

def areOppositeDirections(currentFloor, floorNeeded, floorNeeded2, floorNeeded3=None, floorNeeded4=None):
    global current1Dif, current2Dif, current3Dif, current4Dif
    current1Dif = currentFloor - floorNeeded # Current floor above first floor needed
    current2Dif = currentFloor - floorNeeded2 # Current floor above second floor needed
    current3Dif = currentFloor - floorNeeded3 # Current floor above third floor needed
    current4Dif = currentFloor - floorNeeded4 # Current floor above fourth floor needed
    below1 = current1Dif < 0
    above1 = current1Dif > 0
    below2 = current2Dif < 0
    above2 = current2Dif > 0
    below3 = current3Dif < 0
    above3 = current3Dif > 0
    below4 = current4Dif < 0
    above4 = current4Dif > 0

    if (floorNeeded3 == None) and (floorNeeded4 == None): # 2 floors requested
        below2Above1 = above1 and below2
        below1Above2 = below1 and above2
        if not below1Above2 and not below2Above1: # If floors needed not opposite directions from current floor
            return False
        else:
            return True
    
    elif floorNeeded4 == None: # 3 floors requested (curFl: 1, flNd1: 3, flNd2: 2, flNd3: 5)
        below1Below2Above3 = below1 and below2 and above3
        below1Above2Below3 = below1 and above2 and below3
        above1Below2Below3 = above1 and below2 and below3
        below1Above2Above3 = below1 and above2 and above3
        above1Above2Below3 = above1 and above2 and below3
        above1Below2Above3 = above1 and below2 and above3
        notBelowOrAbovePt1 = (not below1Below2Above3) and (not below1Above2Below3) and (not above1Below2Below3)
        notBelowOrAbovePt2 = (not below1Above2Above3) and (not above1Above2Below3) and (not above1Below2Above3)

        if notBelowOrAbovePt1 and notBelowOrAbovePt2: # If all floors in same direction (in order of request)
            return False
        else:
            return True

    else: # 4 floors requested
        below1Below2Below3Above4 = below1 and below2 and below3 and above4
        below1Below2Above3Below4 = below1 and below2 and above3 and below4
        below1Above2Below3Below4 = below1 and above2 and below3 and below4
        above1Below2Below3Below4 = above1 and below2 and below3 and below4
        below1Below2Above3Above4 = below1 and below2 and above3 and above4
        below1Above2Above3Below4 = below1 and above2 and above3 and below4
        above1Above2Below3Below4 = above1 and above2 and below3 and below4
        below1Above2Below3Above4 = below1 and above2 and below3 and above4
        above1Below2Below3Above4 = above1 and below2 and below3 and above4
        above1Below2Above3Below4 = above1 and below2 and above3 and below4
        below1Above2Above3Above4 = below1 and above2 and above3 and above4
        above1Below2Above3Above4 = above1 and below2 and above3 and above4
        above1Above2Below3Above4 = above1 and above2 and below3 and above4
        above1Above2Above3Below4 = above1 and above2 and above3 and below4

        allInLinePt1 = (not below1Below2Below3Above4) and (not below1Below2Above3Below4) and (not below1Above2Below3Below4) and (not above1Below2Below3Below4)
        allInLinePt2 = (not below1Below2Above3Above4) and (not below1Above2Above3Below4) and (not above1Above2Below3Below4)
        allInLinePt3 = (not below1Above2Below3Above4) and (not above1Below2Below3Above4) and (not above1Below2Above3Below4)
        allInLinePt4 = (not below1Above2Above3Above4) and (not above1Below2Above3Above4) and (not above1Above2Below3Above4) and (not above1Above2Above3Below4)

        if (allInLinePt1) and (allInLinePt2) and (allInLinePt3) and (allInLinePt4):
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

def efficient(currentFloor, floorNeeded, floorNeeded2, floorNeeded3=None, floorNeeded4=None):
    oneCurrentDif = floorNeeded - currentFloor
    twoCurrentDif = floorNeeded2 - currentFloor
    threeCurrentDif = floorNeeded3 - currentFloor

    oneCurrCloser = oneCurrentDif < twoCurrentDif # If 1st requested floor closer, go there first
    twoCurrCloser = oneCurrentDif > twoCurrentDif # If 2nd requested floor closer, go there first
    if floorNeeded3 == None and floorNeeded4 == None: # 2 floor requests
        if (current1Dif < 0) and (current2Dif < 0): # If current floor beneath both requested floors
            if twoCurrCloser:
                currentFloor = inOrder(currentFloor, floorNeeded2, floorNeeded)
            elif oneCurrCloser:
                currentFloor = inOrder(currentFloor, floorNeeded, floorNeeded2)

        elif (current1Dif > 0) and (current2Dif > 0):# If current floor above both requested floors
            if current1Dif > current2Dif: # If 2nd floor requested closer, go there first
                currentFloor = inOrder(currentFloor, floorNeeded2, floorNeeded)
            elif current1Dif < current2Dif: # If 1st floor requested closer, go there first
                currentFloor = inOrder(currentFloor, floorNeeded, floorNeeded2)

    elif floorNeeded4 == None: # 3 floor requests
        oneCurrClosest = oneCurrCloser and (oneCurrentDif < threeCurrentDif)
        twoCurrClosest = twoCurrCloser and (twoCurrentDif < threeCurrentDif)
        threeCurrClosest = (threeCurrentDif < oneCurrentDif) and (threeCurrentDif < twoCurrentDif)
        if (current1Dif < 0) and (current2Dif < 0) and (current3Dif < 0): # If current floor beneath all requested floors
            if oneCurrClosest:
                
        
    return currentFloor

# def floorReq(currentFloor, floorNeeded, floorNeeded2=None):
#     if floorNeeded2 == None: # One floor request
#         closeDoor()
#         while currentFloor != floorNeeded:
#             currentFloor = switchingFloors(currentFloor, floorNeeded)
#         else:
#             openDoor(currentFloor)
# 
#     else: # Two floor reqeusts
#         are = areOppositeDirections(currentFloor, floorNeeded, floorNeeded2)
#         if not are:
#             currentFloor = efficient(currentFloor, floorNeeded, floorNeeded2)
#         else:
#             currentFloor = inOrder(currentFloor, floorNeeded, floorNeeded2)
#         
#     return currentFloor

def floorReq(currentFloor, floorNeeded, floorNeeded2=None, floorNeeded3=None, floorNeeded4=None):
    if (floorNeeded2 == None) and (floorNeeded3 == None) and (floorNeeded4 == None): # 1 floor request
        closeDoor()
        while currentFloor != floorNeeded:
            currentFloor = switchingFloors(currentFloor, floorNeeded)
        else:
            openDoor(currentFloor)

    elif (floorNeeded3 == None) and (floorNeeded4 == None): # 2 floor requests
        are = areOppositeDirections(currentFloor, floorNeeded, floorNeeded2)
        if not are:
            currentFloor = efficient(currentFloor, floorNeeded, floorNeeded2)
        else:
            currentFloor = inOrder(currentFloor, floorNeeded, floorNeeded2)

    elif floorNeeded4 == None: # 3 floor requests
        are = areOppositeDirections(currentFloor, floorNeeded, floorNeeded2, floorNeeded3)
        if not are:
            currentFloor = 


# Main function
def main():
    howToUse()
    keepGoing = True
    currentFloor = 1
    while keepGoing:
        floor = reqFloor() # Receive user input
        if not isValidWord(floor): # While input is not the word quit...
            isWord = search('[a-zA-Z]', floor)
            if isWord: # ...check for any letters...
                print("Enter either a floor number (1 - 5) or 'quit'.")
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