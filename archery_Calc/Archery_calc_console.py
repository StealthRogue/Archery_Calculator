import os

#Functions

def greeter():
    os.system('clear')

    print("\t**********************************************")
    print("\t***           Greetings Archers            ***")
    print("\t**********************************************")

def options():
    print("\n[1]Set Archers")
    print("[2]Start Calc")
    print("[q]Quit")

    return input("What would you like to do?")

def archers():
    #we store em in an array
    arch_1 = input("Please type the name of Archer 1: ")
    arch_2 = input("Please type the name of Archer 2: ")
    archer.append(arch_1)
    print("Get Ready %s!\n" % arch_1.title())
    archer.append(arch_2)
    print("Get Ready %s!\n" % arch_2.title())

def calc():
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
    elif sum_arch_1 < sum_arch_2:
        print("\nArcher 2 Takes 2pts")
    elif sum_arch_1 == sum_arch_2:
        print("\nBoth Archers take 1pt")


### Main Program
archer=[]

greeter()
choice = ''

while choice != 'q':

    choice = options()

    greeter()
    if choice == '1':
        archers()
    elif choice == '2':
        calc()
    elif choice == 'q':
        print("Goodbye, Fellas!")
    else:
        print("Sorry I do not understand that!")