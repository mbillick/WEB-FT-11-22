# I want to ask the user for their name
# I want to ask the user for their password
# and i want to give them the ability to print out
#  specifics about them
# when the user types "n", we will end the program


# userChoice = input("Phone Number Search: Input Number Here \n")


class Contact:
    def __init__(self,name,phonenumber):
        self.name = name
        self.phonenumber = phonenumber
    def listOfContacts(self):
        print(f"{self.name}")
    def printMyName(self):
        print(f"My name is {self.name}")

    def printMyPhonenumber(self):
        print(f"My phonenumber is {self.phonenumber}")

user1 = User(userChoice, "1234")

keepGoing = "y"

while(keepGoing == "y"):

    print("""
    1. Password
    2. Name
    """)
    choice = input("what do you want to search for?\n Choose 1 for Name Search, choose 2 for Name Search\n")
    if(choice == "2"):
        user1.printMyName()
    if(choice == "1"):
        user1.printMyPassword()
    if(choice != "1" or choice != "2"):
        print("Dude please pick a valid choice")
    keepGoing = input("Do you want to keep going? y or n \n")