#Python Covid-19 Program

casesSA = 27403
casesChina = 82995
casesUSA = 1700000
Countries = ["Brazil has 719449 confirmed cases", "Russia has 485253 confirmed cases",\
             "Spain has 289046 confirmed cases", "India has 274450 confirmed cases",\
             "Peru has 199696 confirmed cases", "Italy has 235561 confirmed cases"]

def SA(y):
        return y + casesSA
def USA(y):
        return y + casesUSA
def China(y):
        return y + casesChina




#Menu

print('Welcome to the Covid 19 support service.')
print()
print('Please select an option below: ')
print()

while True:
#Options to choose from 
    print("1. Statistics")
    print("2. Prevention")
    print("3. Symptoms")
    print("4. Treatment")
    print("5. Report Case")
    print("6. Exit")
    print()

    choice = input("Enter choice (1/2/3/4/5/6): ")
    print()

# Option functions and what will happen when that specific number is selected
# if statements
    if choice == "1":
        print("Currently in SA there are",casesSA, "Confirmed cases. ")
        print("Currently in China there are",casesChina, "Confirmed cases. ")
        print("Currently in USA there are",casesUSA, "Confirmed cases. ")
        print()
        op = input("Would you like to see the confirmed cases for a random Country? y/n: ")
        print()
        
        if op == "y":
                
            co = int(input("To select a random Country, type a number from 0 to 9: "))
            print(Countries[co])
            print()
                
    elif choice == "2":
            print("To prevent the spread of COVID-19:")
            print()
            print("Clean your hands often. Use soap and water, or an alcohol-based hand rub. ")
            print("Maintain a safe distance from anyone who is coughing or sneezing.")
            print("Don't touch your eyes, nose or mouth.")
            print("Cover your nose and mouth with your bent elbow or a tissue when you cough or sneeze. ")
            print("Stay home if you feel unwell.")
            print("If you have a fever, cough and difficulty breathing, seek medical attention. Call in advance.")
            print("Follow the directions of your local health authority.")
            print()
            
    elif choice == "3":
            print("Most Common Symptoms: ")
            print()
            print("* Fever")
            print("* Dry Cough")
            print("* Tiredness")
            print()
            
            print("Less Common Symptoms: ")
            print()
            print("* Aches & Pains")
            print("* Sore Throught")
            print("* Diarrhoea")
            print("* Conjunctivitis")
            print("* Headache")
            print("* Loss of Taste or Smell")
            print("* A rash on skin, or discolouration of fingers or toes.")

            print("Serious Symptoms: ")
            print()
            print("Difficulty breathing or shortness of breath")
            print("Chest pain or pressure")
            print("Loss of speech or movement.")
            print()
            
    elif choice == "4":
            print('''
If you feel sick you should rest, drink plenty of fluid and eat nutritious food.Stay in a seperate room\
from other family members, and use a dedicated bathroom if possible.
Clean and disinfect frequentlty touched surfaces.
''')

    elif choice == "5":
            print()

            sym = input("Do you have any of these symptoms? y/n: ")
            if sym == "y":
                    temp = input("Is your temperature above 38.5 degree Celsius? y/n: ")
                    if temp == "y":
                            print()
                            print("In which country are you? Select an option below")
                            print("1. SA")
                            print("2. China")
                            print("3. USA")
                            print()

                            option = input("Please enter your option (1/2/3): ")
                            if option == "1":
                                    casesSA = (SA(1))
                            elif option == "2":
                                    casesChina = (China(1))
                            elif option == "3":
                                    casesUSA = (USA(1))

                            print()
                            print("You have Covid-19 Please get some treatment.")
                            print()
                    elif sym == "n":
                            print()
                            print("You don't have Covid 19.")
                            print()
                            
                    elif sym == "n":
                            print()
                            print("You don't have Covid 19.")
                            print()

    elif choice == "6":
            break
                            
                            
