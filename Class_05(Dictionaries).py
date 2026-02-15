#Dictionary are used to store data in key-value pairs
#Dictionary are mutable.
#They are unordered, mutable and indexed by keys.
#Syntax: {key:value}

info ={
    "name":"Ali",
    "age":20,
    "gender":"Male",
    "city":"Karachi"
}

print(info)

# Another Example:

info = {
    "name": "Ahmad",
    "age": 35,
    "gender": "Male",
    "city": "Islamabad",
    "zip": "12345",
    "country": "Pakistan",
    "list": ["Java", "Python", "C#", "C"],
    "tuple": ("Dictionary", "Set", "List", "Tuple")
}


#Another Example:

info = {
    "name": "Umar",
    "age": 45,
    "gender": "Male",
    "city": "Islamabad",
    "zip": "12345",
    "country": "Pakistan",
    "list": ["Java", "Python", "C#", "C"],
    "tuple": ("Dictionary", "Set", "List", "Tuple")
}
    


# Another Example:

info ={
    "name":"Kamran",
    "age":25,
    "gender":"Male",
    "city":"Karachi",
    "is_adult": True,
    "courses":["Math","Science","English"],
    "address":{
        "street":"123 Main St",
        "city":"Islamabad",
        "zip":"12345",
        "country":"Pakistan"
    },
    "list": [ "Java", "Python","C#" , "C"],
    "tuple":("Dictionary", "Set", "List", "Tuple")
}
print(info["address"])
print(info["list"])
print(info["tuple"])
print(info["courses"])


# #Accessing elements:

# print(info["name"])
# print(info["age"])
# print(info["gender"])
# print(info["city"])

# #Adding elements:

# info["email"]="[EMAIL_ADDRESS]"
# print(info)

# #Updating elements:

# info["age"]=21
# print(info)

# #Removing elements:

# del info["city"]
# print(info)

# #Removing last element:

# info.popitem()
# print(info)

# #Removing specific element:

# info.pop("age")
# print(info)

# #Clearing dictionary:

# info.clear()
# print(info)

#They are unordered, mutable and indexed by keys.
#They are unordered, mutable and indexed by keys. 