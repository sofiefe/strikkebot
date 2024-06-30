# This will be the script for calculating increases and decreases in the round for a knitting project
# Based on https://hobbyhygge.com/nb/strikkekalkulator

# This script will have some main functions:
# The first function takes two inputs; current amount of stiches, and wanted amount of stiches
# It will return the instructions to increase/decrease
# The instructions will have the format:
# [[knitXstiches, Y=-1 for decrease or Y=1 for increase, repeatZtimes]]
# the list can contains multiple instructions.
# Second function wil print a step-by-step interactive guide to help keeping track of the decreases

def calculateIncDec(currentStiches, wantedStitches):
    a = currentStiches
    b = wantedStitches
    instructions = []
    y = 1
    diff = b - a
    z = abs(diff)
    modulo = a % z
    x = a // z
    if (diff < 0):
        y = -1
        x -= 2
    if (modulo == 0):
        instructions.append([x, y, z])
        return instructions
    first = [x, y, z-modulo]
    second = [x+1, y, modulo]
    instructions.append(first)
    instructions.append(second)
    return instructions



    
