from time import sleep

def switchingFloors(currentFloor, floorNeeded): # Sends elevator to floor needed and returns the current floor
    while currentFloor < floorNeeded:
        print(f"Currently at floor {currentFloor}. Going up...")
        sleep(5)
        currentFloor += 1
    else:
        while currentFloor > floorNeeded:
            print(f"Currently at floor {currentFloor}. Going down...")
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
        openDoor(currentFloor)
        closeDoor()
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
    current1Dif = currentFloor - floorNeeded1 # Current floor above first floor needed
    current2Dif = currentFloor - floorNeeded2 # Current floor above second floor needed
    oneCurrentDif = floorNeeded1 - currentFloor # Current floor below first floor needed
    twoCurrentDif = floorNeeded2 - currentFloor # Current floor below second floor needed
    if (current1Dif < 0) and (current2Dif < 0): # If current floor is lower than both requested floors
        if oneCurrentDif > twoCurrentDif: # If the first requested floor is farther away...
            currentFloor = execute(currentFloor, floorNeeded2, floorNeeded1) # ...go to second requested floor first
            return currentFloor
        elif oneCurrentDif < twoCurrentDif: # Otherwise...
            currentFloor = execute(currentFloor, floorNeeded1, floorNeeded2)# ...go to first requested floor first
            return currentFloor

    elif (current1Dif > 0) and (current2Dif > 0): # If currentFloor is higher than both requested floors
        if current1Dif > current2Dif: # If the first requested floor is farther away...
            currentFloor = execute(currentFloor, floorNeeded2, floorNeeded1) # ...go to second requested floor first
            return currentFloor
        elif current1Dif < current2Dif: # Otherwise...
            currentFloor = execute(currentFloor, floorNeeded1, floorNeeded2) # ...go to first requested floor first
            return currentFloor