class PhoneBook:
    def __init__(self):
        self.phonenumbers = []
    def printList(self):
       counter = 1
    for number in self.phonenumbers:
           print(f"""
            {counter}: {number["name"]} - {number["phoneNumber"]}
            """) 
        counter+= 1
    def addNumber(self,phoneNumber):
        self.phonenumbers.append)        
     def deleteNumber(self,number):
        self.phonenumbers,pop(number)        


mkesPhoneBook = PhoneBook()
usersChoice = ""
while(True):
    if (usersChoice == "Y"):
    break
    userNumber = input()
    userName = input()
    entry = {"phoneNumber"}
    mikesPhoneBook(entry)
    numberToDelete = int(input("What number would you like to delete?")
    mikesPhonebook,delNumber(numberToDelete)
    usersChoice = input("Do you want to stop?")