# Modules
from re import search
from HelperFunctions import *

class Elvtr:
    def __init__(self): # Default currentFloor: 1
        self.currentFloor = 1

    def getCurrentFloor(self):
        return self.currentFloor

    def setCurrentFloor(self, currentFloor):
        self.currentFloor = currentFloor
    
    # Receives and returns user input
    def getUserInput(self):
        return input("Which floor do you need?: ")

    # Checks if floors go opposite directions from currentFloor; returns True or False
    def areOppositeDirections(self, currentFloor, floorNeeded, floorNeeded2, *floorsNeeded):
        if len(floorsNeeded) == 0: # 2 floors contrasted
            # Describe position of a floor relative to currentFloor #
            current1Dif = currentFloor - floorNeeded # Current floor above first floor needed
            current2Dif = currentFloor - floorNeeded2 # Current floor above second floor needed
            below1 = current1Dif < 0
            above1 = current1Dif > 0
            below2 = current2Dif < 0
            above2 = current2Dif > 0
            a1B2 = above1 and below2
            b1A2 = below1 and above2
            if (not b1A2) and (not a1B2): # If both floorsNeeded above or below currentFloor
                return False
            else:
                return True

        elif len(floorsNeeded) == 1: # 3 floors contrasted
            # Describe position of floor relative to currentFloor
            current1Dif = currentFloor - floorNeeded # Current floor above first floor needed
            current2Dif = currentFloor - floorNeeded2 # Current floor above second floor needed
            current3Dif = currentFloor - floorsNeeded[0] # Current floor above third floor needed
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

            # Conditional
            notBelowOrAbovePt1 = (not b1B2A3) and (not b1A2B3) and (not a1B2B3)
            notBelowOrAbovePt2 = (not b1A2A3) and (not a1A2B3) and (not a1B2A3)
            if notBelowOrAbovePt1 and notBelowOrAbovePt2:
                return False
            else:
                return True

        elif len(floorsNeeded) == 2: # 4 floors contrasted
            # Describe position of a floor relative to the currentFloor
            current1Dif = currentFloor - floorNeeded # Current floor above first floor needed
            current2Dif = currentFloor - floorNeeded2 # Current floor above second floor needed
            current3Dif = currentFloor - floorsNeeded[0] # Current floor above third floor needed
            current4Dif = currentFloor - floorsNeeded[1] # Current floor above fourth floor needed
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

    # Returns tuple w/ floors in order of closeness to currentFloor
    def closestFloor(currentFloor, floorNeeded, floorNeeded2, *floorsNeeded):
        if len(floorsNeeded) == 0: # 2 floors contrasted
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
                oneCurrCloser = oneCurrentDif < twoCurrentDif
                twoCurrCloser = oneCurrentDif > twoCurrentDif # 2nd floor is closer
                if twoCurrCloser:
                    return (floorNeeded2, floorNeeded)
                elif oneCurrCloser: # If 1st requested floor closer, return it
                    return (floorNeeded, floorNeeded2)

            elif above1 and above2: # If current floor above both requested floors
                currOneCloser = current1Dif < current2Dif # 1st floor is closer
                currTwoCloser = current1Dif > current2Dif # 2nd floor is closer
                if currTwoCloser: # If 2nd floor requested closer, return it
                    return (floorNeeded2, floorNeeded)
                elif currOneCloser: # If 1st floor requested closer, return it
                    return (floorNeeded, floorNeeded2)

        elif len(floorsNeeded) == 1: # 3 floors contrasted
            floorNeeded3 = floorsNeeded[0]
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
                        return (floorNeeded, floorNeeded2, floorNeeded3)
                    elif threeCurrCloser: # floorNeeded3 is next closest
                        return (floorNeeded, floorNeeded3, floorNeeded2)

                elif twoCurrClosest: # floorNeeded2 is closest
                    oneCurrCloser = oneCurrentDif < threeCurrentDif
                    threeCurrCloser = oneCurrentDif > threeCurrentDif
                    if oneCurrCloser: # floorNeeded is next closest
                        return (floorNeeded2, floorNeeded, floorNeeded3)
                    elif threeCurrCloser: # floorNeeded3 is next closest
                        return (floorNeeded2, floorNeeded3, floorNeeded)

                elif threeCurrClosest: # floorNeeded3 is closest
                    oneCurrCloser = oneCurrentDif < twoCurrentDif
                    twoCurrCloser = oneCurrentDif > twoCurrentDif
                    if oneCurrCloser: # floorNeeded is next closest
                        return (floorNeeded3, floorNeeded, floorNeeded2)
                    elif twoCurrCloser: # floorNeeded2 is next closest
                        return (floorNeeded3, floorNeeded2, floorNeeded)

            elif above1 and above2 and above3: # If currentFloor above all requested floors
                oneCurrClosest = (current1Dif < current2Dif) and (current1Dif < current3Dif)
                twoCurrClosest = (current2Dif < current1Dif) and (current2Dif < current3Dif)
                threeCurrClosest = (current3Dif < current1Dif) and (current3Dif < current2Dif)

                if oneCurrClosest: # floorNeeded is closest
                    twoCurrCloser = current2Dif < current3Dif
                    threeCurrCloser = current2Dif > current3Dif
                    if twoCurrCloser: # floorNeeded2 is next closest
                        return (floorNeeded, floorNeeded2, floorNeeded3)
                    elif threeCurrCloser: # floorNeeded3 is next closest
                        return (floorNeeded, floorNeeded3, floorNeeded2)

                elif twoCurrClosest: # floorNeeded2 is closest
                    oneCurrCloser = current1Dif < current3Dif
                    threeCurrCloser = current1Dif > current3Dif
                    if oneCurrCloser: # floorNeeded is next closest
                        return (floorNeeded2, floorNeeded, floorNeeded3)
                    elif threeCurrCloser: # floorNeeded3 is next closest
                        return (floorNeeded2, floorNeeded3, floorNeeded)

                elif threeCurrClosest: # floorNeeded3 is closest
                    oneCurrCloser = current1Dif < current2Dif
                    twoCurrCloser = current1Dif > current2Dif
                    if oneCurrCloser: # floorNeeded is next closest
                        return (floorNeeded3, floorNeeded, floorNeeded2)
                    elif twoCurrCloser: # floorNeeded2 is next closest
                        return (floorNeeded3, floorNeeded2, floorNeeded)

        elif len(floorsNeeded) == 2: # 4 floors contrasted
            floorNeeded3 = floorsNeeded[0]
            floorNeeded4 = floorsNeeded[1]

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
                            return (floorNeeded, floorNeeded2, floorNeeded3, floorNeeded4)
                        elif fourCurrNext: # floorNeeded4 is 2nd farthest
                            return (floorNeeded, floorNeeded2, floorNeeded4, floorNeeded3)

                    elif threeCurrCloser: # floorNeeded3 is 2nd closest
                        twoCurrNext = twoCurrentDif < fourCurrentDif
                        fourCurrNext = twoCurrentDif > fourCurrentDif
                        if twoCurrNext: # floorNeeded2 is 2nd farthest
                            return (floorNeeded, floorNeeded3, floorNeeded2, floorNeeded4)
                        elif fourCurrNext: # floorNeeded4 is 2nd farthest
                            return (floorNeeded, floorNeeded3, floorNeeded4, floorNeeded2)

                    elif fourCurrCloser: # floorNeeded4 is 2nd closest
                        twoCurrNext = twoCurrentDif < threeCurrentDif
                        threeCurrNext = twoCurrentDif > threeCurrentDif
                        if twoCurrNext:
                            return (floorNeeded, floorNeeded4, floorNeeded2, floorNeeded3)
                        elif threeCurrNext:
                            return (floorNeeded, floorNeeded4, floorNeeded3, floorNeeded2)

                elif twoCurrClosest: # floorNeeded2 is closest
                    oneCurrCloser = (oneCurrentDif < threeCurrentDif) and (oneCurrentDif < fourCurrentDif)
                    threeCurrCloser = (threeCurrentDif < oneCurrentDif) and (threeCurrentDif < fourCurrentDif)
                    fourCurrCloser = (fourCurrentDif < oneCurrentDif) and (fourCurrentDif < threeCurrentDif)
                    if oneCurrCloser: # floorNeeded is 2nd closest
                        threeCurrNext = threeCurrentDif < fourCurrentDif
                        fourCurrNext = threeCurrentDif > fourCurrentDif
                        if threeCurrNext: # floorNeeded3 is 2nd farthest
                            return (floorNeeded2, floorNeeded, floorNeeded3, floorNeeded4)
                        elif fourCurrNext: # floorNeeded4 is 2nd farthest
                            return (floorNeeded2, floorNeeded, floorNeeded4, floorNeeded3)

                    elif threeCurrCloser: # floorNeeded3 is 2nd closest
                        oneCurrNext = oneCurrentDif < fourCurrentDif
                        fourCurrNext = oneCurrentDif > fourCurrentDif
                        if oneCurrNext: # floorNeeded is 2nd farthest
                            return (floorNeeded2, floorNeeded3, floorNeeded, floorNeeded4)
                        elif fourCurrNext: # floorNeeded4 is 2nd farthest
                            return (floorNeeded2, floorNeeded3, floorNeeded4, floorNeeded)

                    elif fourCurrCloser: # floorNeeded4 is 2nd closest
                        oneCurrNext = oneCurrentDif < threeCurrentDif
                        threeCurrNext = oneCurrentDif > threeCurrentDif
                        if oneCurrNext: # floorNeeded is 2nd farthest
                            return (floorNeeded2, floorNeeded4, floorNeeded, floorNeeded3)
                        elif threeCurrNext: # floorNeeded3 is 2nd farthest
                            return (floorNeeded2, floorNeeded4, floorNeeded3, floorNeeded)

                elif threeCurrClosest: # floorNeeded3 is closest
                    oneCurrCloser = (oneCurrentDif < twoCurrentDif) and (oneCurrentDif < fourCurrentDif)
                    twoCurrCloser = (twoCurrentDif < oneCurrentDif) and (twoCurrentDif < fourCurrentDif)
                    fourCurrCloser = (fourCurrentDif < oneCurrentDif) and (fourCurrentDif < twoCurrentDif)
                    if oneCurrCloser: # floorNeeded is 2nd closest
                        twoCurrNext = twoCurrentDif < fourCurrentDif
                        fourCurrNext = twoCurrentDif > fourCurrentDif
                        if twoCurrNext: # floorNeeded2 is 2nd farthest
                            return (floorNeeded3, floorNeeded, floorNeeded2, floorNeeded4)
                        elif fourCurrNext: # floorNeeded4 is 2nd farthest
                            return (floorNeeded3, floorNeeded, floorNeeded4, floorNeeded2)

                    elif twoCurrCloser: # floorNeeded2 is 2nd closest
                        oneCurrNext = oneCurrentDif < fourCurrentDif
                        fourCurrNext = oneCurrentDif > fourCurrentDif
                        if oneCurrNext: # floorNeeded is 2nd farthest
                            return (floorNeeded3, floorNeeded2, floorNeeded, floorNeeded4)
                        elif fourCurrNext: # floorNeeded4 is 2nd farthest
                            return (floorNeeded3, floorNeeded2, floorNeeded4, floorNeeded)

                    elif fourCurrCloser: # floorNeeded4 is 2nd closest
                        oneCurrNext = oneCurrentDif < twoCurrentDif
                        twoCurrNext = oneCurrentDif > twoCurrentDif
                        if oneCurrNext: # floorNeeded is 2nd farthest
                            return (floorNeeded3, floorNeeded4, floorNeeded, floorNeeded2)
                        elif twoCurrNext: # floorNeeded2 is 2nd farthest
                            return (floorNeeded3, floorNeeded4, floorNeeded2, floorNeeded)

                elif fourCurrClosest: # floorNeeded4 is closest
                    oneCurrCloser = (oneCurrentDif < twoCurrentDif) and (oneCurrentDif < threeCurrentDif)
                    twoCurrCloser = (twoCurrentDif < oneCurrentDif) and (twoCurrentDif < threeCurrentDif)
                    threeCurrCloser = (threeCurrentDif < oneCurrentDif) and (threeCurrentDif < twoCurrentDif)
                    if oneCurrCloser: # floorNeeded is 2nd closest
                        twoCurrNext = twoCurrentDif < threeCurrentDif
                        threeCurrNext = twoCurrentDif > threeCurrentDif
                        if twoCurrNext: # floorNeeded2 is 2nd farthest
                            return (floorNeeded4, floorNeeded, floorNeeded2, floorNeeded3)
                        elif threeCurrNext: # floorNeeded3 is 2nd farthest
                            return (floorNeeded4, floorNeeded, floorNeeded3, floorNeeded2)

                    elif twoCurrCloser: # floorNeeded2 is 2nd closest
                        oneCurrNext = oneCurrentDif < threeCurrentDif
                        threeCurrNext = oneCurrentDif > threeCurrentDif
                        if oneCurrNext: # floorNeeded is 2nd farthest
                            return (floorNeeded4, floorNeeded2, floorNeeded, floorNeeded3)
                        elif threeCurrNext: # floorNeeded3 is 2nd farthest
                            return (floorNeeded4, floorNeeded2, floorNeeded3, floorNeeded)

                    elif threeCurrCloser: # floorNeeded3 is 2nd closest
                        oneCurrNext = oneCurrentDif < twoCurrentDif
                        twoCurrNext = oneCurrentDif > twoCurrentDif
                        if oneCurrNext: # floorNeeded is 2nd farthest
                            return (floorNeeded4, floorNeeded3, floorNeeded, floorNeeded2)
                        elif twoCurrNext: # floorNeeded2 is 2nd farthest
                            return (floorNeeded4, floorNeeded3, floorNeeded2, floorNeeded)

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
                            return (floorNeeded, floorNeeded2, floorNeeded3, floorNeeded4)
                        elif fourCurrNext: # floorNeeded4 is 2nd farthest
                            return (floorNeeded, floorNeeded2, floorNeeded4, floorNeeded3)

                    elif threeCurrCloser: # floorNeeded3 is 2nd closest
                        twoCurrNext = current2Dif < current4Dif
                        fourCurrNext = current2Dif > current4Dif
                        if twoCurrNext: # floorNeeded2 is 2nd farthest
                            return (floorNeeded, floorNeeded3, floorNeeded2, floorNeeded4)
                        elif fourCurrNext: # floorNeeded4 is 2nd farthest
                            return (floorNeeded, floorNeeded3, floorNeeded4, floorNeeded2)

                    elif fourCurrCloser: # floorNeeded4 is 2nd closest
                        twoCurrNext = current2Dif < current3Dif
                        threeCurrNext = current2Dif > current3Dif
                        if twoCurrNext:
                            return (floorNeeded, floorNeeded4, floorNeeded2, floorNeeded3)
                        elif threeCurrNext:
                            return (floorNeeded, floorNeeded4, floorNeeded3, floorNeeded2)

                elif twoCurrClosest: # floorNeeded2 is closest
                    oneCurrCloser = (current1Dif < current3Dif) and (current1Dif < current4Dif)
                    threeCurrCloser = (current3Dif < current1Dif) and (current3Dif < current4Dif)
                    fourCurrCloser = (current4Dif < current1Dif) and (current4Dif < current3Dif)
                    if oneCurrCloser: # floorNeeded is 2nd closest
                        threeCurrNext = current3Dif < current4Dif
                        fourCurrNext = current3Dif > current4Dif
                        if threeCurrNext: # floorNeeded3 is 2nd farthest
                            return (floorNeeded2, floorNeeded, floorNeeded3, floorNeeded4)
                        elif fourCurrNext: # floorNeeded4 is 2nd farthest
                            return (floorNeeded2, floorNeeded, floorNeeded4, floorNeeded3)

                    elif threeCurrCloser: # floorNeeded3 is 2nd closest
                        oneCurrNext = current1Dif < current4Dif
                        fourCurrNext = current1Dif > current4Dif
                        if oneCurrNext: # floorNeeded is 2nd farthest
                            return (floorNeeded2, floorNeeded3, floorNeeded, floorNeeded4)
                        elif fourCurrNext: # floorNeeded4 is 2nd farthest
                            return (floorNeeded2, floorNeeded3, floorNeeded4, floorNeeded)

                    elif fourCurrCloser: # floorNeeded4 is 2nd closest
                        oneCurrNext = current1Dif < current3Dif
                        threeCurrNext = current1Dif > current3Dif
                        if oneCurrNext: # floorNeeded is 2nd farthest
                            return (floorNeeded2, floorNeeded4, floorNeeded, floorNeeded3)
                        elif threeCurrNext: # floorNeeded3 is 2nd farthest
                            return (floorNeeded2, floorNeeded4, floorNeeded3, floorNeeded)

                elif threeCurrClosest: # floorNeeded3 is closest
                    oneCurrCloser = (current1Dif < current2Dif) and (current1Dif < current4Dif)
                    twoCurrCloser = (current2Dif < current1Dif) and (current2Dif < current4Dif)
                    fourCurrCloser = (current4Dif < current1Dif) and (current4Dif < current2Dif)
                    if oneCurrCloser: # floorNeeded is 2nd closest
                        twoCurrNext = current2Dif < current4Dif
                        fourCurrNext = current2Dif > current4Dif
                        if twoCurrNext: # floorNeeded2 is 2nd farthest
                            return (floorNeeded3, floorNeeded, floorNeeded2, floorNeeded4)
                        elif fourCurrNext: # floorNeeded4 is 2nd farthest
                            return (floorNeeded3, floorNeeded, floorNeeded4, floorNeeded2)

                    elif twoCurrCloser: # floorNeeded2 is 2nd closest
                        oneCurrNext = current1Dif < current4Dif
                        fourCurrNext = current1Dif > current4Dif
                        if oneCurrNext: # floorNeeded is 2nd farthest
                            return (floorNeeded3, floorNeeded2, floorNeeded, floorNeeded4)
                        elif fourCurrNext: # floorNeeded4 is 2nd farthest
                            return (floorNeeded3, floorNeeded2, floorNeeded4, floorNeeded)

                    elif fourCurrCloser: # floorNeeded4 is 2nd closest
                        oneCurrNext = current1Dif < current2Dif
                        twoCurrNext = current1Dif > current2Dif
                        if oneCurrNext: # floorNeeded is 2nd farthest
                            return (floorNeeded3, floorNeeded4, floorNeeded, floorNeeded2)
                        elif twoCurrNext: # floorNeeded2 is 2nd farthest
                            return (floorNeeded3, floorNeeded4, floorNeeded2, floorNeeded)

                elif fourCurrClosest: # floorNeeded4 is closest
                    oneCurrCloser = (current1Dif < current2Dif) and (current1Dif < current3Dif)
                    twoCurrCloser = (current2Dif < current1Dif) and (current2Dif < current3Dif)
                    threeCurrCloser = (current3Dif < current1Dif) and (current3Dif < current2Dif)
                    if oneCurrCloser: # floorNeeded is 2nd closest
                        twoCurrNext = current2Dif < current3Dif
                        threeCurrNext = current2Dif > current3Dif
                        if twoCurrNext: # floorNeeded2 is 2nd farthest
                            return (floorNeeded4, floorNeeded, floorNeeded2, floorNeeded3)
                        elif threeCurrNext: # floorNeeded3 is 2nd farthest
                            return (floorNeeded4, floorNeeded, floorNeeded3, floorNeeded2)

                    elif twoCurrCloser: # floorNeeded2 is 2nd closest
                        oneCurrNext = current1Dif < current3Dif
                        threeCurrNext = current1Dif > current3Dif
                        if oneCurrNext: # floorNeeded is 2nd farthest
                            return (floorNeeded4, floorNeeded2, floorNeeded, floorNeeded3)
                        elif threeCurrNext: # floorNeeded3 is 2nd farthest
                            return (floorNeeded4, floorNeeded2, floorNeeded3, floorNeeded)

                    elif threeCurrCloser: # floorNeeded3 is 2nd closest
                        oneCurrNext = current1Dif < current2Dif
                        twoCurrNext = current1Dif > current2Dif
                        if oneCurrNext: # floorNeeded is 2nd farthest
                            return (floorNeeded4, floorNeeded3, floorNeeded, floorNeeded2)
                        elif twoCurrNext: # floorNeeded2 is 2nd farthest
                            return (floorNeeded4, floorNeeded3, floorNeeded2, floorNeeded)

    def efficient(self, currentFloor, floorNeeded, floorNeeded2, *floorsNeeded):
        if len(floorsNeeded) == 0: # 2 floor requests
            closest = self.closestFloor(currentFloor, floorNeeded, floorNeeded2)
            currentFloor = self.execute(currentFloor, closest[0], closest[1])
        elif len(floorsNeeded) == 1: # 3 floor requests
            closest = self.closestFloor(currentFloor, floorNeeded, floorNeeded2, floorsNeeded[0])
            currentFloor = self.execute(currentFloor, closest[0], closest[1], closest[2])
        elif len(floorsNeeded) == 2: # 4 floor requests
            closest = self.closestFloor(currentFloor, floorNeeded, floorNeeded2, floorsNeeded[0], floorsNeeded[1])
            currentFloor = self.execute(currentFloor, closest[0], closest[1], closest[2], closest[3])
        return currentFloor
    
    # Opens and closes door for elevator; calls switchingFloors to move elevator
    def execute(self, currentFloor, floorNeeded, *floorsNeeded):
        closeDoor()
        currentFloor = self.switchingFloors(currentFloor, floorNeeded)
        openDoor(currentFloor)
        if len(floorsNeeded) > 0: # If more than one floor
            for floor in floorsNeeded:
                closeDoor()
                currentFloor = self.switchingFloors(currentFloor, floor)
                openDoor(currentFloor)
        return currentFloor
    

    # Moves elevator up or down; changes currentFloor
    def switchingFloors(self, currentFloor, floorNeeded):
        while currentFloor < floorNeeded: # currentFloor below floorNeeded
            print(f"Currently at floor {currentFloor}; Going up...")
            sleep(5)
            currentFloor += 1
        else:
            while currentFloor > floorNeeded: # currentFloor above floorNeeded
                print(f"Currently at floor {currentFloor}; Going down...")
                sleep(5)
                currentFloor -= 1
        return currentFloor
        
    """
    Sends floor request. Either runs execute function directly (if floors are in opposite directions)
       or runs efficient function (if all needed floors are in one direction)
    """
    def floorReq(self, currentFloor, floorNeeded, *floorsNeeded):
        if len(floorsNeeded) == 0: # 1 floor request
            currentFloor = self.execute(currentFloor, floorNeeded)
    
        elif len(floorsNeeded) == 1: # 2 floor requests
            are = self.areOppositeDirections(currentFloor, floorNeeded, floorsNeeded[0])
            if not are:
                currentFloor = self.efficient(currentFloor, floorNeeded, floorsNeeded[0])
            else:
                currentFloor = self.execute(currentFloor, floorNeeded, floorsNeeded[0])
    
        elif len(floorsNeeded) == 2: # 3 floor requests
            are = self.areOppositeDirections(currentFloor, floorNeeded, floorsNeeded[0], floorsNeeded[1])
            if not are:
                currentFloor = self.efficient(currentFloor, floorNeeded, floorsNeeded[0], floorsNeeded[1])
            else:
                currentFloor = self.execute(currentFloor, floorNeeded, floorsNeeded[0], floorsNeeded[1])
        
        elif len(floorsNeeded) == 3: # 4 floor requests
            are = self.areOppositeDirections(currentFloor, floorNeeded, floorsNeeded[0], floorsNeeded[1], floorsNeeded[2])
            if not are:
                currentFloor = self.efficient(currentFloor, floorNeeded, floorsNeeded[0], floorsNeeded[1], floorsNeeded[2])
            else:
                currentFloor = self.execute(currentFloor, floorNeeded, floorsNeeded[0], floorsNeeded[1], floorsNeeded[2])
        self.setCurrentFloor(currentFloor)

