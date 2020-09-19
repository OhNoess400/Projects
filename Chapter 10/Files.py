#with open('pi_digits.txt') as file_object:
#    contents=file_object.read()
#    print(contents)

#with open('pi_digits.txt') as file_object:
#    contents=file_object.read()
#    print(contents.rstrip())

with open('pi_digits.txt') as file_object:
    lines= file_object.readlines()

pistring=''
for line in lines:
    pistring+=line.strip()

print(pistring)
print(len(pistring))

filename='pi_million_digits.txt'

with open(filename) as file_object:
    lines=file_object.readlines()
million_digits=''
for line in lines:
    million_digits+=line.strip()
birthday=input("Enter your birthday, in the form 'mmddyy':\n")
if birthday in million_digits:
    print("Your birthday is in the first million digits of  PI!")
else:
    print("Your birthday does not appear in the first million digits of PI. :(")

with open('learining_python.txt') as file_object:
    lines=file_object.read()
    print(lines)
print("\n\n")
with open('learining_python.txt') as file_object:
    lines=file_object.readlines()
lines_py=""
for line in lines:
    print(line)
print("\n\n")
with open('learining_python.txt') as file_object:
    lines=file_object.readlines()
lines_py=""
for line in lines:
    line.replace('Python','Ruby')
    lines_py+=line
print(lines_py)
linespy=lines_py.replace('Python','Ruby')
print(linespy)

filename='programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I live in the US.\n")

with open(filename,'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that run in a browser.\n")


filename='guest.txt'

with open(filename,'a') as file_object:
    while True:
        message=input("What's your name?\nType 'q' to exit.\n")
        if message.lower()=='q':
            print("Program succesfully ended.")
            break
        elif message.strip()==" ":
            print("Please re-run the program, this is a required field.")
            break
        elif message.strip()=="":
            print("This is a required feild.")
        else:
            file_object.write(str(message.title())+"\n")
