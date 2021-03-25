import math

smallDiam = 0.5 #cm
smallDiamSigma = 0.1 #cm
smallLen = 0.1 #cm
smallLenSigma = 0.05 #cm

largeLen = [4.8, 4.7, 4.7, 4.8, 4.7, 4.6, 4.7, 4.8, 4.9, 4.7]
largeDiam = [1.4, 1.5, 1.4, 1.4, 1.3, 1.5, 1.5, 1.4, 1.4, 1.3]


N = 10
sumOfNums = 0

for i in largeLen:
    sumOfNums = sumOfNums + i

meanLargeLen = sumOfNums / N

N = 10
sumOfNums = 0

for i in largeDiam:
    sumOfNums = sumOfNums + i

meanLargeDiam = sumOfNums / N


N = 10
sumOfElements = 0

for i in largeLen:
    sumOfElements = sumOfElements + math.pow((i - meanLargeLen), 2)

largeLenSigma = math.sqrt((1/N*(N - 1)) * sumOfElements)

#print(largeLenSigma)

N = 10
sumOfElements = 0

for i in largeDiam:
    sumOfElements = sumOfElements + math.pow((i - meanLargeDiam), 2)

largeDiamSigma = math.sqrt((1/N*(N - 1)) * sumOfElements)

#print(largeDiamSigma)


smallRadius = smallDiam / 2
smallVolume = 2 * math.pi * smallRadius * smallLen
#print(smallVolume)

largeRadius = meanLargeDiam / 2
largeVolume = 2 * math.pi * largeRadius * meanLargeLen
#print(largeVolume)


largeVderR = 2 * math.pi * meanLargeLen
largeVderL = 2 * math.pi * largeRadius
largeRadiusSigma = largeDiamSigma / 2

sigmaLargeV = math.sqrt((math.pow(largeVderR, 2) * math.pow(largeRadiusSigma, 2)) +
                        (math.pow(largeVderL, 2) * math.pow(largeLenSigma, 2)))


smallVderR = 2 * math.pi * smallLen
smallVderL = 2 * math.pi * smallRadius
smallRadiusSigma = smallDiamSigma / 2

sigmaSmallV = math.sqrt((math.pow(smallVderR, 2) * math.pow(smallRadiusSigma, 2)) +
                        (math.pow(smallVderL, 2) * math.pow(smallLenSigma, 2)))

print(sigmaSmallV)