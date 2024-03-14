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



