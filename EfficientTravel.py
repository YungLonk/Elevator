from time import sleep
#EX...
# current floor is 3
# first floor needed is floor 2
# second floor needed is floor 5
# floor 5 request comming from floor 1 (requestingFloor = 4)

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

def closeDoor(sec=None): # Can be interrupted
    if sec == None:
        print("Closing doors...")
        sleep(2)
    else:
        print(f"Closing door in {sec} seconds...")
        sleep(sec)

def openDoor(currentFloor):
    print(f"Arrived at floor {currentFloor}; Opening doors...")
    sleep(4)

def execute(currentFloor, floorNeeded, otherFloorNeeded):
    closeDoor()
    while currentFloor != floorNeeded:
        currentFloor = switchingFloors(currentFloor, floorNeeded)
    else:
        currentFloor = switchingFloors(currentFloor, otherFloorNeeded)
    openDoor(currentFloor)
    return currentFloor


"""
In the future, the below function must be adapted to account for
which floors people are requesting from, not just where they need
to go
"""
def efficientTravel(currentFloor, floorNeeded1, floorNeeded2):
    current1Difference = currentFloor - floorNeeded1
    current2Difference = currentFloor - floorNeeded2
    oneCurrentDifference = floorNeeded1 - currentFloor
    twoCurrentDifference = floorNeeded2 - currentFloor
    if (current1Difference < 0) and (current2Difference < 0): # If current floor is lower than both requested floors...

        if abs(oneCurrentDifference) > abs(twoCurrentDifference): # If the first requested floor is farther away...
            currentFloor = execute(currentFloor, floorNeeded2, floorNeeded1) #... go to second requested floor first
            return currentFloor
        elif twoCurrentDifference > oneCurrentDifference: # If the second requested floor is farther away...
            currentFloor = execute(currentFloor, floorNeeded1, floorNeeded2)#... go to first requested floor first
            return currentFloor

    elif (current1Difference > 0) and (current2Difference > 0): # If currentFloor is greater than both requested floors

        if abs(current1Difference) > abs(current2Difference): # If the first requested floor is farther away...
            currentFloor = execute(currentFloor, floorNeeded2, floorNeeded1) #... go to second requested floor first
            return currentFloor
        elif abs(current1Difference) < abs(current2Difference): # If the second requested floor is farther away...
            currentFloor = execute(currentFloor, floorNeeded1, floorNeeded2) #... go to first requested floor first
            return currentFloor
    
    # currentFloor: 4
    # floorNeeded1: 2
    # floorNeeded2: 5
    elif (current1Difference > 0) and (current2Difference < 0): # If currentFloor greater than floorNeeded1 but not than floorNeeded2
        if abs(current1Difference) > abs(twoCurrentDifference): # If the first requested floor is farther away...
            currentFloor = execute(currentFloor, floorNeeded2, floorNeeded1)#... go to second requested floor first
            return currentFloor
        elif abs(current1Difference) < abs(twoCurrentDifference): # If the second requested floor is farther away...
            currentFloor = execute(currentFloor, floorNeeded1, floorNeeded2)#... go to first requested floor first
            return currentFloor

    elif (current1Difference < 0) and (current2Difference > 0): # If currentFloor less than floorNeeded1 but not than floorNeeded2
        if abs(oneCurrentDifference) > abs(current2Difference): # If the first requested floor is farther away...
            currentFloor = execute(currentFloor, floorNeeded2, floorNeeded1)
            return currentFloor
        elif abs(oneCurrentDifference) < abs(current2Difference): # If the second requested floor is farther away...
            currentFloor = execute(currentFloor, floorNeeded1, floorNeeded2)
            return currentFloor