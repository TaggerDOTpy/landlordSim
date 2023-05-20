from Functions.dialogueFunction import dialogue
from Functions.continueFunction import Pause

landlordName = input("What name do you want Yourself as the Landlord to have? ")
houseType = int(input("""What type of house to you want the person who will be paying the bills to have? 
1) Small house
2) Second story House
3) Mansion
Enter the Number to choose: """))
if houseType > 3:
    print('Invalid Answer!')

Pause()

clientName = input('What name do you want the person who will be paying the bills to be? ')
input("Hey " + clientName + "! I'm Your new landlord, I hope you will be paying your bills, Anyways Goodluck! ")
if houseType == 1:
    print('Ok... sigh*')
elif houseType == 2:
    print('Most definetly will!')
elif houseType == 3:
    print('Look at this mansion!!')
else:
    print('Please reopen this game, and only put 1 ~ 3 In the choices.')
Pause()

dialogue("-One month later- Hey " + clientName + " Heres this month's bills, Please pay them today.")
dialogue("Will! ")

Pause()

dialogue("-Tommorow- " + clientName + "! Why haven't you payed your bills? ")
if houseType == 1:
    input('Ohh Yeah, Now it makes sense. ')
elif houseType == 2:
    input("I mean, Don't you own a two story House? ")
elif houseType == 3:
    input("Look at this mansion!! Why can't you pay the bills? ")


evictChoice = input("""Evict? 
Y) Yes.
N) No.
(ENTER ANSWER IN CAPITALS) """)

if evictChoice == "Y":
    whileLoop = False
    print(f"But {landlordName}! -then {clientName} left his home depressed-")
    Pause()
    input('You have evicted the moneymaker. Now you can restart the game because you beat it!')
    input('Quit? ')
    quit()
elif evictChoice == "N":
    whileLoop = False
    print("You've lost the game, as you failed to evict someone who didn't pay the bills")
    Pause()
    input('Restart Or Quit?')
    quit()
