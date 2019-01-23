import math
from functools import reduce 

inputList = input("Please enter a comma separated list of numbers to calculate mean, standard deviation, median, n-quartil and n-percentil\n")

inputArray = inputList.split(",")
numberArray = []

for x in inputArray:
    try:
        n=float(x)
        numberArray.append(n)
    except ValueError:
        print ("There is an invalid value ('"+str(x)+"') somewhere in the input, please make sure all input values are numbers ")
        quit()

numberArray.sort()

print (numberArray)

def calcMean(numberList):
    sum = reduce(lambda a,b:float(a)+float(b), numberList)
    return sum/len(numberList)

def calcStdDev(numberList):
    mean = calcMean(numberList)
    sigma = 0
    for num in numberList:
        diffSqr = (float(num) - mean)**2
        sigma += diffSqr
    div = sigma / len(numberList)
    return math.sqrt(div)

def calcMedian(numberList):
    if (len(numberList)%2==0):
        return (numberList[int((len(numberList)-1)/2)] + numberList[int((len(numberList)-1)/2)+1]) /2 
    else:
        return numberList[int((len(numberList)-1)/2)] 

print(calcMean(numberArray))
print(calcStdDev(numberArray))
print(calcMedian(numberArray))