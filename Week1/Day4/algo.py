dog = {
    "name": "Bear",
   "breed": "German Shepherd",
   "age": 3,
   "ageUnits": "years",} 


print(dog["breed"])
#owner
dog["owner"] = "Jessika"
print(dog)
dog["owner"] = "Michael"
dog["age"] = dog["age"] + 1
dog["name"] = "woof woof"
dog["tailLength"] = "12 in"
print(dog

print(dog.keys()))
dogValues = dog.values()
print(dogValues)

for key,value in dog.items():
    #print("my dogs %s %s" % (value,key))
print(f"my dogs {key} is {value}")
