#car=input("What kind of rental car would you like?\n")
#print("Okay, let me see if I can get a",car.title(),"for you!")

#numba=input("How many people are in your dinner group?\n")
#if int(numba) >= 8:
#    print("Sorry, You guys will have to wait for a table")
#elif int(numba) < 8:
#    print("Your table is ready.")

#curr_num=0
#while curr_num <=5:
#    curr_num+=1
#    print(curr_num)

#prompt="\nTell me something and I will repeat it back to you!"
#prompt+="\nEnter 'quit' to end the program\t\t"
#message=""
#while message !="quit":
#    message=input(prompt)
#    if message != "quit":
#        print(message)
#prompt="\nPlease enter a Pizza Topping"
#prompt+="\nEnter 'quit' to display the selected toppings\n"
#message=""
#while message.lower() !="quit":
#    message=input(prompt)
#    if message.lower() !="quit":
#        print("I'll add that to the Pizza!")
#
#age=""
#while age =="":
#    age=input("\nPlease enter your age:\n")
#    if int(age) < 3:
#        print("Your entry is free!")
#    elif int(age)< 12:
#        print("Your entry fee is $10")
#    else:
#        print("Your entry fee is $15")

#inp=input("Do you want an Infinite loop?\n")
#if inp.lower()=='yes':
#    infinity="This goes on forever."
#    while infinity=="This goes on forever.":
#        print(infinity)
#else:
#    print("Okay")

sandwich_orders=["Turkey","Salami","Chicken","Ham","BLT","Meatball",
"Pastrami","Pastrami","Pastrami"]
finished_sandwiches=[]
print("We are currently out of Pastrami.\n")
while "Pastrami" in sandwich_orders:
    sandwich_orders.remove("Pastrami")

while sandwich_orders:
    Making_sandwiches=sandwich_orders.pop()
    print("I am making your", Making_sandwiches,"sandwich")
    finished_sandwiches.append(Making_sandwiches)

print("\n\nHere is a list of finished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)
