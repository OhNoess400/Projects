#user1={"Name":"John", "Age":21, "School": "Uni"}
#print(user1["Name"])
#print(user1["School"])
#intro=user1["Name"]
#print("His name is",intro,"!")
#print(user1)
#user1["Location"]="Moscow"
#user1["Fav Pet"]="Cat"
#print(user1)

#user2={}
#user2["Name"]="Samantha"
#user2["Age"]=22
#print(user2)

#user2["Name"]="Sam"
#print(user2)

#alien0={"x_position":0,"y_position":25,"Speed":"Medium"}
#print(alien0)
#print("\n")
#del alien0["y_position"]
#print(alien0)
#change=input("How fast would you like the alien to be? Please answer with 'fast','medium', or 'slow'\n")
#if change.lower()=="fast":
#    alien0["Speed"]="Fast"
#elif change.lower()=="medium":
#    alien0["Speed"]="Medium"
#elif change.lower()=="slow":
#    alien0["Speed"]="Slow"
#else:
#    print("Please enter:\nFast, Slow, or Medium!\nBeucase of innappropriate answer, changed speed to Medium.")
#print("Original X-position:",alien0["x_position"])


#if alien0["Speed"].lower()=="slow":
#    x_increment=1
#elif alien0["Speed"].lower()=="medium":
#    x_increment=2
#else:
#    x_increment=3

#alien0["x_position"]= alien0["x_position"]+x_increment

#print("New X-position:",alien0["x_position"])

#person={"Name":"Jimmy","Age":17,"City":"Cary"}
#person["LastName"]="Grimaldi"
#print(person["Name"])
#print(person["LastName"])
#print(person["Age"])
#print(person["City"])

#User0={"Name":"John",
#"Last":"Gauss",
#"User":"GJon",
#}
#for k,v in User0.items():
#    print("\tKey:",k)
#    print("\tValue:",v)

#fav_lang={"Jen":"Python","Sarah":"C","Edward":"Ruby","Phil":"Python"}
#friends=["Phil","Sarah"]
#for name in fav_lang.keys():
#    print(name.title())
#    if name in friends:
#        print("Hi",name.title(),", I see your favorite language is ", fav_lang[name].title(),"!")
#    else:
#        pass
#
#if "erin".title() not in fav_lang.keys():
#    print("Erin, please take the poll!\n\n")

#for name in sorted(fav_lang.keys()):
#    print(name.title(),", thank you for taking the poll!")

#print("\n\nThe following languages are mentioned:\n")
#for lang in set(sorted((fav_lang.values()))):
#    print(lang.title())

#pyglossary={"Arguement":"A value passed to a function (or method) when calling the function",
#"List":"Something that holds Strings, Integers and even other lists",
#"Tuple":"Basically Lists but cannot be modified after making unless you make a new one",
#"Looping":"Doing a thing over and over",
#"Dictionary":"Something that holds a key:value pair"}


#pyglossary["Object"]="Any data with a state"
#pyglossary["Parameter"]="A named entity in a function"
#pyglossary["Path Entry"]="A single location on the import path which the path based finder consults to find modules for importing"

#for k,v in pyglossary.items():
#    print("\nKey:  >",k)
#    print("\nValue:|",v)

#rivers={"Nile":"Egypt","Amazon":"Brazil","Yangtze":"China",
#"Mississippi":"America","Ob":"Russia"}

#for river, country in rivers.items():
#    print("\nThe",river.title(),"goes through",country.title())
#    print("\nRiver:",river)
#    print("Country:",country)


aliens=[]
for alien_number in range(30):
    new_alien={"color":"Green","points":5,"speed":"slow"}
    aliens.append(new_alien)

for alien in aliens[0:5]:
    alien["color"]="Yellow"
    alien["points"]=10
    alien["speed"]="Medium"

for alien in aliens[0:3]:
    if alien["color"]=="Green":
        alien["color"]="Yellow"
        alien["points"]=10
        alien["speed"]="Medium"
    elif alien['color']=="Yellow":
        alien["color"]="Red"
        alien["points"]="15"
        alien["speed"]="Fast"

for alien in aliens[0:5]:
    print(alien)
print("...")

#favorite_lang={
#"jen":["Python","Ruby"],
#"sarah":["C"],
#"edward":["Ruby","Go"],
#"phil":["Python","Haskell"],
#}

#for name,lang in favorite_lang.items():
#    print("\n",name.title(),"'s favorite languages are:")
#    for language in lang:
#        print("\t",language.title())
