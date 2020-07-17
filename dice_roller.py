import random
import os
import subprocess as sp

def clear():
    os.system('clear')

def Roll_dice(number_of_rolls):
    for i in range(0, number_of_rolls):
        number = random.randint(1,6)
        print(number)
    play_again = input("do you want to play again? (y/n): ")
    if play_again == "y":
        clear()
        Starting()
    else:
        quit()

def Starting():
    print("Welcome in Pedro's dice roller game. Select what do you want to do by choosing one of the options:")
    print("1 = one roll")
    print("2 = multiple rolls")
    print("3 = exit")
    decision = int(input("Enter what you want to do: "))
    if decision == 1:
        clear()
        print("You choose one roll. This is your output: ")
        Roll_dice(1)
    elif decision == 2:
        clear()
        print("You choose multiple rolls. Please input how many rolls would you like to do")
        num_rolls = int(input("Enter number of rolls: "))
        Roll_dice(num_rolls)
    elif decision == 3:
        exit()


Starting()