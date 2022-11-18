#
phonebook_dict = {'Alice': '703-493-1834', 'Bob': '857-384-1234', 'Elizabeth': '484-584-2923'}
print(phonebook_dict["Elizabeth"])
#
phonebook_dict["Kareem"] = "968-489-1234"

del phonebook_dict['Alice']

phonebook_dict["Bob"] = "968-345-2345"

#for key , value in phonebook_dict.items():
# print(f"The phone number of {key} is {value}")
#
ramit = { 'name': 'Ramit', 'email': 'ramit@gmail.com', 'interests': ['movies', 'tennis'], 'friends': [ { 'name': 'Jasmine', 'email': 'jasmine@yahoo.com', 'interests': ['photography', 'tennis'] }, { 'name': 'Jan', 'email': 'jan@hotmail.com', 'interests': ['movies', 'tv'] } ] }
print(ramit["email"])
print(ramit["interests"][0])
print(ramit["friends"][1])




# 