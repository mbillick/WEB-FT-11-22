# kiss it simple
# 


class Phonebook:
    def __init__(self):
        self.listOfPhoneNumbers = []
        self.listOfPhoneNumbers = []
    def addEntry(self,usersEntry):
        self.listOfPhoneNumbers.append(usersEntry)
    def printListOfNumbers(self):
        for number in self.listOfPhoneNumbers:
            print(f"""
           {number["name"]} : {number["number"]} 
            """)

myPhoneBook = Phonebook()
userChoice = ""
while(True):
    if(userChoice == "y"):
        break
    def Remove
    userName = input("What is your name?\n")
    phoneNumber = input("What is your phone number?\n")
    usersEntry = {"name": userName, "number":phoneNumber}
    myPhoneBook.addEntry(usersEntry)
    myPhoneBook.printListOfNumbers()
    userChoice = input("Do you want to quit? y/n?")