from spy_details import spy_name,spy_rating,spy_age


print "Hello buddy"
print "Let's get started"


STATUS_MESSAGE = ['EXAMPLE STATUS 1', 'EXAMPLE STATUS 2', 'EXAMPLE STATUS 3']
friends_name = ['Ram']
friends_age= [36]
friends_rating = [2.5]
friend_is_online = [True]




def add_status(c_status):
    if c_status != None:
        print "Your Current status is " + c_status
    else:
        print"Your don't have any status currently"
    existing_status = raw_input("You want to select from older status? Y/N")
    if existing_status.upper()=="N":
        new_status= raw_input("Enter your status: ")
        if len(new_status)>0:
            STATUS_MESSAGE.append(new_status)
    elif existing_status.upper()=="Y":
        serial_no = 1
        for old_status in STATUS_MESSAGE:
            print  str(serial_no)+"."+old_status
            serial_no = serial_no + 1
        user_choice = input ("Enter your choice: ")
        new_status = STATUS_MESSAGE[user_choice-1]
    updated_status = new_status
    return updated_status


def add_friend():
    frnd_name = raw_input("What is your name?")
    frnd_age = input("What is your age")
    frnd_rating = input("What id your rating?")
    if len(frnd_name)>2 and 12 <frnd_age<50 and frnd_rating>spy_rating:
        friends_name.append(frnd_name)
        friends_age.append(frnd_age)
        friends_rating.append(frnd_rating)
        friend_is_online.append(True)
    else:
        print "Friends cannot be added"
    return len(friends_name)
#defining function start_chat


def start_chat(spy_name, spy_age, spy_rating):

    print "Please select an option " + spy_name
    current_status = None

    show_menu= True
    while show_menu:
        choice = input("What do you want to do?  \n 1) Add a status. \n 2) Add a friend. \n 3) Send a message \n 4) Read a message \n 0) Exit. ")
        if choice == 1:
            current_status =  add_status(current_status)
            print "Updated status is " + current_status
        elif choice == 2:
            no_of_frnds = add_friend()
            print"You have " + str(no_of_frnds) + " friends"
        elif choice == 3:
            print"Will send a message"
        elif choice == 4:
            print"Will read a message"
        elif choice == 0:
            show_menu = False
        else:
            print"Invalid input"


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