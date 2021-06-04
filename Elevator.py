# Time separations:
#     10 seconds before beginning to close door (after requesting one floor)
#        This turns into 5 seconds if requesting another floor
#     2 seconds to close the door
#     5 seconds to travel to each floor
#     4 seconds to open door
#     +5 seconds before closing the doors by typing 'hold door' (after hitting ctrl + c) (yet to attempt)
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

# Runs user input through all validation
def isValidUserInput(userInput):
    if not isValidWord(userInput):
        isWord = search("[A-Za-z]", userInput)
        if isWord:
            return False
        else:
            intInput = int(userInput)
            if not isValidFloor(intInput):
                return False
            else:
                return True
    else:
        return True



# ----------------------------- Processing Functions ----------------------------- #

# Sends elevator to floor needed; returns the current floor
def switchingFloors(currentFloor, floorNeeded):
    while currentFloor < floorNeeded: # currentFloor beneath floorNeeded. Go up
        print(f"Currently at floor {currentFloor}. Going up...")
        sleep(5)
        currentFloor += 1
    else:
        while currentFloor > floorNeeded: # currentFloor above floorNeede. Go down
            print(f"Currently at floor {currentFloor}. Going down...")
            sleep(5)
            currentFloor -= 1
    return currentFloor

# Makes elevator move
def execute(currentFloor, floorNeeded, floorNeeded2=None, floorNeeded3=None, floorNeeded4=None):
    if floorNeeded2 == None and floorNeeded3 == None and floorNeeded4 == None: # 1 floor request
        closeDoor()
        currentFloor = switchingFloors(currentFloor, floorNeeded)
        openDoor(currentFloor)
    else: # create list for itteration; repeat code with each floor until reaching NoneValue
        floorsNeeded = [floorNeeded, floorNeeded2, floorNeeded3, floorNeeded4]
        for floor in floorsNeeded: 
            if floor == None: # If NoneValue reached, all other floors after will have NoneValue. break loop
                break
            else:
                closeDoor()
                currentFloor = switchingFloors(currentFloor, floor)
                openDoor(currentFloor)
    return currentFloor

# Checks for floors in opposite directions relative to the currentFloor; Returns false or true
def areOppositeDirections(currentFloor, floorNeeded, floorNeeded2, floorNeeded3=None, floorNeeded4=None):
    if (floorNeeded3 == None) and (floorNeeded4 == None): # 2 floors requested
        current1Dif = currentFloor - floorNeeded # Current floor above first floor needed
        current2Dif = currentFloor - floorNeeded2 # Current floor above second floor needed
        below1 = current1Dif < 0
        above1 = current1Dif > 0
        below2 = current2Dif < 0
        above2 = current2Dif > 0
        b2A1 = above1 and below2
        b1A2 = below1 and above2
        if (not b1A2) and (not b2A1): # If floors needed not opposite directions from current floor
            return False
        else:
            return True
    
    elif floorNeeded4 == None: # 3 floors requested
        current1Dif = currentFloor - floorNeeded # Current floor above first floor needed
        current2Dif = currentFloor - floorNeeded2 # Current floor above second floor needed
        current3Dif = currentFloor - floorNeeded3 # Current floor above third floor needed
        below1 = current1Dif < 0
        above1 = current1Dif > 0
        below2 = current2Dif < 0
        above2 = current2Dif > 0
        below3 = current3Dif < 0
        above3 = current3Dif > 0
        b1B2A3 = below1 and below2 and above3
        b1A2B3 = below1 and above2 and below3
        a1B2B3 = above1 and below2 and below3
        b1A2A3 = below1 and above2 and above3
        a1A2B3 = above1 and above2 and below3
        a1B2A3 = above1 and below2 and above3
        notBelowOrAbovePt1 = (not b1B2A3) and (not b1A2B3) and (not a1B2B3)
        notBelowOrAbovePt2 = (not b1A2A3) and (not a1A2B3) and (not a1B2A3)
        if notBelowOrAbovePt1 and notBelowOrAbovePt2:
            return False
        else:
            return True

    else: # 4 floors requested
        # Describe position of a floor relative to the currentFloor
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

        # Conditional statement
        allInLinePt1 = (not b1B2B3A4) and (not b1B2A3B4) and (not b1A2B3B4) and (not a1B2B3B4)
        allInLinePt2 = (not b1B2A3A4) and (not b1A2A3B4) and (not a1A2B3B4)
        allInLinePt3 = (not b1A2B3A4) and (not a1B2B3A4) and (not a1B2A3B4)
        allInLinePt4 = (not b1A2A3A4) and (not a1B2A3A4) and (not a1A2B3A4) and (not a1A2A3B4)
        if (allInLinePt1) and (allInLinePt2) and (allInLinePt3) and (allInLinePt4):
            return False
        else:
            return True

