import csv
    

def set_micros(food):
    global foodName
    global choline
    global betaine
    global folate
    global b12
    global index
    

    with open('data.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        foods = []
        cholineVals = []
        betaineVals = []
        folateVals = []
        b12Vals = []

        for row in readCSV:
            foodName = row[0]
            choline = row[1]
            betaine = row[2]
            folate = row[3]
            b12 = row[4]
            
            foods.append(foodName)
            cholineVals.append(choline)
            betaineVals.append(betaine)
            folateVals.append(folate)
            b12Vals.append(b12)

    print(foods)
    print(cholineVals)
        
    for x in range(len(foods)):
        if(food == foods[x]):
            index = x

        else:
            continue

    choline = cholineVals[index]
    betaine = betaineVals[index]
    folate = folateVals[index]
    b12 = b12Vals[index]

    print("this is the choline for ", food, ": ", choline)
    print("this is the betaine for ", food, ": ", betaine)
    print("this is the folate for ", food, ": ", folate)
    print("this is the b12 for ", food, ": ", b12)


def calculate(freq, amount):
    global fin_choline
    global fin_betaine
    global fin_folate
    global fin_b12

    amount = amount/100
    
    fin_choline = per100g * freq * choline
    fin_betaine = per100g * freq * betaine
    fin_folate = per100g * freq * folate
    fin_b12 = per100g * freq * b12

    print("This is the micronutrient breakdown for ", food)
    print("This is the choline content: ", fin_choline)
    print("This is the betaine content: ", fin_betaine)
    print("This is the folate content: ", fin_folate)
    print("This is the B12 content: ", fin_b12)



def print_frequencies():
    print("\nThese are the frequencies") 
    print("0: never")
    print("0.03: 1/month")
    print("0.07: 2/month")
    print("0.13: 1/week")
    print("0.4: 3/week")
    print("0.73: 5.5/week")
    print("1: 1/day")
    print("2.5: 2.5/day")
    print("4.5: 4.5/day")
   
   
def main():
    
    global food
    
    food = input('Enter the food you are calculating the micronutrients for? (check data file to find specific name to type) ')
    amount = input('\nHow often is the food consumed? (ex: if it\'s 40g, put 40, or 125mL, put 125) ')
    print_frequencies()
    freq = input('\nHow often is the food item consumed? (input number corresponding to frequency) ')
    
    set_micros(food)
    print("Found micronutrient values for ", food, "...")
    
    print("Now calculating final micronutrient values... ")
    calculate(freq, amount)


main()
