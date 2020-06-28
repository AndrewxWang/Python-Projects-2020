import sys
import time
import random

print("While walking in the forest, you find a monster!")
time.sleep(1)
print("The monster challenges you to fight!")
time.sleep(1)
print("")

def game():
    #INITIALIZATION
    ending = -1     #decides which ending you get
    myHP = 100      #Your HP
    myPots = 5      #Potions, they heal for 30HP
    monHP = 100     #Monster HP
    choice = -1     #Your Choice, choice is reset to -1 each round
    inGame = True
    inChoice = True
    
    #GAME
    while inGame:
        #MY CHOICE
        while inChoice:
            print("<------------------------------->")
            print("Your HP: " + str(myHP) + " | Monster's HP: " + str(monHP))
            print("Potions left: " + str(myPots))
            print("")
            time.sleep(1)
            print("Your turn:")
            choice = input("Attack[0] | Heal[1] | Run[2]: ")
            if myPots > 0:
                if choice in ['0','1','2']:
                    inChoice = False
                else:
                    print("Invalid input.")
            else:
                if choice in['0','2']:
                    inChoice = False
                elif choice in['1']:
                    print("You have no potions left.")
                else:
                    print("Invalid input.")
        print("")
        #BATTLE
        if choice in ['0']:
            dmg = random.randint(1,20)
            if monHP-dmg <= 0:
                dmg=monHP
                print("You did " + str(dmg) + " damage to the monster!")
                myHP-dmg
                ending = 0
                inGame = False
                continue
            else:
                print("You did " + str(dmg) + " damage to the monster!")
                monHP-=dmg
 
        #HEAL
        elif choice in ['1']:
            if myHP == 100:
                print("Potion had no effect!")
            elif myHP+30 > 100:
                n = 100-myHP
                print("You used a potion! + " + str(n) + "HP!")
                myHP+=(n)
            else:
                print("You used a potion! +30HP!")
                myHP+=30
            myPots-=1
            
        #RUN
        elif choice in ['2']:
            while True:
                randNum = random.randint(1,5)
                your_num = input("Pick a number between 1-5: ")
                if (int(your_num) >= 1) and (int(your_num) <= 5):
                    break
                else:
                    print("Invalid input.")

            if randNum == int(your_num):
                ending = 1
                inGame = False
            else:
                print("You failed to run away. Your number: " + str(your_num) + " | Monster's number: " + str(randNum))


        #MONSTER'S CHOICE
        if monHP > 0:
            print("")
            print("The Monster's turn:")
            time.sleep(2)
            monChoice = random.randint(1,30)
            if monChoice <= 24:
                if myHP-monChoice <= 0:
                    monChoice= myHP
                    print("The monster attacked you for " + str(monChoice) + " damage!")
                    myHP-=monChoice
                    ending = 2
                    inGame = False
                else:
                    print("The monster attacked you for " + str(monChoice) + " damage!")
                    myHP-=monChoice
            else:
                print("The monster missed his attack!")
        #RESET
        choice = -1
        inChoice = True
    print("")
    if ending == 0:
        print("You successfully killed the monster!")
    elif ending == 1:
        print("You successfully ran away from the monster!")
    elif ending == 2:
        print("You were killed...better luck next time!")
    time.sleep(5)
    print("Closing game..")
    time.sleep(10)
        
game()