# Returns list of floors needed in index order ([closestFloorNeeded, nextClosestFloorNeeded, etc.])
def closestFloor(currentFloor, floorNeeded, floorNeeded2, floorNeeded3=None, floorNeeded4=None): # Needes to be DRYed up desperately
    if floorNeeded3 == None and floorNeeded4 == None: # 2 floor requests
        # Describe position of a floor relative to the currentFloor #
        current1Dif = currentFloor - floorNeeded # Current floor above first floor needed
        current2Dif = currentFloor - floorNeeded2 # Current floor above second floor needed
        oneCurrentDif = floorNeeded - currentFloor # Current floor below first floor needed
        twoCurrentDif = floorNeeded2 - currentFloor # Current floor below second floor needed
        below1 = current1Dif < 0
        above1 = current1Dif > 0
        below2 = current2Dif < 0
        above2 = current2Dif > 0

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
        current1Dif = currentFloor - floorNeeded # Current floor above first floor needed
        current2Dif = currentFloor - floorNeeded2 # Current floor above second floor needed
        current3Dif = currentFloor - floorNeeded3 # Current floor above third floor needed
        oneCurrentDif = floorNeeded - currentFloor # Current floor below first floor needed
        twoCurrentDif = floorNeeded2 - currentFloor # Current floor below second floor needed
        threeCurrentDif = floorNeeded3 - currentFloor # Current floor below third floor needed
        below1 = current1Dif < 0
        above1 = current1Dif > 0
        below2 = current2Dif < 0
        above2 = current2Dif > 0
        below3 = current3Dif < 0
        above3 = current3Dif > 0

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
                    oneCurrNext = oneCurrentDif < fourCurrentDif
                    fourCurrNext = oneCurrentDif > fourCurrentDif
                    if oneCurrNext: # floorNeeded is 2nd farthest
                        return [floorNeeded3, floorNeeded2, floorNeeded, floorNeeded4]
                    elif fourCurrNext: # floorNeeded4 is 2nd farthest
                        return [floorNeeded3, floorNeeded2, floorNeeded4, floorNeeded]

                elif fourCurrCloser: # floorNeeded4 is 2nd closest
                    oneCurrNext = oneCurrentDif < twoCurrentDif
                    twoCurrNext = oneCurrentDif > twoCurrentDif
                    if oneCurrNext: # floorNeeded is 2nd farthest
                        return [floorNeeded3, floorNeeded4, floorNeeded, floorNeeded2]
                    elif twoCurrNext: # floorNeeded2 is 2nd farthest
                        return [floorNeeded3, floorNeeded4, floorNeeded2, floorNeeded]

            elif fourCurrClosest: # floorNeeded4 is closest
                oneCurrCloser = (oneCurrentDif < twoCurrentDif) and (oneCurrentDif < threeCurrentDif)
                twoCurrCloser = (twoCurrentDif < oneCurrentDif) and (twoCurrentDif < threeCurrentDif)
                threeCurrCloser = (threeCurrentDif < oneCurrentDif) and (threeCurrentDif < twoCurrentDif)
                if oneCurrCloser: # floorNeeded is 2nd closest
                    twoCurrNext = twoCurrentDif < threeCurrentDif
                    threeCurrNext = twoCurrentDif > threeCurrentDif
                    if twoCurrNext: # floorNeeded2 is 2nd farthest
                        return [floorNeeded4, floorNeeded, floorNeeded2, floorNeeded3]
                    elif threeCurrNext: # floorNeeded3 is 2nd farthest
                        return [floorNeeded4, floorNeeded, floorNeeded3, floorNeeded2]

                elif twoCurrCloser: # floorNeeded2 is 2nd closest
                    oneCurrNext = oneCurrentDif < threeCurrentDif
                    threeCurrNext = oneCurrentDif > threeCurrentDif
                    if oneCurrNext: # floorNeeded is 2nd farthest
                        return [floorNeeded4, floorNeeded2, floorNeeded, floorNeeded3]
                    elif threeCurrNext: # floorNeeded3 is 2nd farthest
                        return [floorNeeded4, floorNeeded2, floorNeeded3, floorNeeded]

                elif threeCurrCloser: # floorNeeded3 is 2nd closest
                    oneCurrNext = oneCurrentDif < twoCurrentDif
                    twoCurrNext = oneCurrentDif > twoCurrentDif
                    if oneCurrNext: # floorNeeded is 2nd farthest
                        return [floorNeeded4, floorNeeded3, floorNeeded, floorNeeded2]
                    elif twoCurrNext: # floorNeeded2 is 2nd farthest
                        return [floorNeeded4, floorNeeded3, floorNeeded2, floorNeeded]

        elif above1 and above2 and above3 and above4: # currentFloor is above all floors needed
            oneCurrClosest = (current1Dif < current2Dif) and (current1Dif < current3Dif) and (current1Dif < current4Dif)
            twoCurrClosest = (current2Dif < current1Dif) and (current2Dif < current3Dif) and (current2Dif < current4Dif)
            threeCurrClosest = (current3Dif < current1Dif) and (current3Dif < current2Dif) and (current3Dif < current4Dif)
            fourCurrClosest = (current4Dif < current1Dif) and (current4Dif < current2Dif) and (current4Dif < current3Dif)

            if oneCurrClosest: # floorNeeded is closest
                twoCurrCloser = (current2Dif < current3Dif) and (current2Dif < current4Dif)
                threeCurrCloser = (current3Dif < current2Dif) and (current3Dif < current4Dif)
                fourCurrCloser = (current4Dif < current2Dif) and (current4Dif < current3Dif)
                if twoCurrCloser: # floorNeeded2 is 2nd closest
                    threeCurrNext = current3Dif < current4Dif
                    fourCurrNext = current3Dif > current4Dif
                    if threeCurrNext: # floorNeeded3 is 2nd farthest
                        return [floorNeeded, floorNeeded2, floorNeeded3, floorNeeded4]
                    elif fourCurrNext: # floorNeeded4 is 2nd farthest
                        return [floorNeeded, floorNeeded2, floorNeeded4, floorNeeded3]

                elif threeCurrCloser: # floorNeeded3 is 2nd closest
                    twoCurrNext = current2Dif < current4Dif
                    fourCurrNext = current2Dif > current4Dif
                    if twoCurrNext: # floorNeeded2 is 2nd farthest
                        return [floorNeeded, floorNeeded3, floorNeeded2, floorNeeded4]
                    elif fourCurrNext: # floorNeeded4 is 2nd farthest
                        return [floorNeeded, floorNeeded3, floorNeeded4, floorNeeded2]

                elif fourCurrCloser: # floorNeeded4 is 2nd closest
                    twoCurrNext = current2Dif < current3Dif
                    threeCurrNext = current2Dif > current3Dif
                    if twoCurrNext:
                        return [floorNeeded, floorNeeded4, floorNeeded2, floorNeeded3]
                    elif threeCurrNext:
                        return [floorNeeded, floorNeeded4, floorNeeded3, floorNeeded2]
            
            elif twoCurrClosest: # floorNeeded2 is closest
                oneCurrCloser = (current1Dif < current3Dif) and (current1Dif < current4Dif)
                threeCurrCloser = (current3Dif < current1Dif) and (current3Dif < current4Dif)
                fourCurrCloser = (current4Dif < current1Dif) and (current4Dif < current3Dif)
                if oneCurrCloser: # floorNeeded is 2nd closest
                    threeCurrNext = current3Dif < current4Dif
                    fourCurrNext = current3Dif > current4Dif
                    if threeCurrNext: # floorNeeded3 is 2nd farthest
                        return [floorNeeded2, floorNeeded, floorNeeded3, floorNeeded4]
                    elif fourCurrNext: # floorNeeded4 is 2nd farthest
                        return [floorNeeded2, floorNeeded, floorNeeded4, floorNeeded3]

                elif threeCurrCloser: # floorNeeded3 is 2nd closest
                    oneCurrNext = current1Dif < current4Dif
                    fourCurrNext = current1Dif > current4Dif
                    if oneCurrNext: # floorNeeded is 2nd farthest
                        return [floorNeeded2, floorNeeded3, floorNeeded, floorNeeded4]
                    elif fourCurrNext: # floorNeeded4 is 2nd farthest
                        return [floorNeeded2, floorNeeded3, floorNeeded4, floorNeeded]

                elif fourCurrCloser: # floorNeeded4 is 2nd closest
                    oneCurrNext = current1Dif < current3Dif
                    threeCurrNext = current1Dif > current3Dif
                    if oneCurrNext: # floorNeeded is 2nd farthest
                        return [floorNeeded2, floorNeeded4, floorNeeded, floorNeeded3]
                    elif threeCurrNext: # floorNeeded3 is 2nd farthest
                        return [floorNeeded2, floorNeeded4, floorNeeded3, floorNeeded]
            
            elif threeCurrClosest: # floorNeeded3 is closest
                oneCurrCloser = (current1Dif < current2Dif) and (current1Dif < current4Dif)
                twoCurrCloser = (current2Dif < current1Dif) and (current2Dif < current4Dif)
                fourCurrCloser = (current4Dif < current1Dif) and (current4Dif < current2Dif)
                if oneCurrCloser: # floorNeeded is 2nd closest
                    twoCurrNext = current2Dif < current4Dif
                    fourCurrNext = current2Dif > current4Dif
                    if twoCurrNext: # floorNeeded2 is 2nd farthest
                        return [floorNeeded3, floorNeeded, floorNeeded2, floorNeeded4]
                    elif fourCurrNext: # floorNeeded4 is 2nd farthest
                        return [floorNeeded3, floorNeeded, floorNeeded4, floorNeeded2]

                elif twoCurrCloser: # floorNeeded2 is 2nd closest
                    oneCurrNext = current1Dif < current4Dif
                    fourCurrNext = current1Dif > current4Dif
                    if oneCurrNext: # floorNeeded is 2nd farthest
                        return [floorNeeded3, floorNeeded2, floorNeeded, floorNeeded4]
                    elif fourCurrNext: # floorNeeded4 is 2nd farthest
                        return [floorNeeded3, floorNeeded2, floorNeeded4, floorNeeded]

                elif fourCurrCloser: # floorNeeded4 is 2nd closest
                    oneCurrNext = current1Dif < current2Dif
                    twoCurrNext = current1Dif > current2Dif
                    if oneCurrNext: # floorNeeded is 2nd farthest
                        return [floorNeeded3, floorNeeded4, floorNeeded, floorNeeded2]
                    elif twoCurrNext: # floorNeeded2 is 2nd farthest
                        return [floorNeeded3, floorNeeded4, floorNeeded2, floorNeeded]

            elif fourCurrClosest: # floorNeeded4 is closest
                oneCurrCloser = (current1Dif < current2Dif) and (current1Dif < current3Dif)
                twoCurrCloser = (current2Dif < current1Dif) and (current2Dif < current3Dif)
                threeCurrCloser = (current3Dif < current1Dif) and (current3Dif < current2Dif)
                if oneCurrCloser: # floorNeeded is 2nd closest
                    twoCurrNext = current2Dif < current3Dif
                    threeCurrNext = current2Dif > current3Dif
                    if twoCurrNext: # floorNeeded2 is 2nd farthest
                        return [floorNeeded4, floorNeeded, floorNeeded2, floorNeeded3]
                    elif threeCurrNext: # floorNeeded3 is 2nd farthest
                        return [floorNeeded4, floorNeeded, floorNeeded3, floorNeeded2]

                elif twoCurrCloser: # floorNeeded2 is 2nd closest
                    oneCurrNext = current1Dif < current3Dif
                    threeCurrNext = current1Dif > current3Dif
                    if oneCurrNext: # floorNeeded is 2nd farthest
                        return [floorNeeded4, floorNeeded2, floorNeeded, floorNeeded3]
                    elif threeCurrNext: # floorNeeded3 is 2nd farthest
                        return [floorNeeded4, floorNeeded2, floorNeeded3, floorNeeded]

                elif threeCurrCloser: # floorNeeded3 is 2nd closest
                    oneCurrNext = current1Dif < current2Dif
                    twoCurrNext = current1Dif > current2Dif
                    if oneCurrNext: # floorNeeded is 2nd farthest
                        return [floorNeeded4, floorNeeded3, floorNeeded, floorNeeded2]
                    elif twoCurrNext: # floorNeeded2 is 2nd farthest
                        return [floorNeeded4, floorNeeded3, floorNeeded2, floorNeeded]

