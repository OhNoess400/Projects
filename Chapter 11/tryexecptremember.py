import json
def greet_user():
    filename='username.json'
    try:
        with open(filename) as f_obj:
            username=json.load(f_obj)
    except FileNotFoundError:
        usename= input("What's your username?\t")
        with open(filename,'w') as f_obj:
            json.dump(username, f_obj)
            print("We will remember you when you come back,",username+"!")
    else:
        print("Welcome back",username+"!")

greet_user()


favnumb=input("What's your favorite number?\n")
filename='favnumb.json'
with open(filename,'w') as f_obj:
    json.dump(favnumb,f_obj)
    print("I'll remember it!")

with open(filename) as f_obj:
    favnumb=json.load(f_obj)
    print("Welcome back! Your favorite number is",favnumb)
