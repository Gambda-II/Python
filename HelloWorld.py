# import statements
import math

# comment
print("Hello World!")

# CTRL + K , CTRL + C
# makes a multiline comment

# variables and datatypes
age = 31
name = "Alex"
is_cool = True
x=math.pi
y=math.cos(x)

# output
print(x+y)

# formatted output
print(f"{name} ist {age} Jahre alt.")


# If-Else
if age >= 18:
    print(f"{name} can drink")
else:
    print(f"{name} can drink, but shouldn't")


number = 3

# If-Elseif-Else
if number == 1:
    print("Nummer ist Eins")
elif number == 2:
    print("Nummer ist Zwei")
elif number == 11:
    print("Nummer ist EinsElf")
else:
    print("Nummer ist keine Nummer")

# Switch
match number:
    case 1: 
        print("Eins")
    case 2: 
        print("Zwei")
    case 3: 
        print("Drei")
    case 4: 
        print("Vier")
    case _:
        print("nummer ist etwas anderes")

# For        
for x in range(0,10):
    print(x)

# arrays must be imported first
import array

# declare an array
myArray = array.array('i',[1,2,3])

# lists
myList = [1, "hallo", 3.14, True]

# dictionaries
dictionary = {
    "name": "Max", 
    "age": 30, 
    "city": "New New York",
    }

# multi dimensional data structures
list_2d = [[1,2,3],[4,5,6],[7,8,9]]
print(list_2d)

dictionary_2d = {
    "person1": {"name": "John", "age": 69, "city": "Old New York"},
    "person2": dictionary,
}
print(dictionary_2d)

# Loops

colors = ["Rot", "Grün", "Blau"]
for color in colors:
    print(color)

for x in range(5):
    print(x)

for x in range(10,15):
    print(x)

for x in range(69,420,99):
    print(x)

counter = 0
while counter < 10:
    counter = counter + 1 
    print(f"Counter: {counter}")

countdown = 10
while (countdown > 0):
    countdown -= 2
    print(f"Countdown: {countdown}")

number = 5
while True:
    print(number)
    number -= 1
    if (number <= 0):
        break


multi2d_list = [[1,2,3],[4,5,6],[7,8,9]]

for i in multi2d_list:
    for j in i:
        print(f"entry: {j}")


import random

randomNumber = random.random()
print(randomNumber)

randomNumber = random.randint(5,10)
print(randomNumber)

randomNumber = random.lognormvariate(10, 3)
print(randomNumber)

randomNumber = random.randrange(10,50,3);
print(randomNumber)

randomNumber = random.uniform(1,6)
print(randomNumber)

element = random.choice(['Apfel', 'Birne', 'Dattel', 'Kirsche'])
print(element)

sortedList = [1,2,3,4,5,6,7,8,9];
random.shuffle(sortedList)
print(sortedList)

samples = random.sample(range(1,101),5)
print(samples)

def myFunction(name):
    return f"Hallo {name}"

print(myFunction("Alex"))
print(myFunction(99))
print(myFunction('Luftballons'))

# leere Klasse
class Leer:
    pass

# eine nicht-leere Klasse
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show_info(self):
        print(f"{self.name} ist {self.age} Jahre alt.")

firstPerson = Person("Michael", 31)
firstPerson.show_info()

# Access modifiers, default in classes public

class AccessModifiers:
    def __init__(self):
        self._protectedElement = "Geschützt"

class SubClass(AccessModifiers):
    def method(self):
        print(self._protectedElement)

object = AccessModifiers();
print(object._protectedElement)

object = SubClass();
object.method()

class PrivateAttributeClass:
    def __init__(self):
        self.__myPrivateAttribute = "Privat"
    
    def myMethod(self):
        print(self.__myPrivateAttribute)

object = PrivateAttributeClass()
object.myMethod()

# print(object.__myPrivateAttribute) --> object has no attribute (private)

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Es brummt!")

car = Car()
car.start();

class MyStaticMethodClass:
    classVariable = "I am a class variable"

    @staticmethod
    def staticMethod():
        print("S T A T I C")

MyStaticMethodClass.staticMethod()

#try-except
x = 1
y = 2
try:
    print(x/y)
except ZeroDivisionError:
    print("Division durch Null ist nicht so nice.")
except NameError:
    print("Variablen wurden nicht gefunden.")
finally:
    print("Versuch gestartet.")


try:
    with open('text.txt','r',encoding='utf8') as file:
        print(file.read())
except FileNotFoundError:
    print("Datei existiert nicht!")
except Exception as e:
    print(f"Der Fehler lautet: {e}")    
else:
    print("Datei wurde gefunden und konnte gelesen werden.")
finally:
    print("Versuch eine Datei zu lesen.")

with open('text.txt', 'r') as file:
    print(file.readlines())

with open('text.txt', 'w') as file:
    file.write("Das ist der neue Text!")
    
userInput = input("Bitte trage eine Zahl ein:")
int(userInput)
print(userInput)

from res.Bicycle import Bicycle

myBike = Bicycle("Mountainbike")
myBike.showDetails()

import numpy as np

array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

for zeile in array_2d:
    for element in zeile:
        print(element)