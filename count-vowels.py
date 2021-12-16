import random


def getCharacters(lower, upper, numberOfCharacters, arr=[]):
    for _ in range(numberOfCharacters):
        arr.append(chr(random.randint(lower, upper)))
    return arr


def reducedArray(array, checkArray, result={}):
    for element in array:
        if element in checkArray:
            try:
                result[element] = result[element] + 1
            except:
                result[element] = 1
    return result


def getTotalCount(object, total=0):
    for key in object:
        total += object[key]
    return total


characters = getCharacters(97, 122, 100)

vowels = ['a', 'e', 'i', 'o', 'u']
print(characters)
vowelsCount = reducedArray(characters, vowels)
print(vowelsCount)
count = getTotalCount(vowelsCount)
print(count)