def efficient(currentFloor, floorNeeded, floorNeeded2, floorNeeded3=None, floorNeeded4=None):
    if floorNeeded3 == None and floorNeeded4 == None: # 2 floor requests
        closest = closestFloor(currentFloor, floorNeeded, floorNeeded2)
        currentFloor = execute(currentFloor, closest[0], closest[1])
    elif floorNeeded4 == None: # 3 floor requests
        closest = closestFloor(currentFloor, floorNeeded, floorNeeded2, floorNeeded3)
        currentFloor = execute(currentFloor, closest[0], closest[1], closest[2])
    else: # 4 floor requests
        closest = closestFloor(currentFloor, floorNeeded, floorNeeded2, floorNeeded3, floorNeeded4)
        currentFloor = execute(currentFloor, closest[0], closest[1], closest[2], closest[3])
    return currentFloor

# Either runs execute function directly (if floors are in opposite directions)
#   or runs efficient function (if all needed floors are in one direction)
def floorReq(currentFloor, floorNeeded, floorNeeded2=None, floorNeeded3=None, floorNeeded4=None):
    if floorNeeded2 == None and floorNeeded3 == None and floorNeeded4 == None: # 1 floor request
        currentFloor = execute(currentFloor, floorNeeded)

    elif floorNeeded3 == None and floorNeeded4 == None: # 2 floor requests
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

