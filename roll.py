import random
import time

print("-----------")
print("Dice Roller")
print("-----------")
print("")

def D4():
    D4L = [1, 2, 3, 4]
    D4 = random.choice(D4L)
    print("D4 Roll:", D4)

def D6():
    D6L = [1, 2, 3, 4, 5, 6]
    D6 = random.choice(D6L)
    print("D6 Roll:", D6)

def D8():
    D8L = [1, 2, 3, 4, 5, 6, 7, 8]
    D8 = random.choice(D8L)
    print("D8 Roll:", D8)

def D10():
    D10L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    D10 = random.choice(D10L)
    print("D10 Roll:", D10)

def D12():
    D12L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    D12 = random.choice(D12L)
    print("D12 Roll:", D12)

def D20():
    D20L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    D20 = random.choice(D20L)
    print("D20 Roll:", D20)

def user_input():
    roll = input("choose Dice (D4, D6, D8, D10, D12, D20): ")

    if roll == "D4":
        D4()
    elif roll == "4":
        D4()
    elif roll == "D6":
        D6()
    elif roll == "6":
       D6()
    elif roll == "D8":
        D8()
    elif roll == "8":
        D8()
    elif roll == "D10":
        D10()
    elif roll == "10":
        D10()
    elif roll == "D12":
        D12()
    elif roll == "12":
        D12()
    elif roll == "D20":
        D20()
    elif roll == "20":
        D20()
    else:
        print("Error - Invalid Charater - exit(01)")
        exit()

loop = 1
while loop == 1:
    user_input()
    time.sleep(0.5)