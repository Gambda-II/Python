import keyboard
import random
import asyncio

from os import system, name

options = ["Schere", "Stein", "Papier"]
currentOption = 0

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def DisplayMessage(message):
    print(message)

def DisplayIntro():
    DisplayMessage("Willkommen zum Schere-Stein-Papier Simulator v1")

def DisplayOptions():
    clear()
    for index, option in enumerate(options):
        if index == currentOption:
            print(f"> {option} <")
        else:
            print(option)

def GetKeyPressed():
    global currentOption

    playing = True

    while(playing):

        keyboard.read_key()
        if keyboard.is_pressed("down"):
            currentOption += 1
            currentOption %= 3
            DisplayOptions()
            GetKeyPressed()
        elif keyboard.is_pressed("up"):
            currentOption -= 1
            currentOption %= 3
            DisplayOptions()
            GetKeyPressed()
        elif keyboard.is_pressed("enter"):
            playing = False
            return currentOption
        

def GetUsersPick():
    clear()
    DisplayMessage("Wähle Schere, Stein oder Papier aus!")
    DisplayOptions()

    return  GetKeyPressed()

def ComputerPick():
    randomNumber = random.randint(0,2)
    return randomNumber

def GetEndScreen(userPicked, computerPicked):

    if (userPicked == computerPicked):
    
        DisplayMessage("DRAW!")
        quit()
        

    if (userPicked - 1) % 3 == computerPicked:
        DisplayMessage("YOU WIN!")   
        quit()
        
    
    DisplayMessage("YOU LOSE!")
    quit()
    

def Program():
    DisplayIntro()
    userPicked = GetUsersPick()
    clear()
    print("User picked:", options[userPicked])
    computerPicked = ComputerPick()
    print("Computer picked:", options[computerPicked])
    GetEndScreen(userPicked, computerPicked)

Program()