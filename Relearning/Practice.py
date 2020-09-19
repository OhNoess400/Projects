user={'Username':"John","Password":"John11"}
tries=0
loginU=input("Please enter your username:\n") #Asks for user username
while tries < 2:
    if loginU.lower()!= user['Username'].lower():
        tries+=1
        print("That's not the right username!")
    else:
        pass
    loginP=input("Please enter your password:\n") #Asks for User pass
    if loginP.lower()!= user['Password'].lower():
        tries+=1
        print("That's not the right password!")
    else:
        print("Welcome back,",user['Username'].title()+'!')
        break
