# Necessary resources/modules
from Elevator import switchingFloors, execute, areOppositeDirections
from HelperFunctions import *

# currentFloor: 1, fromFloor: 1, floorNeeded: 3, fromFloor2: 4, floorNeeded2: 2
#     Order of travel: 3, 4, 2
# currentFloor: 3, fromFloor: 1, floorNeeded: 3, fromFloor2: 4, floorNeeded2: 2
#     Order of travel: 1, 3, 4, 2
# currentFloor: 2, fromFloor: 5, floorNeeded: 1, fromFloor2: 2, floorNeeded2: 4
#     Order of travel: 2, 4, 5, 1
# currentFloor: 3, fromFloor: 1, floorNeeded: 5, fromFloor2: 2, floorNeeded2: 5
#     Order of travel: 2, 1, 5
def efficient(currentFloor, fromFloor, fromFloor2, floorNeeded, floorNeeded2, fromFloor3=None, fromFloor4=None, floorNeeded3=None, floorNeeded4=None):
    noFloor3Or4 = (fromFloor3 == None) and (fromFloor4 == None)
    noFloor3Or4Needed = (floorNeeded3 == None) and (floorNeeded4 == None)
    if noFloor3Or4 and noFloor3Or4Needed: # 2 floor requests