def lowest():
    print(f"Which is the lowest?")

def numbers():
    firstNumber = float(input("First Number: \n >"))
    secondNumber = float(input("Second Number: \n >"))
    thirdNumber = float(input("Third NUmber: \n >"))
    return firstNumber, secondNumber, thirdNumber

lowest()
firstGiven, secondGiven, thirdGiven = numbers()
if thirdGiven > firstGiven <= secondGiven:
    print(f"The lowest number is {firstGiven}.")
elif thirdGiven >= secondGiven < firstGiven:
    print(f"The lowest number is {secondGiven}.")
elif secondGiven > thirdGiven <= firstGiven:
    print(f"The lowest number is {thirdGiven}")
elif firstGiven == secondGiven == thirdGiven:
    print("The numbers are equal.")