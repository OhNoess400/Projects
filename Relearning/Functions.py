

#def greet():
#    """Display a greeting"""
#    print("Hello")

#greet()

#def make_shirt(size=21, text="I love python"):
#    print("The size of the shirt is",size)
#    print("The shirt says",text)

#make_shirt(15,"What's up?")
#make_shirt(size=15,text="What's up?")

#make_shirt()
#make_shirt(size=15)
#make_shirt(size=15,text="I donut :)")

#def format(first,last):
#    full=first + " " + last
#    return full.title()

#firstn="jon"
#lastn="smith"
#full=format(firstn,lastn)
#print(full)

#def formatN(first,last,middle=""):
#    full=first + " " + middle + " " + last
#    return full.title()
#name=formatN("John","Smith")
#name2=formatN("John","Smith","N")
#print(name)
#print(name2)
#
#def formatN_D(firstn,lastn,middlen=""):
#    person={"First":firstn.title(),"Last":lastn.title(),"Middle":middlen.title()}
#    return person
#
#fname="jimi"
#lname="hendrix"
#mname="lee"
#full=formatN_D(fname,lname)
#full2=formatN_D(fname,lname,mname)
#print(full)
#print(full2)

#def formatN(firstn,lastn):
#    fulln=firstn+" "+lastn
#    return fulln

#while True:
#    print("\nPlease enter your name")
#    print("(Enter 'q' to quit)\n")
#    first=input("Please enter your first name:\n")
#    if first.lower()=="q":
#        break
#    last=input("Please enter your last name:\n")
#    if last.lower()=="q":
#        break
#
#    full=formatN(first,last)
#    print("Hello,",full.title())

def city_country(city, country):
    location=city.title()+","+" "+country.title()
    return location

#city1="New York"
#country1="America"
#city2="madrid"
#country2="spain"
#city3="kathmandu"
#country3="nepal"
#c1=city_country(city1,country1)
#print(c1)
#c2=city_country(city2,country2)
#print(c2)
#c3=city_country(city3,country3)
#print(c3)

#def make_album(Art_name,Alb_title,Alb_Numb=""):
#    artInfo={"Artist":Art_name,"Album":Alb_title}
#    if Alb_Numb:
#        artInfo={"Artist":Art_name,"Album":Alb_title,"Number of Songs":Alb_Numb}
#    else:
#        artInfo={"Artist":Art_name,"Album":Alb_title}
#    return artInfo

#artist="Pentakill"
#AlbumName="Sett, The boss"
#AlbumLength=12
#alb1=make_album(artist,AlbumName)
#alb2=make_album(artist,AlbumName,AlbumLength)
#print(alb1)
#print(alb2)

#while True:
#    print("Give me some info about the Album!")
#    print("(press 'q' at any time to quit.)\n\n")
#    fName=input("What's the name of the Artist?\n")
#    if fName.lower()=='q':
#        break
#    aName=input("What is the name of the Album?\n")
#    if aName.lower()=="q":
#        break
#    aLength=input("How many songs are in the Album,?\n(Leave blank for none)\n")
#    if aLength.lower()=='q':
#        break
#    if aLength=="":
#        fAlbum=make_album(fName, aName)
#    else:
#        fAlbum=make_album(fName, aName, aLength)
#
#    print(fAlbum)

#magicians=["David Copperfeild","Harry Houdini","David Blaine"]
#
#def show_magicians(magicians):
#    for magician in magicians:
#        print(magician)
#show_magicians(magicians)
#print("\n")
#def make_great(magicianss):
#    for magician in magicianss:
#        magician="Great "+ magician
#        print(magician)
#make_great(magicians)
#print("\n")
#print(magicians)
def topping(*toppings):
    print(toppings)
topping("chicken")
topping("Chicken","Mushrooms")

from testdef.py import sandwiches

testdef.sandwiches("Chicken","Tomato")