# -------------------- Main Function -------------------- #
def main():
    howToUse()
    currentFloor = 1
    keepGoing = True
    while keepGoing:
        floor = input("Which floor do you need?: ") # Receive user input
        if not isValidUserInput(floor): # If invalid input, try again
            userError()
            keepGoing = True
            continue
        elif floor == 'quit': # If input is the word 'quit', shut down the loop
            print("Elevator shutting down...")
            keepGoing = False
            continue
        else: # Is valid input
            intFloor = int(floor)
            try: # One floor request
                closeDoor(10)
                currentFloor = floorReq(currentFloor, intFloor)
            except KeyboardInterrupt: # 2 floor requests
                floor2 = input("Which other floor do you need?: ")
                while not isValidUserInput(floor): # Keep trying if invalid input here
                    userError()
                    floor2 = input("Which other floor do you need?: ")
                else:
                    intFloor2 = int(floor2)
                    try:
                        closeDoor(5)
                        currentFloor = floorReq(currentFloor, intFloor, intFloor2)
                    except KeyboardInterrupt: # 3rd floor request
                        floor3 = input("Which other floor do you need?: ")
                        while not isValidUserInput(floor3):
                            userError()
                            floor3 = input("Which other floor do you need?: ")
                        else:
                            intFloor3 = int(floor3)
                            try:
                                closeDoor(5)
                                currentFloor = floorReq(currentFloor, intFloor, intFloor2, intFloor3)
                            except KeyboardInterrupt: # 4th - and final - floor request
                                floor4 = input("Which other floor do you need?: ")
                                while not isValidUserInput(floor4):
                                    userError()
                                    floor4 = input("Which other floor do you need?: ")
                                else:
                                    intFloor4 = int(floor4)
                                    closeDoor()
                                    currentFloor = floorReq(currentFloor, intFloor, intFloor2, intFloor3, intFloor4)

main()