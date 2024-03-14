from os import system, name

# define our clear function
def clear():
 
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def GetInputNumber(console_message):
    while(True):
        input_number = input(console_message)

        clear()
        try:
            number = float(input_number)
            return number
        except:
            print("You're input could not be converted to a number. Please retry your input.\n")

def Addition(augend, addend):
    sum = augend + addend
    return sum

def Subtraction(minuend, subtrahend):
    difference = minuend - subtrahend
    return difference

def Multiplication(multiplier, multiplicand):
    product = multiplier * multiplicand
    return product

def Division(dividend, divisor):

    if (dividend == 0 and divisor == 0):
        return "NaN"
    
    if (dividend > 0):
        sign = "+"
    else:
        sign = "-"

    try:
        quotient = dividend / divisor
        return quotient
    except ZeroDivisionError:
        print("Can't divide by Zero")
        return f"{sign} Inf"



def Calculation(firstNumber, secondNumber):
    while(True):
        input_operation = input("Select an operation (+ - * /):\n\t")
        clear()
        match (input_operation):
            case "+":
                result = Addition(firstNumber,secondNumber)
                break
            case "-":
                result = Subtraction(firstNumber,secondNumber)
                break
            case "*":
                result = Multiplication(firstNumber,secondNumber)
                break
            case "/":
                result = Division(firstNumber,secondNumber)
                break
            case _:
                print("An error occured with your input. Please retry.\n")
    return input_operation, result

def Restart():
    input_yesOrNo = input("Restart another calculation? Yes / No \n")

    yesOrNo = input_yesOrNo.lower()

    if (yesOrNo.__contains__("yes") or yesOrNo.startswith("y")):
        return True
    if (yesOrNo.__contains__("no") or yesOrNo.startswith("n")):
        return False

def Program():
    clear()
    while (True):
        firstNumber = GetInputNumber("Pick your first number:\n\t")
        print(f"First Number: {firstNumber}" )

        secondNumber = GetInputNumber("Pick your second number:\n\t")
        print(f"First Number: {firstNumber}" )
        print(f"Second Number: {secondNumber}" )

        op, result = Calculation(firstNumber,secondNumber)
        print(f"{firstNumber} {op} {secondNumber} = {result} \n")

        if (not Restart()):
            clear()
            print("Exited program")
            break
        else:
            clear()

Program()