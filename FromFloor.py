# Necessary resources/modules
from Elevator import switchingFloors, execute
from HelperFunctions import *

# fromFloor: 1, floorNeeded: 3, fromFloor2: , floorNeeded2: 2
def efficient(currentFloor, fromFloor, fromFloor2, floorNeeded, floorNeeded2, *fromAndNeeded):
    