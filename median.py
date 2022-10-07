"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""




import math
def checkEven():
    if len(numbers) % 2 == 0:
        numbersEven()
    else:
        numbersOdd()


def numbersEven():
    half = int(len(numbers)/2)
    sum = numbers[half] + numbers[half-1]
    printMedian(sum/2)


def numbersOdd():
    half = len(numbers)/2
    printMedian(numbers[math.floor(half)])


def printMedian(median):
    print(median)
    return median


while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
        numbers.sort()
        checkEven()
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
