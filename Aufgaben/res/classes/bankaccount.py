import mysql.connector

def create_connection():
    try:
        connection =  mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "bankdb",
            port = "3306"
        )
        #print("Connection - SUCCESS")
        return connection

    except Exception as e:
        print(f"Connection - FAILED - {e}")

def create_account_in_database(firstName, lastName, initialDeposit):
    connection = create_connection()
    cursor = connection.cursor()

    query = "INSERT INTO bankaccount (firstName, lastName, balance) VALUES (%s, %s, %s);"
    params = (firstName, lastName, initialDeposit)

    try:
        cursor.execute(query, params)
        connection.commit()
        message = "Account creation in DB - SUCCESS"
        print(message)
        return message

    except Exception as e:
        message = f"Account creation in DB - FAILED {e}"
        print(message)
        return message

    finally:
        connection.close()

def fetch_balance_from_database(id):
    connection = create_connection()
    cursor = connection.cursor()

    query = "SELECT balance FROM bankaccount WHERE id=%s;"
    params = (id,)

    try:
        cursor.execute(query,params)
        resultArray = cursor.fetchall()
        resultTupel = resultArray[0]
        firstValueInTupel = resultTupel[0]
        formattedResult = float(firstValueInTupel).__round__(2)
        return formattedResult

    except Exception as e:
        print(f"Fetch balance - FAILED - {e}")
    
    finally:
        connection.close()

def fetch_name_by_id_from_database(id):
    connection = create_connection()
    cursor = connection.cursor()

    query = f"SELECT firstName, lastName FROM bankaccount WHERE id=%s;"
    params = (id,)

    try:
        cursor.execute(query,params)
        resultArray = cursor.fetchall()
        
        return resultArray

    except Exception as e:
        print(f"Fetch name - FAILED - {e}")

    finally:
        connection.close()

def fetch_id_from_database():
    connection = create_connection()
    cursor = connection.cursor()

    query = "SELECT id FROM bankaccount ORDER BY id DESC LIMIT 1;"
    
    try:
        cursor.execute(query)
        resultArray = cursor.fetchall()
        resultTupel = resultArray[0]
        id = resultTupel[0]
        return id
    
    except Exception as e:
        print(f"Fetch id - FAILED - {e}")

    finally:
        connection.close()

def update_balance_in_database(id, amount):
    connection = create_connection()
    cursor = connection.cursor()
    balance_from_db = fetch_balance_from_database(id)
    newBalance = balance_from_db + amount
    query = f"UPDATE bankaccount SET balance=%s WHERE id=%s"
    params =(newBalance, id,)

    try:
        cursor.execute(query,params)
        connection.commit()
        print("Update balance - SUCCESS!")

    except Exception as e:
        print(f"Update balance - FAILED - {e}")
    
    finally:
        connection.close()
        

class BankAccount:

    def __init__(self, firstName, lastName, initialDesposit = 0, id = 0):

        self.__firstName = firstName
        self.__lastName = lastName
        self.__currentBalance = 0

        try:
            if (initialDesposit > 0):
                self.__currentBalance = 0 + initialDesposit
        except:
            if isinstance(initialDesposit,float):
                initialDesposit = float(initialDesposit)
                self.__currentBalance += initialDesposit

        if (self.checkID(id) == False):
            message = create_account_in_database(firstName,lastName,self.__currentBalance)
            id_db = fetch_id_from_database()
            self.__id = id_db
        else:
            self.__id = id
            
    
    def deposit(self, amount):
        try:
            if (amount == 0):
                print("Transaction 'Deposit' ignored - deposit was zero")
                return "Transaction 'Deposit' ignored - deposit was zero"

            if (amount < 0):
                print("Error: Transaction 'Deposit' failed - deposit was negative")
                return "Error: Transaction 'Deposit' failed - deposit was negative"
            self.__currentBalance += amount
            #print(self.__currentBalance)
            update_balance_in_database(self.__id,amount)
            #print(fetch_balance_from_database(self.__id))
            print("Transaction 'Deposit' successfully completed!")
            return "Transaction 'Deposit' successfully completed!"

        except Exception as e: 
            print(f"Error: Transaction 'Deposit' failed -  {e}")
            return f"Error: Transaction 'Deposit' failed -  {e}"


    def withdraw(self, amount):
        try:
            if (amount == 0):
                print("Transaction 'Withdraw' ignored - withdraw was zero")
                return

            if (amount < 0):
                print("Error: Transaction 'Withdraw' failed - withdraw was negative")
                return
            
            if (amount > self.__currentBalance):
                print("Error: Transaction 'Withdraw' failed - current Balance is too low to complete transaction")
                return
            
            self.__currentBalance -= amount
            update_balance_in_database(self.__id,-amount)
            print("Transaction 'Withdraw' successfully completed!")

        except Exception as e:
            print(f"Error: Transaction 'Withdraw' failed - {e}")


    def showBalance(self):
        currentBalance = fetch_balance_from_database(self.__id)
        formattedCurrentBalance = f"Current Balance:\t {currentBalance.__round__(2)} €"
        print(formattedCurrentBalance)

    def showBankInfo(bankAccount):
        id = bankAccount.__id
        formattedId = f"Banking ID:\t\t {id}"
        name = fetch_name_by_id_from_database(id)
        firstName = name[0][0]
        lastName = name[0][1]
        formattedFullName = f"Name: \t\t\t {firstName}, {lastName}"        
        print("-----------------------------------------------")
        print(formattedId)
        print(formattedFullName)
        bankAccount.showBalance()
        #fetch_balance_from_database(bankAccount.__id)
        print("-----------------------------------------------")

    @staticmethod
    def checkID(id):
        connection = create_connection()
        cursor = connection.cursor()
        query = f"SELECT id FROM bankaccount WHERE id={id};"

        try:
            cursor.execute(query)
            result = cursor.fetchall()

            if (len(result) > 0):
                return True
            else:
                return False
                
        except Exception as e:
            BankAccount.checkID(id)
    
    @staticmethod
    def getAccountByID(id):

        try:
            if(BankAccount.checkID(id) == True):
                name = fetch_name_by_id_from_database(id)
                firstName = name[0][0]
                lastName = name[0][1]
                balance = fetch_balance_from_database(id)
                bankaccount = BankAccount(firstName, lastName, balance, id)
                return bankaccount
            else:
                print("ID was not found")
                return None
        except Exception as e:
            print(f"An Error occured - {e}")
            return None
