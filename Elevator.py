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

# ----------------------------- Helper Functions ----------------------------- #
# Describes how to use the program
def howToUse():
    print("Enter the floor you need when prompted.")
    print("If you need 2 floors, hit 'ctrl + c', and enter when prompted.")
    print("")

# Closes the door
def closeDoor(sec=2):
    if sec == 2:
        print(f"Closing doors...")
        sleep(2)
    else: # Overload: This part can be interrupted
        print(f"Closing doors in {sec} seconds...")
        sleep(sec)

# Opens the door
def openDoor(currentFloor):
    print(f"Arrived at floor {currentFloor}; Opening doors...")
    sleep(4)

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

# Checks for any letters in user's input
def isWord(word):
    if not str.isalpha(word):
        return False
    else:
        return True

# Makes sure input is a number
def isValidNumber(num):
    if not int(num):
        return False
    else:
        return True


# ----------------------------- Processing Functions ----------------------------- #
# Sends elevator to floor needed; returns the current floor
def switchingFloors(currentFloor, floorNeeded):
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

# Checks for floors in opposite directions relative to the currentFloor; Returns false or true
def areOppositeDirections(currentFloor, floorNeeded, floorNeeded2, floorNeeded3=None, floorNeeded4=None):
    # Describe position of a floor relative to the currentFloor (pt. 1)
    current1Dif = currentFloor - floorNeeded # Current floor above first floor needed
    current2Dif = currentFloor - floorNeeded2 # Current floor above second floor needed
    current3Dif = currentFloor - floorNeeded3 # Current floor above third floor needed
    current4Dif = currentFloor - floorNeeded4 # Current floor above fourth floor needed

    # Describe position of a floor relative to the currentFloor (pt. 2)
    below1 = current1Dif < 0
    above1 = current1Dif > 0
    below2 = current2Dif < 0
    above2 = current2Dif > 0
    below3 = current3Dif < 0
    above3 = current3Dif > 0
    below4 = current4Dif < 0
    above4 = current4Dif > 0

    # 2-floor-request scenario possible outcomes (a = Above; b = Below)
    b2A1 = above1 and below2
    b1A2 = below1 and above2

    # 3-floor-request scenario possible outcomes (a = Above; b = Below)
    b1B2A3 = below1 and below2 and above3
    b1A2B3 = below1 and above2 and below3
    a1B2B3 = above1 and below2 and below3
    b1A2A3 = below1 and above2 and above3
    a1A2B3 = above1 and above2 and below3
    a1B2A3 = above1 and below2 and above3

    # 4-floor-request scenario possible outcomes (a = Above; b = Below)
    b1B2B3A4 = below1 and below2 and below3 and above4
    b1B2A3B4 = below1 and below2 and above3 and below4
    b1A2B3B4 = below1 and above2 and below3 and below4
    a1B2B3B4 = above1 and below2 and below3 and below4
    b1B2A3A4 = below1 and below2 and above3 and above4
    b1A2A3B4 = below1 and above2 and above3 and below4
    a1A2B3B4 = above1 and above2 and below3 and below4
    b1A2B3A4 = below1 and above2 and below3 and above4
    a1B2B3A4 = above1 and below2 and below3 and above4
    a1B2A3B4 = above1 and below2 and above3 and below4
    b1A2A3A4 = below1 and above2 and above3 and above4
    a1B2A3A4 = above1 and below2 and above3 and above4
    a1A2B3A4 = above1 and above2 and below3 and above4
    a1A2A3B4 = above1 and above2 and above3 and below4

    # Acutal function
    if (floorNeeded3 == None) and (floorNeeded4 == None): # 2 floors requested
        if (not b1A2) and (not b2A1): # If floors needed not opposite directions from current floor
            return False
        else:
            return True
    
    elif floorNeeded4 == None: # 3 floors requested
        notBelowOrAbovePt1 = (not b1B2A3) and (not b1A2B3) and (not a1B2B3)
        notBelowOrAbovePt2 = (not b1A2A3) and (not a1A2B3) and (not a1B2A3)
        if notBelowOrAbovePt1 and notBelowOrAbovePt2:
            return False
        else:
            return True

    else: # 4 floors requested
        allInLinePt1 = (not b1B2B3A4) and (not b1B2A3B4) and (not b1A2B3B4) and (not a1B2B3B4)
        allInLinePt2 = (not b1B2A3A4) and (not b1A2A3B4) and (not a1A2B3B4)
        allInLinePt3 = (not b1A2B3A4) and (not a1B2B3A4) and (not a1B2A3B4)
        allInLinePt4 = (not b1A2A3A4) and (not a1B2A3A4) and (not a1A2B3A4) and (not a1A2A3B4)
        if (allInLinePt1) and (allInLinePt2) and (allInLinePt3) and (allInLinePt4):
            return False
        else:
            return True

