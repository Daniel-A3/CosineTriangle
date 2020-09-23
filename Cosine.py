# Welcome to Daniels Cosine rule calculator

#cosine rule for missing SIDE : a^2 = b^2 + c^2 - 2bcCos(A)

#cosine rule for missing ANGLE : Cos(A) = (b^2 + c^2 - a^2) / 2bc

import math

def missingAngle():
    sideA = float(input("size of side a = "))
    sideB = float(input("size of side b = "))
    sideC = float(input("size of side c = "))
    try:
        answer = math.acos((sideB**2 + sideC**2 - sideA**2) / (2 * sideB * sideC))
        return f'Your answer is: {math.degrees(answer):.2f} degrees'
    except ValueError:
        return 'Values given cannot form a triangle'

def missingSide():
    angleA = math.radians(float(input("size of angle A (degrees) = ")))
    sideB = float(input("size of side b = "))
    sideC = float(input("size of side c = "))

    answer = math.sqrt(sideB**2 + sideC**2 - 2 * sideB * sideC * math.cos(angleA))
    return f'Your answer is: {answer:.2f} units'


while True:
    missingSideOrAngle = input("Are you trying to work out the missing angle or side?(Angle/Side) = ")
    if missingSideOrAngle.title() == "Angle":
        print(missingAngle())

    elif missingSideOrAngle.title() == "Side":
        print(missingSide())

    else:
        missingSideOrAngle = input("Please enter a valid string(Angle/Side) = ")


