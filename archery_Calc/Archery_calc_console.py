import os
from time import sleep
import string

#Functions

def greeter():
    os.system('clear')

    print("\t**********************************************")
    print("\t***           Greetings Archers            ***")
    print("\t**********************************************")

def options():
    print("\n[1]Set Archers")
    print("[2]Tournament Mode(Calculator)")
    print("[3]Collecting Pts (Calculator)")
    print("[q]Quit")

    return input("What would you like to do? ")

def archers():
    #we store em in an array
    arch_1 = input("Please type the name of Archer 1: ")
    arch_2 = input("Please type the name of Archer 2: ")
    archer.append(arch_1)
    print("Get Ready %s!\n" % arch_1.title())
    archer.append(arch_2)
    print("Get Ready %s!\n" % arch_2.title())

def calc():
    a = 0 #archer 1
    b = 0 #archer 2
    while a!= 6 or b!=6:
        #the calculations goes here
        Arrow1_arch_1 = int(input("\nPlease Archer 1, input your highest score for this shoot: "))
        Arrow2_arch_1 = int(input("Please Archer 1, input your second highest score for this shoot: "))
        Arrow3_arch_1 = int(input("Please Archer 1, input the lowest score for this shoot: "))
        sum_arch_1 = Arrow1_arch_1 + Arrow2_arch_1 + Arrow3_arch_1
        print("\nArcher 1")
        print("The sum of this shoot is: ",sum_arch_1)

        Arrow1_arch_2 = int(input("\nPlease Archer 2, input your highest score for this shoot: "))
        Arrow2_arch_2 = int(input("Please Archer 2, input your second highest score for this shoot: "))
        Arrow3_arch_2 = int(input("Please Archer 2, input the lowest score for this shoot: "))
        sum_arch_2 = Arrow1_arch_2 + Arrow2_arch_2 + Arrow3_arch_2
        print("\nArcher 2")
        print("The sum of this shoot is: ", sum_arch_2)

        if sum_arch_1 > sum_arch_2:
            print("\nArcher 1 Takes 2pts")
            a= a + 2
        elif sum_arch_1 < sum_arch_2:
            print("\nArcher 2 Takes 2pts")
            b = b+2
        elif sum_arch_1 == sum_arch_2:
            print("\nBoth Archers take 1pt")
            a = a+1
            b = b+1
        print("\n-------------------------------------------------------")
        if a == 6 or a > 6:
            print("Archer 1 Wins with: ", a ,"to", b)
            break

        elif b == 6 or b > 6:
            print("Archer 2 Wins with: ", b ,"to", a)
            break


def pts_collector():
    for i in range(1,11):
        print("Shoot No.: ", i)
        Arrow1_arch_1 = int(input("\nPlease Archer 1, input your highest score for this shoot: "))
        Arrow2_arch_1 = int(input("Please Archer 1, input your second highest score for this shoot: "))
        Arrow3_arch_1 = int(input("Please Archer 1, input the lowest score for this shoot: "))
        sum_arch_1 = Arrow1_arch_1 + Arrow2_arch_1 + Arrow3_arch_1
        print("\nArcher 1")
        print("The sum of this shoot is: ", sum_arch_1)

        Arrow1_arch_2 = int(input("\nPlease Archer 2, input your highest score for this shoot: "))
        Arrow2_arch_2 = int(input("Please Archer 2, input your second highest score for this shoot: "))
        Arrow3_arch_2 = int(input("Please Archer 2, input the lowest score for this shoot: "))
        sum_arch_2 = Arrow1_arch_2 + Arrow2_arch_2 + Arrow3_arch_2
        print("\nArcher 2")
        print("The sum of this shoot is: ", sum_arch_2)
        print("--------------------------------------------------------")
        sleep(120)
        a = sum_arch_1+ sum_arch_1
        b = sum_arch_2 + sum_arch_2
    print("\n",a)
    print(b)
### Main Program
archer=[]

greeter()
choice = ''
x = 10
while choice != 'q':

    choice = options()

    greeter()
    if choice == '1':
            archers()
    elif choice == '2':
        calc()
    elif choice == 'q':
        print("Goodbye, Fellas!")
    elif choice == '3':
        pts_collector()
    else:
        print("Sorry I do not understand that!")