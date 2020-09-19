#age_1=15
#age2=12

#print(age_1<=15 and age2>=12)

#age1=12
#age2=14
#print(age1>23 or age2>57)

#bannedU=["Marie","Jonah","Nicole"]
#User="Marie"
#if User in bannedU:
#    print("L. You got banned, hold this. L")

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#
#alienC="red"
#alienC="green"
#alienC="yellow"
#if alienC.lower() =="green":
#    print("You got 5 points!")
#elif alienC.lower() =="yellow":
#    print("You got 10 points!")
#else:
#    print("You got 15 points!")

#age=input("What is your age?\n")

#if int(age) < 2:
#    print("That person is a baby")
#elif int(age) < 4:
#    print("That person is a toddler")
#elif int(age) < 13:
#    print("That person is a kid")
#elif int(age) < 20:
#    print("That person is a teenager")
#elif int(age) < 65:
#    print("That person is an Adult")
#elif int(age) > 64:
#    print("That person is an elder")
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!#
#UserN=["DaBe5t","admin","S4m4nth4","Rikkyyyy","J0hnn5mith"]
UserN=[]

if not UserN:
    print("We need to find more users!")
else:
    pass

for name in UserN:
    if name.lower()=="admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello ",name,", good to see you again")

currentU=["Maria","John","Lenny","Orange"]
newU=["Maria","ORANGE","Johnny","Lenny2"]
for user in newU:
    if user.title() in currentU:
        print("Sorry, That username is already in use")
    else:
        print("That name is available!")

num=[1,2,3,4,5,6,7,8,9]
for num in num:
    if num ==1:
        print(str(num)+"st")
    elif num==2:
        print(str(num)+"nd")
    elif num==3:
        print(str(num)+"rd")
    else:
        print(str(num)+"th")
