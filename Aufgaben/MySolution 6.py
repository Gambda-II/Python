import random

import math

minValue = 0
maxValue = 1000
steps = 1

completeList = range(minValue, maxValue, steps)

samples = 20

unsortedList = random.sample(completeList, samples)
unsortedList = [4, 33, 7, 1, 23, 12]





def swap(list,firstIndex, secondIndex):
    left = list[firstIndex]
    right = list[secondIndex]

    list[firstIndex] = right
    list[secondIndex] = left

    #print(f"swapped position {firstIndex} and {secondIndex}")

    return list


def bubbleSort(listToSort):
    
    counter = 0

    print(listToSort)
    length = len(listToSort)

    if (length < 1):
        return listToSort

    for i in range(0, length - 1, 1):

        for j in range(0, length - i - 1 , 1):
        
            left = listToSort[j]
            right = listToSort[j + 1]

            if (right < left):
                listToSort = swap(listToSort, j, j + 1)
                counter += 1

    print(f"After {counter} swaps")
    print(listToSort)

    return listToSort


bubbleSort(unsortedList)



# Merge Sort does not work here

def merge(left, right):
    emptyList = []

    leftLength = len(left) - 1
    rightLength = len(right) - 1

    leftIndex = 0

    for i in range(0, leftLength + rightLength + 1):
        if (leftIndex > rightLength):
            emptyList.append(right[i-leftIndex])
        if leftIndex < i-rightLength:
            leftIndex += 1
        if left[leftIndex] <= right[i-leftIndex]:
            emptyList.append(left[leftIndex])
        else:
            emptyList.append(right[i-leftIndex])

    return emptyList

def mergeSort(listToSort):

    length = len(listToSort)

    if (length <= 1):
        return listToSort
    
    leftList = []
    rightList = []

    midpoint = math.floor((length - 1) / 2)

    for i in range(0,midpoint + 1):
        value = listToSort[i]
        leftList.append(value)


    for i in range(midpoint + 1, length):
        value = listToSort[i]
        rightList.append(value)
    
    leftList = mergeSort(leftList)
    rightList = mergeSort(rightList)


    return merge(leftList, rightList)

    
print("Merge")
print(mergeSort(unsortedList))