# Operates the elevator (makes it move from floor to floor)
def execute(currentFloor, floorNeeded, floorNeeded2=None, floorNeeded3=None, floorNeeded4=None):
    if floorNeeded2 == None and floorNeeded3 == None and floorNeeded4 == None: # 1 floor request
        closeDoor()
        currentFloor = switchingFloors(currentFloor, floorNeeded)
        openDoor(currentFloor)

    if floorNeeded3 == None and floorNeeded4 == None: # 2 floor requests
        closeDoor()
        currentFloor = switchingFloors(currentFloor, floorNeeded)
        openDoor(currentFloor)

        closeDoor()
        currentFloor = switchingFloors(currentFloor, floorNeeded2) # To the last requested floor
        openDoor(currentFloor)

    elif floorNeeded4 == None: # 3 floor requests
        closeDoor()
        currentFloor = switchingFloors(currentFloor, floorNeeded) # To the first requested floor...
        openDoor(currentFloor)

        closeDoor()
        currentFloor = switchingFloors(currentFloor, floorNeeded2) # To the second requested floor...
        openDoor(currentFloor)

        closeDoor()
        currentFloor = switchingFloors(currentFloor, floorNeeded3) # To the last requested floor
        openDoor(currentFloor)

    else: # 4 floor requests
        closeDoor()
        currentFloor = switchingFloors(currentFloor, floorNeeded) # To the first requested floor...
        openDoor(currentFloor)

        closeDoor()
        currentFloor = switchingFloors(currentFloor, floorNeeded2) # To the second requested floor...
        openDoor(currentFloor)

        closeDoor()
        currentFloor = switchingFloors(currentFloor, floorNeeded3) # To the third requested floor...
        openDoor(currentFloor)

        closeDoor()
        currentFloor = switchingFloors(currentFloor, floorNeeded4) # To the last requested floor
        openDoor(currentFloor)
    return currentFloor

