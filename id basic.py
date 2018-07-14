restart="y"
while restart=="y":
    
    #inputs
    name=input("what's your name?\n")
    birthday=int(input("what year were you born in?\n"))
    age=2018-birthday

     #age
    age=2018-int(birthday)
    if age>=150:
        age=str(age)+" (deceased)"
        eyes="x x"

    elif age<=0:
        age="(unborn) eta "+(str(age)).strip("-")+" years"
        eyes="_ _"

    else:
        eyes="o o"
            
    #space calculations
    namespace=20-len(name)
    agespace=21-len(str(age))
    birthspace=16-len(str(birthday))

    #the card
    print(" _________________________________ ")
    print("|  ___                            |")
    print("| /o o\                           |")
    print("| \_-_/  Name:"+name.title()+" "*namespace+"|")
    print("|  _|_   Age:"+str(age)+" "*agespace+"|")
    print("|   |    Birthday:"+str(birthday)+" "*birthspace+"|")
    print("|  / \                            |")
    print("|_________________________________|")
    print("")

    restart="n"
    restart=input("start over? y/n: ")
    print("")
