from os import system
import random
import re
from time import sleep
import sys


def main():
    system("cls")
    listofchoices=["rock","paper","scissors"]
    print("\nWELCOME TO THE ROCK/PAPER/SCISSORS GAME\n")
    while True:
        try:
            name=get_name()
            break
        except ValueError:
            continue
    
    print(f"Welcome {name}! Press Enter to get started")
    input()
    system("cls")
    
    while True:
        while True:
            try:
                print("Whats your choice(rock/paper/scissors): ")
                choice=get_choice()
                break
            except ValueError:
                continue
        print("Good choice. So lets begin")
        sleep(1)
        system("cls")
        for i in listofchoices:
            print(f"{i.upper()}!!!")
            sleep(1)
        system("cls")
        enemy_choice=generate_answer(listofchoices)
        print(f"\nYou: {choice}")
        print(f"Me: {enemy_choice}\n")

        print(game(choice,enemy_choice,listofchoices))
        
        print("\n\n Press Enter")
        input()
        system("cls")
        while True:
            try:
                restart_or_no()
                break
            except ValueError:
                print("Invalid input! Try again\n")


def restart_or_no():
    c=input("Do you wanna play again(yes/no): ")
    match(c.lower()):
        case "yes":
            pass
        case "no":
            sys.exit()
        case _:
            raise ValueError
        

def game(mchoice,echoice,listofchoices):
    mc=listofchoices.index(mchoice)
    ec=listofchoices.index(echoice)
    if mc+1>len(listofchoices):
        if listofchoices[0]==listofchoices[ec]:
            return f"You lost!"
    elif listofchoices[mc+1]==listofchoices[ec]:
        return f"You lost!"
    elif listofchoices[mc]==listofchoices[ec]:
        return f"Draw!"
    elif mc-1==-1:
        if listofchoices[2]==listofchoices[ec]:
            return f"You won!"
    elif listofchoices[mc-1]==listofchoices[ec]:
        return f"You won!"
        
        
def get_choice():
    choice=input().strip()
    isword=re.search(r"^(rock|paper|scissors)$",choice,flags=re.I)
    if isword:
        return isword.group(1).lower()
    else:
        raise ValueError("Wrong input")
    

def get_name():
    n=input("Whats your name: ")
    t=re.search(r"([\w -]+)",n,flags=re.I)
    if t:
        return n
    elif t.group(1)==None:
        raise ValueError("Please")
    else:
        raise ValueError("Invalid input. use only letters and -")

def generate_answer(lis):
    return random.choice(lis)


if __name__=="__main__":
    main()