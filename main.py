from spy_details import spy_name,spy_rating,spy_age


print "Hello buddy"
print "Let's get started"

#defining function start_chat
def start_chat(spy_name, spy_age, spy_rating):
    print "Please select an option " + spy_name
    show_menu= True
    while show_menu:
        choice = input("What do you want to do?  \n 1) Add a status. \n 2) Add a friend. \n 0) Exit. \n ")
    if choice ==1:
        print"Will add a status"
    elif choice ==2:
        print"Will add a friend"
    elif choice ==0:
        show_menu= False
    else:
        print"Invalid input"

spy_name
spy_exist = raw_input("Are you a new user? Y/N? ")

if spy_exist.upper()=="N":
    print "Welcome back " + spy_name + " age: "+ str(spy_age) + " having rating "+ str(spy_rating)
    start_chat(spy_name,spy_age,spy_rating)


elif spy_exist.upper()=="Y":

    spy_name =  raw_input ("What is your spy name? ")
    if len(spy_name) >3:
        print "Welcome " + spy_name + ". Glad to have you with us."
        spy_salutation= raw_input("What's your title? ")
        if spy_salutation == "Mr." or spy_salutation =="Ms.":
            spy_name = spy_salutation + " " + spy_name
            print "Welcome " + spy_name + ". Let me know about you a bit more."
            spy_age = input("Please enter your age")
            if 50>spy_age>18:
                print "Your age is Correct."
                spy_rating = input("Please enter your rating ")
                if spy_rating>=5.0:
                    print "Great spy"
                elif 3.5<=spy_rating<5.0:
                    print "Good spy"
                elif 2<=spy_rating<3.5:
                    print "Not bad."
                else :
                    print "Not good. Need hardwork"
                spy_is_active = True
                print "Conratulations! authentication process completed successfully. Welcome " +spy_name+ "age: " + str(spy_age) + " and rating: " + str(spy_rating) + " Glad to have ypou with us."
                start_chat(spy_name,spy_age,spy_rating)
            else:
                print "Sorry, you are not eligible to be a spy"
        else:
            print "Invalid Information."
    else:
        print "Opps! please enter a valid name."
else:
    print"Invalid Entry"