# Returns list of floors needed in index order ([closestFloorNeeded, nextClosestFloorNeeded])
def closestFloor(currentFloor, floorNeeded, floorNeeded2, floorNeeded3=None, floorNeeded4=None):
    # Describe position of a floor relative to the currentFloor (pt. 1)
    current1Dif = currentFloor - floorNeeded # Current floor above first floor needed
    current2Dif = currentFloor - floorNeeded2 # Current floor above second floor needed
    current3Dif = currentFloor - floorNeeded3 # Current floor above third floor needed
    current4Dif = currentFloor - floorNeeded4 # Current floor above fourth floor needed
    oneCurrentDif = floorNeeded - currentFloor # Current floor below first floor needed
    twoCurrentDif = floorNeeded2 - currentFloor # Current floor below second floor needed
    threeCurrentDif = floorNeeded3 - currentFloor # Current floor below third floor needed
    fourCurrentDif = floorNeeded4 - currentFloor # Current floor below fourth floor needed

    # Describe position of a floor relative to the currentFloor (pt. 2)
    below1 = current1Dif < 0
    above1 = current1Dif > 0
    below2 = current2Dif < 0
    above2 = current2Dif > 0
    below3 = current3Dif < 0
    above3 = current3Dif > 0
    below4 = current4Dif < 0
    above4 = current4Dif > 0

    if floorNeeded3 == None and floorNeeded4 == None: # 2 floor requests
        if below1 and below2: # If current floor beneath both requested floors
            oneCurrCloser = oneCurrentDif < twoCurrentDif # 1st floor is closer
            twoCurrCloser = oneCurrentDif > twoCurrentDif # 2nd floor is closer
            if twoCurrCloser: # If 2nd requested floor closer, return it
                return [floorNeeded2, floorNeeded]
            elif oneCurrCloser: # If 1st requested floor closer, return it
                return [floorNeeded, floorNeeded2]

        elif above1 and above2: # If current floor above both requested floors
            currOneCloser = current1Dif < current2Dif # 1st floor is closer
            currTwoCloser = current1Dif > current2Dif # 2nd floor is closer
            if currTwoCloser: # If 2nd floor requested closer, return it
                return [floorNeeded2, floorNeeded]
            elif currOneCloser: # If 1st floor requested closer, return it
                return [floorNeeded, floorNeeded2]

        
    elif floorNeeded4 == None: # 3 floor requests
        if below1 and below2 and below3: # If currentFloor beneath all requested floors
            oneCurrClosest = (oneCurrentDif < twoCurrentDif) and (oneCurrentDif < threeCurrentDif)
            twoCurrClosest = (twoCurrentDif < oneCurrentDif) and (twoCurrentDif < threeCurrentDif)
            threeCurrClosest = (threeCurrentDif < oneCurrentDif) and (threeCurrentDif < twoCurrentDif)

            if oneCurrClosest: # floorNeeded is closest
                twoCurrCloser = twoCurrentDif < threeCurrentDif
                threeCurrCloser = twoCurrentDif > threeCurrentDif
                if twoCurrCloser: # floorNeeded2 is next closest
                    return [floorNeeded, floorNeeded2, floorNeeded3]
                elif threeCurrCloser: # floorNeeded3 is next closest
                    return [floorNeeded, floorNeeded3, floorNeeded2]

            elif twoCurrClosest: # floorNeeded2 is closest
                oneCurrCloser = oneCurrentDif < threeCurrentDif
                threeCurrCloser = oneCurrentDif > threeCurrentDif
                if oneCurrCloser: # floorNeeded is next closest
                    return [floorNeeded2, floorNeeded, floorNeeded3]
                elif threeCurrCloser: # floorNeeded3 is next closest
                    return [floorNeeded2, floorNeeded3, floorNeeded]

            elif threeCurrClosest: # floorNeeded3 is closest
                oneCurrCloser = oneCurrentDif < twoCurrentDif
                twoCurrCloser = oneCurrentDif > twoCurrentDif
                if oneCurrCloser: # floorNeeded is next closest
                    return [floorNeeded3, floorNeeded, floorNeeded2]
                elif twoCurrCloser: # floorNeeded2 is next closest
                    return [floorNeeded3, floorNeeded2, floorNeeded]
        
        elif above1 and above2 and above3: # If currentFloor above all requested floors
            oneCurrClosest = (current1Dif < current2Dif) and (current1Dif < current3Dif)
            twoCurrClosest = (current2Dif < current1Dif) and (current2Dif < current3Dif)
            threeCurrClosest = (current3Dif < current1Dif) and (current3Dif < current2Dif)

            if oneCurrClosest: # floorNeeded is closest
                twoCurrCloser = current2Dif < current3Dif
                threeCurrCloser = current2Dif > current3Dif
                if twoCurrCloser: # floorNeeded2 is next closest
                    return [floorNeeded, floorNeeded2, floorNeeded3]
                elif threeCurrCloser: # floorNeeded3 is next closest
                    return [floorNeeded, floorNeeded3, floorNeeded2]

            elif twoCurrClosest: # floorNeeded2 is closest
                oneCurrCloser = current1Dif < current3Dif
                threeCurrCloser = current1Dif > current3Dif
                if oneCurrCloser: # floorNeeded is next closest
                    return [floorNeeded2, floorNeeded, floorNeeded3]
                elif threeCurrCloser: # floorNeeded3 is next closest
                    return [floorNeeded2, floorNeeded3, floorNeeded]

            elif threeCurrClosest: # floorNeeded3 is closest
                oneCurrCloser = current1Dif < current2Dif
                twoCurrCloser = current1Dif > current2Dif
                if oneCurrCloser: # floorNeeded is next closest
                    return [floorNeeded3, floorNeeded, floorNeeded2]
                elif twoCurrCloser: # floorNeeded2 is next closest
                    return [floorNeeded3, floorNeeded2, floorNeeded]

    
    else: # 4 floor requests
        if below1 and below2 and below3 and below4: # currentFloor is below all floors needed
            oneCurrClosest = (oneCurrentDif < twoCurrentDif) and (oneCurrentDif < threeCurrentDif) and (oneCurrentDif < fourCurrentDif)
            twoCurrClosest = (twoCurrentDif < oneCurrentDif) and (twoCurrentDif < threeCurrentDif) and (twoCurrentDif < fourCurrentDif)
            threeCurrClosest = (threeCurrentDif < oneCurrentDif) and (threeCurrentDif < twoCurrentDif) and (threeCurrentDif < fourCurrentDif)
            fourCurrClosest = (fourCurrentDif < oneCurrentDif) and (fourCurrentDif < twoCurrentDif) and (fourCurrentDif < threeCurrentDif)

            if oneCurrClosest: # floorNeeded is closest
                twoCurrCloser = (twoCurrentDif < threeCurrentDif) and (twoCurrentDif < fourCurrentDif)
                threeCurrCloser = (threeCurrentDif < twoCurrentDif) and (threeCurrentDif < fourCurrentDif)
                fourCurrCloser = (fourCurrentDif < twoCurrentDif) and (fourCurrentDif < threeCurrentDif)
                if twoCurrCloser: # floorNeeded2 is 2nd closest
                    threeCurrNext = threeCurrentDif < fourCurrentDif
                    fourCurrNext = threeCurrentDif > fourCurrentDif
                    if threeCurrNext: # floorNeeded3 is 2nd farthest
                        return [floorNeeded, floorNeeded2, floorNeeded3, floorNeeded4]
                    elif fourCurrNext: # floorNeeded4 is 2nd farthest
                        return [floorNeeded, floorNeeded2, floorNeeded4, floorNeeded3]

                elif threeCurrCloser: # floorNeeded3 is 2nd closest
                    twoCurrNext = twoCurrentDif < fourCurrentDif
                    fourCurrNext = twoCurrentDif > fourCurrentDif
                    if twoCurrNext: # floorNeeded2 is 2nd farthest
                        return [floorNeeded, floorNeeded3, floorNeeded2, floorNeeded4]
                    elif fourCurrNext: # floorNeeded4 is 2nd farthest
                        return [floorNeeded, floorNeeded3, floorNeeded4, floorNeeded2]

                elif fourCurrCloser: # floorNeeded4 is 2nd closest
                    twoCurrNext = twoCurrentDif < threeCurrentDif
                    threeCurrNext = twoCurrentDif > threeCurrentDif
                    if twoCurrNext:
                        return [floorNeeded, floorNeeded4, floorNeeded2, floorNeeded3]
                    elif threeCurrNext:
                        return [floorNeeded, floorNeeded4, floorNeeded3, floorNeeded2]
            
            elif twoCurrClosest: # floorNeeded2 is closest
                oneCurrCloser = (oneCurrentDif < threeCurrentDif) and (oneCurrentDif < fourCurrentDif)
                threeCurrCloser = (threeCurrentDif < oneCurrentDif) and (threeCurrentDif < fourCurrentDif)
                fourCurrCloser = (fourCurrentDif < oneCurrentDif) and (fourCurrentDif < threeCurrentDif)
                if oneCurrCloser: # floorNeeded is 2nd closest
                    threeCurrNext = threeCurrentDif < fourCurrentDif
                    fourCurrNext = threeCurrentDif > fourCurrentDif
                    if threeCurrNext: # floorNeeded3 is 2nd farthest
                        return [floorNeeded2, floorNeeded, floorNeeded3, floorNeeded4]
                    elif fourCurrNext: # floorNeeded4 is 2nd farthest
                        return [floorNeeded2, floorNeeded, floorNeeded4, floorNeeded3]

                elif threeCurrCloser: # floorNeeded3 is 2nd closest
                    oneCurrNext = oneCurrentDif < fourCurrentDif
                    fourCurrNext = oneCurrentDif > fourCurrentDif
                    if oneCurrNext: # floorNeeded is 2nd farthest
                        return [floorNeeded2, floorNeeded3, floorNeeded, floorNeeded4]
                    elif fourCurrNext: # floorNeeded4 is 2nd farthest
                        return [floorNeeded2, floorNeeded3, floorNeeded4, floorNeeded]

                elif fourCurrCloser: # floorNeeded4 is 2nd closest
                    oneCurrNext = oneCurrentDif < threeCurrentDif
                    threeCurrNext = oneCurrentDif > threeCurrentDif
                    if oneCurrNext: # floorNeeded is 2nd farthest
                        return [floorNeeded2, floorNeeded4, floorNeeded, floorNeeded3]
                    elif threeCurrNext: # floorNeeded3 is 2nd farthest
                        return [floorNeeded2, floorNeeded4, floorNeeded3, floorNeeded]
            
            elif threeCurrClosest: # floorNeeded3 is closest
                oneCurrCloser = (oneCurrentDif < twoCurrentDif) and (oneCurrentDif < fourCurrentDif)
                twoCurrCloser = (twoCurrentDif < oneCurrentDif) and (twoCurrentDif < fourCurrentDif)
                fourCurrCloser = (fourCurrentDif < oneCurrentDif) and (fourCurrentDif < twoCurrentDif)
                if oneCurrCloser: # floorNeeded is 2nd closest
                    twoCurrNext = twoCurrentDif < fourCurrentDif
                    fourCurrNext = twoCurrentDif > fourCurrentDif
                    if twoCurrNext: # floorNeeded2 is 2nd farthest
                        return [floorNeeded3, floorNeeded, floorNeeded2, floorNeeded4]
                    elif fourCurrNext: # floorNeeded4 is 2nd farthest
                        return [floorNeeded3, floorNeeded, floorNeeded4, floorNeeded2]

                elif twoCurrCloser: # floorNeeded2 is 2nd closest
                
                elif fourCurrCloser: # floorNeeded4 is 2nd closest

            elif fourCurrClosest: # floorNeeded4 is closest

        elif above1 and above2 and above3 and above4: # currentFloor is above all floors needed
            oneCurrClosest = (current1Dif < current2Dif) and (current1Dif < current3Dif) and (current1Dif < current4Dif)
            twoCurrClosest = (current2Dif < current1Dif) and (current2Dif < current3Dif) and (current2Dif < current4Dif)
            threeCurrClosest = (current3Dif < current1Dif) and (current3Dif < current2Dif) and (current3Dif < current4Dif)
            fourCurrClosest = (current4Dif < current1Dif) and (current4Dif < current2Dif) and (current4Dif < current3Dif)

