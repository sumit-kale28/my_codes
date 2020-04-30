import random
import time
def rand_number(swg):
    comp=random.choice(swg)
    return comp
    # print(num)



# rand_num= random.random ()
# print(rand_num)

# rand=random.randint(1,100)
# print(rand)

# lst=["Star plus","Star gold","DD National","Star Sport","Tens Sport","AAj Tak"]
# rand=random.choice(lst)
# print(rand)


user=0
computer=0
while True:
    print("------------------------------Snake-Water-Gun-------------------------------")
    name=input("Enter Your Name: ")
    print("----------------------------------------------------------------------------")
    str1=f"Congratulations {name} you win....!!!"
    print("Welcome",name.upper())
    lst_swg=["SNAKE","WATER","GUN"]
    for i in range(1,7):
        print("***************************************************************************")
        print("Round",i)
        num1=input("Select your choice(SNAKE-WATER-GUN): ")
        num=num1.upper()
        v=rand_number(lst_swg)
        if num=="GUN" and v=="GUN":
            computer=computer +1
            user=user+1
        elif num=="WATER" and v=="WATER":
            computer = computer + 1
            user = user + 1
        elif num=="SNAKE" and v=="SNAKE":
            computer = computer + 1
            user = user + 1
        elif num=="GUN" and v=="WATER":
            computer=computer + 1
            user=user + 0
        elif num=="GUN" and v=="SNAKE":
            user =user +1
            computer=computer +0
        elif num=="SNAKE" and v=="WATER":
            user = user + 1
            computer = computer + 0
        elif num=="SNAKE" and v=="GUN":
            user = user + 0
            computer = computer + 1
        elif num=="WATER" and v=="SNAKE":
            user = user + 0
            computer = computer + 1
        elif num=="WATER" and v=="GUN":
            user = user + 1
            computer = computer + 0
        else:
            print("ENTER VALID OPTION")
    print("***************************************************************************")
    print("Result will display soon.......Score is calculating")
    time.sleep(5)
    print("----------------------------------RESULT-----------------------------------")
    print("Computer:",computer)
    print("User:",user)
    if computer < user:
        print(str1)
    elif computer > user:
        print("Sorry {0} you loose...Better luck next time ,Computer Win".format(name))
    else:
        print("Result Tie")
    print("***************************************************************************")
    cont=input("Do You Want to Continue(Y/N)?:")
    print("***************************************************************************")
    if cont=="Y" or cont=="y":
        user=0
        computer=0
        continue
    elif cont=="N" or cont =="n":
        break
    else:
        print("You Enter invalid Option....sorry bye bye..!!")
        break
    print("***************************************************************************")