def main():
    howToUse()
    elvtr = Elvtr()
    keepGoing = True
    while keepGoing:
        floor = elvtr.getUserInput()
        if not isValidUserInput(floor):
            userError()
            keepGoing = True
            continue
        elif floor == 'quit':
            print("Elevator shutting down...")
            keepGoing = False
            continue
        else:
            # Variables
            floor2, floor3, floor4 = "", "", "" # Initiate next inputs to NoneValue...
            floors = [floor, floor2, floor3, floor4]
            emptyFloors = [floor2, floor3, floor4]
            intFloors = []

            for level in emptyFloors: # Receive input and change variable from NoneValue to empty string
                level = elvtr.getUserInput()
                while level == 'quit':
                    print("You already requested a floor. You must enter more now")
                    print("")
                    level = elvtr.getUserInput()
                while not isValidUserInput(level):
                    userError()
                    level = elvtr.getUserInput()
            for i in range(3): # Add floors to floors list
                floors[i + 1] = emptyFloors[i]
            for i in range(4): # Convert floors to integers
                if floors[i] != "":
                    intFloors[i] = int(floors[i])
            intLen = len(intFloors)
            if intLen == 1:
                currentFloor = elvtr.floorReq(currentFloor, intFloors[0])
            elif intLen == 2:
                currentFloor = elvtr.floorReq(currentFloor, intFloors[0], intFloors[1])
            elif intLen == 3:
                currentFloor = elvtr.floorReq(currentFloor, intFloors[0], intFloors[1], intFloors[2])
            elif intLen == 4:
                currentFloor = elvtr.floorReq(currentFloor, intFloors[0], intFloors[1], intFloors[2], intFloors[3])

if __name__ == '__main__':
    main()