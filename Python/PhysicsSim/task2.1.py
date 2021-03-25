import math


#box has 3 dimensions labeled x, y and z
#10 measurements have been done for each dimension, and they will be stored in a list
xMeasurements = [27.8, 28.0, 27.8, 28.1, 27.9, 27.7, 28.0, 27.9, 27.8, 28.1]
yMeasurements = [19.8, 20.0, 19.9, 19.7, 19.7, 20.2, 20.1, 19.9, 20.1, 20.0]
zMeasurements = [10.0, 9.9, 10.2, 10.1, 10.1, 9.9, 10.0, 9.8, 10.2, 9.9]


sumOfNums = 0
counter = 0
for x in xMeasurements:
    sumOfNums = sumOfNums + x
    counter = counter + 1
meanX = sumOfNums / counter

sumOfNums = 0
counter = 0
for y in yMeasurements:
    sumOfNums = sumOfNums + y
    counter = counter + 1
meanY = sumOfNums / counter

sumOfNums = 0
counter = 0
for z in zMeasurements:
    sumOfNums = sumOfNums + z
    counter = counter + 1
meanZ = sumOfNums / counter

#print("meanX: {}, meanY: {}, meanZ: {}".format(round(meanX, 2), round(meanY, 2), round(meanZ, 2)))

#obtaining the uncertainty for each of the dimensions
N = 10

sumOfElements = 0
for i in xMeasurements:
    sumOfElements = sumOfElements + math.pow((i - meanX), 2)

res = math.sqrt((1/N*(N - 1)) * sumOfElements)
sigmaX = res

sumOfElements = 0
for i in yMeasurements:
    sumOfElements = sumOfElements + math.pow((i - meanY), 2)

res = math.sqrt((1/N*(N - 1)) * sumOfElements)
sigmaY = res

sumOfElements = 0
for i in zMeasurements:
    sumOfElements = sumOfElements + math.pow((i - meanZ), 2)

res = math.sqrt((1/N*(N - 1)) * sumOfElements)
sigmaZ = res

print(sigmaX, sigmaY, sigmaZ)



#getting the uncertainty of the volume
VderX = meanY * meanZ  #the derived formula of volume with respect to x
VderY = meanX * meanZ
VderZ = meanX * meanY


a = ((meanY * meanZ)**2 * sigmaX**2)
b = ((meanX * meanZ)**2 * sigmaY**2)
c = ((meanX * meanY)**2 * sigmaZ**2)

res = math.sqrt(a + b + c)
print(res)
print(meanZ)