import json
import os

def userInput():
    first_Name = input("what is your first name?")
    last_Name = input("what is your last name?")
    userNames = { "first Name": first_Name,
                  "last name": last_Name,
                 }
    
    with open("user_data.json", "w") as json_file:
        json.dump(userNames, json_file, indent=4)


def readAndPrintJSON():
    with open("user_data.json", "r") as json_file:
        data = json.load(json_file)
        print("JSON Data:", data)

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def changeTerminalColorToGreen ():
    GREEN = '\033[92m'
    RESET = '\033[0m' ## This Resets the color the defualt one. adds this to the print command to reset.
    print(GREEN + "This text is Green." + RESET)

