import csv
    

def micronutrients(food):
    global choline
    global betaine
    global folate
    global b12

    choline = 5

def calculate(freq, amount):
    global fin_choline
    global fin_betaine
    global fin_folate
    global fin_b12

    per100g = amount/100
    
    fin_choline = per100g * freq * choline
    fin_betaine = per100g * freq * betaine
    fin_folate = per100g * freq * folate
    fin_b12 = per100g * freq * b12

    print("This is the micronutrient breakdown for ", food)
    print("This is the choline content: ", fin_choline)
    print("This is the betaine content: ", fin_betaine)
    print("This is the folate content: ", fin_folate)
    print("This is the B12 content: ", fin_b12)



#def print_frequencies(tempFrequency):
   #global freq

#def set_frequencies(numFrequency):
    
def main():
    with open("data.csv", "rt") as f:
        reader = csv.reader(f, delimiter="\t")
        for i, line in enumerate(reader):
            print ('line[{}] = {}'.format(i, line))
    
    global food
    
    food = input("Enter the food you are calculating the micronutrients for? (check data file to find specific name to type) ")
    amount = input("How often is the food consumed? (ex: if it's 40g, dont put 0.4, put 40) ") 
    freq = input("how often is it consumed? (input number corresponding to frequencies) ")
    
    micronutrients(food)
    print("found micronutrient values for ", food, "...")
    
    print("Now calculating final micronutrient values... ")
    calculate(freq, amount)

    
    #print(choline)
    


main()
