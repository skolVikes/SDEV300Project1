## SDEV300 Voter Application Program
states = ['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY', 'LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SD','SC','TN','TX','UT','VT','VA','WA','WV','WY']

def get_age():
    while True:
        try:
            user_age = int(input("What is your age? "))
            if user_age < 18:
                print("Please return when you are at least 18 years of age.")
                exit()
            elif user_age > 110:
                print("You did not enter a realistic age. Goodbye.")
                exit()
        except ValueError:
            print("Please enter your age in numerical format.\n")
            continue
        else:
            return user_age
##Gets user's zip code
def get_zip():
    while True:
        try:
            user_age = int(input("What is your zip code? "))
            if(user_age < 10000 or user_age > 99999):
                print("Please enter a 5 digit zip code.")
                continue
        except ValueError:
            print("Please enter your zip code in numerical format.\n")
            continue
        else:
            return user_age
##Gets user's first name
def get_first_name():
    while True:
        user_first_name = input("What is your first name? ")
        if(len(user_first_name) >= 2 and len(user_first_name) <= 20):
            return user_first_name
        else: 
            print("Please enter your first name. Must be between 2 and 20 characters.\n")
##Gets user's last name
def get_last_name():
    while True:
        user_last_name = input("What is your last name? ")
        if(len(user_last_name) >= 2 and len(user_last_name) <= 20):
            return user_last_name
        else:
            print("Please enter your last name. Must be between 2 and 20 characters.\n")
##Gets user's address
def get_address():
    while True:
        user_address = input("What is the two letter abbreviation for the state you reside in? ")
        if user_address.upper() in states:
            return user_address
        else:
            print("please enter the two letter abbreviation for the state you reside in. \n")
            continue
##Ask user if they would like to continue application
def continue_using_application():
    while True:
        voter_continue = input("Do you want to continue with Voter Registration? Please enter yes or no. ")
        if voter_continue.lower() == "yes":
            break
        elif voter_continue.lower() == "no":
            print("Have a great day!")
            exit()
        else:
            continue

##Running application
print("Welcome to the Python Voter Registration Application")
continue_using_application()
get_age()
continue_using_application()
voter_us_citizen = input("Are you a U.S. Citizen: ")
if voter_us_citizen.lower() != "yes":
    print("In order to vote in the United States, it is required that you are a U.S. Citizen. Please come back after obtaining U.S. Citizenship.")
else:
    continue_using_application()
    voter_first_name = get_first_name()
    continue_using_application()
    voter_last_name = get_last_name()
    continue_using_application()
    voter_address = get_address()
    continue_using_application()
    voter_zip = get_zip()
    print("Hello, " +voter_first_name+ " " +voter_last_name+ ". You have entered that your state is " +voter_address+ ", " + str(voter_zip) + ". You should receive your voter registration card within 3 weeks.")
