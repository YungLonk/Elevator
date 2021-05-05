from time import sleep

def efficientTravel(currentFloor, floorNeeded1):
    if currentFloor != floorNeeded1:
        if currentFloor > floorNeeded1: # If going down...
            requestingFloor = input(f"Which floor is the person requesting floor {floorNeeded2} coming from?: ")
            if requestingFloor < floorNeeded1: # If the floor requested from is along the route to the first requested floor...

                # ...stop at that floor before floorNeeded1
                print("Closing doors...")
                sleep(2)
                while currentFloor != floor