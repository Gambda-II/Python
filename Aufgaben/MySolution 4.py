def FizzBuzz(upperLimit,firstDivisor = 3, secondDivisor = 5):
    currentNumber = 1


    while (currentNumber <= upperLimit):

        text = ""

        isFizz = currentNumber % firstDivisor == 0
        isBuzz = currentNumber % secondDivisor == 0

        if (isFizz and isBuzz):
            text = "FizzBuzz"
        elif (isFizz):
            text = "Fizz".center(8)
        elif (isBuzz):
            text = "Buzz".center(8)
        else:
            text = f"{currentNumber}".center(8)
        
        print(text)
        currentNumber += 1

FizzBuzz(100,3,5)