def efficient(currentFloor, floorNeeded, floorNeeded2, floorNeeded3=None, floorNeeded4=None):
    # Describe position of a floor relative to the currentFloor (pt. 1)
    current1Dif = currentFloor - floorNeeded # Current floor above first floor needed
    current2Dif = currentFloor - floorNeeded2 # Current floor above second floor needed
    current3Dif = currentFloor - floorNeeded3 # Current floor above third floor needed
    current4Dif = currentFloor - floorNeeded4 # Current floor above fourth floor needed
    oneCurrentDif = floorNeeded - currentFloor # Current floor below first floor needed
    twoCurrentDif = floorNeeded2 - currentFloor # Current floor below second floor needed
    threeCurrentDif = floorNeeded3 - currentFloor # Current floor below third floor needed
    fourCurrentDif = floorNeeded4 - currentFloor # Current floor below fourth floor needed

    # Describe position of a floor relative to the currentFloor (pt. 2)
    below1 = current1Dif < 0
    above1 = current1Dif > 0
    below2 = current2Dif < 0
    above2 = current2Dif > 0
    below3 = current3Dif < 0
    above3 = current3Dif > 0
    below4 = current4Dif < 0
    above4 = current4Dif > 0

    if floorNeeded3 == None and floorNeeded4 == None: # 2 floor requests

        if below1 and below2: # If current floor beneath both requested floors
            oneCurrCloser = oneCurrentDif < twoCurrentDif # 1st floor is closer
            twoCurrCloser = oneCurrentDif > twoCurrentDif # 2nd floor is closer
            if twoCurrCloser: # If 2nd requested floor closer, return it
                currentFloor = execute(currentFloor, floorNeeded2, floorNeeded)
            elif oneCurrCloser: # If 1st requested floor closer, return it
                currentFloor = execute(currentFloor, floorNeeded, floorNeeded2)

        elif above1 and above2:# If current floor above both requested floors
            currOneCloser = current1Dif < current2Dif # 1st floor is closer
            currTwoCloser = current1Dif > current2Dif # 2nd floor is closer
            if currTwoCloser: # If 2nd floor requested closer, return it
                currentFloor = execute(currentFloor, floorNeeded2, floorNeeded)
            elif currOneCloser: # If 1st floor requested closer, return it
                currentFloor = execute(currentFloor, floorNeeded, floorNeeded2)

    elif floorNeeded4 == None: # 3 floor requests
        if below1 and below2 and below3: # If current floor beneath all requested floors

            # Find closest floor
            oneCurrClosest = (oneCurrentDif < twoCurrentDif) and (oneCurrentDif < threeCurrentDif)
            twoCurrClosest = (twoCurrentDif < oneCurrentDif) and (twoCurrentDif < threeCurrentDif)
            threeCurrClosest = (threeCurrentDif < oneCurrentDif) and (threeCurrentDif < twoCurrentDif)

            if oneCurrClosest: # If 1st floor closest...
                twoCurrCloser = twoCurrentDif < threeCurrentDif
                threeCurrCloser = twoCurrentDif > threeCurrentDif

                if twoCurrCloser: # ...and 2nd floor next closest...
                    currentFloor = execute(currentFloor, floorNeeded, floorNeeded2, floorNeeded3)
                elif threeCurrCloser:
        
    return currentFloor

