import csv

global choline

def micronutrients(food):
    global choline
    global betaine
    global folate
    global b12

    choline = 0


def main():

    food = input("Enter food you are calculating the micronutrients for? ")
    print ("hows it going")
    micronutrients(food)
    print(choline)
    


main()
