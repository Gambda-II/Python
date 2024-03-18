# TO DO
# PYTHON
# add class customer
# 
# add class bankaccount DONE
# add constructor with 4
# 4
# ters name, optional initial deposit value DONE
# add auto generated unique id
# add method to deposit a value and add it to the balance DONE
# add method to withdraw money, check if the balance allows this first, else print a warning DONE
# add method to show the current balance DONE
# add method to show the account info: show name, id, balance DONE
# DATABASE
# add DB functionality to every method
# add database bankaccount DONE
# add databse client / customer


from res.classes.bankaccount import BankAccount

# 

def program():
    showMenu()
    option = getUserSelection()
    optionAction(option)


def showMenu():
    print("1: Create a new bank account ")
    print("2: Deposit ")
    print("3: Withdraw ")
    print("4: Show Account Details ")

def getUserSelection():
    userInput = input("Please choose a number \n")
    try:
        number = int(userInput)
        if (number > 0 and number < 6):
            return number
        
        getUserSelection()
    except:
        getUserSelection()
        
def optionAction(inputOption):

    try:
        match inputOption:
            case 1:
                createNewAccount()
            case 2:
                deposit()
            case 3:
                withdraw()
            case 4:
                showInfo()
            case _:
                print("No Option implemented, program closes")
                quit()
    except Exception as e:
        print(f"Unexpected error, program closes - {e}")
        quit()

def createNewAccount():
    firstNameInput = getUserInputText("What's your first name?\n")
    lastNameInput = getUserInputText("What's your last name?\n")
    roundedValue = 0

    if (getUserInputBoolean("Do you want to deposit an initial value? Y/N\n") == True):
        value = getUserInputFloat("Please type in your amount you want to deposit:\n")
        print(value)
        roundedValue = value.__round__(2)
    
    formattedInputs = f"First Name: \t {firstNameInput}\nLast Name: \t {lastNameInput}\nDeposit: \t {roundedValue}\n"
    if (getUserInputBoolean(f"Is everything correct? Y/N\n{formattedInputs}\n") == False):
        createNewAccount()
        return

    newAccount = BankAccount(firstNameInput,lastNameInput,roundedValue) 
    return newAccount

def deposit():
    id = getUserInputID("Please type in your bank id:\n")
    if (checkIDExists(id) == True):
        value = getUserInputFloat("Please type in your amount you want to deposit:\n")
        bankaccount = BankAccount.getAccountByID(id)
        bankaccount.deposit(value)
    else:
        print("Id was not found")

def withdraw():
    id = getUserInputID("Please type in your bank id:\n")
    if (checkIDExists(id) == True):
        value = getUserInputFloat("Please type in your amount you want to withdrawl:\n")
        bankaccount = BankAccount.getAccountByID(id)
        bankaccount.withdraw(value)
    else:
        print("Id was not found")

def showInfo():
    id = getUserInputID("Please type in your bank id:\n")
    if (checkIDExists(id) == True):
        bankaccount = BankAccount.getAccountByID(id)
        print(bankaccount)
        bankaccount.showBankInfo()
    else:
        print("Id was not found")


def checkIDExists(id):
    return BankAccount.checkID(id)

def getUserInputText(prompt):
    return input(prompt)

def getUserInputBoolean(prompt):
    isBoolean = input(prompt) 
    isBoolean = isBoolean.upper()
    print(isBoolean)
    try:
        if (isBoolean.__contains__("YES") or isBoolean.startswith("Y")):
            return True
        elif (isBoolean.__contains__("NO") or isBoolean.startswith("N")):
            return False
        else:
            return getUserInputBoolean("Please try again\n")
    except:
        return getUserInputBoolean("Please only type Yes (Y) or No (N):\n")

def getUserInputFloat(prompt):
    value = input(prompt)

    try:
        convertedValue = float(value)
        return convertedValue
    except:
        print("Please try again")
        return getUserInputFloat(prompt)

def getUserInputID(prompt):
    
    value = input(prompt)

    try:
        convertedValue = int(value)
        return convertedValue
    except:
        print("Please try again")
        return getUserInputID(prompt)

program()