# Either runs execute function directly (if floors are in opposite directions)
#   or runs efficient function (if all needed floors are in one direction)
def floorReq(currentFloor, floorNeeded, floorNeeded2=None, floorNeeded3=None, floorNeeded4=None):
    if (floorNeeded2 == None) and (floorNeeded3 == None) and (floorNeeded4 == None): # 1 floor request
        currentFloor = execute(currentFloor, floorNeeded)

    elif (floorNeeded3 == None) and (floorNeeded4 == None): # 2 floor requests
        are = areOppositeDirections(currentFloor, floorNeeded, floorNeeded2)
        if not are:
            currentFloor = efficient(currentFloor, floorNeeded, floorNeeded2)
        else:
            currentFloor = execute(currentFloor, floorNeeded, floorNeeded2)

    elif floorNeeded4 == None: # 3 floor requests
        are = areOppositeDirections(currentFloor, floorNeeded, floorNeeded2, floorNeeded3)
        if not are:
            currentFloor = efficient(currentFloor, floorNeeded, floorNeeded2, floorNeeded3)
        else:
            currentFloor = execute(currentFloor, floorNeeded, floorNeeded2, floorNeeded3)

    else: # 4 floor requests
        are = areOppositeDirections(currentFloor, floorNeeded, floorNeeded2, floorNeeded3, floorNeeded4)
        if not are:
            currentFloor = efficient(currentFloor, floorNeeded, floorNeeded2, floorNeeded3, floorNeeded4)
        else:
            currentFloor = execute(currentFloor, floorNeeded, floorNeeded2, floorNeeded3, floorNeeded4)
    return currentFloor


# Main function
def main():
    howToUse()
    keepGoing = True
    while keepGoing:
        floor = input("Which floor do you need?: ") # Receive user input
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
                        floor2 = input("Which other floor do you need?: ") # ...receive the 2nd request...
                        intFloor2 = int(floor2)
                        currentFloor = floorReq(currentFloor, intFloor, intFloor2) #...and fulfill it.
        else:
            print("Elevator shutting down...")
            keepGoing = False