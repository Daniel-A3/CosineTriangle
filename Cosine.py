# Welcome to Daniels Cosine rule calculator

#cosine rule for missing SIDE : a^2 = b^2 + c^2 - 2bcCos(A)

#cosine rule for missing ANGLE : Cos(A) = (b^2 + c^2 - a^2) / 2bc

import math, sys

def missingAngle():
    sideA = int(input("size of side a = "))
    sideB = int(input("size of side b = "))
    sideC = int(input("size of side c = "))

    answer = math.cos((sideB**2 + sideC**2 - sideA**2) / 2 * sideB * sideC)

    return answer

def missingSide():
    angleA = int(input("size of angle A = "))
    sideB = int(input("size of side b = "))
    sideC = int(input("size of side c = "))

    answer = math.sqrt(sideB**2 + sideC**2 - 2 * sideB * sideC * math.cos(angleA))

    return answer

missingSideOrAngle = input("Are you trying to work out the missing angle or side?(Angle/Side) = ")

while True:
    if missingSideOrAngle.title() == "Angle":
        print("Your answer is = " + str(missingAngle()))
        sys.exit()

    elif missingSideOrAngle.title() == "Side":
        print("Your answer is = " + str(missingSide()))
        sys.exit()

    else:
        missingSideOrAngle = input("Please enter a valid string(Angle/Side) = ")


