from spy_details import spy, Spy, ChatMessage # importing variables from spydetails.py
from datetime import datetime # importing datetime library
import csv
from steganography.steganography import Steganography # importing Steganography library


def select_frnd():  # function to select a friend
    print"Select your friend"
    serial_no=1
    for frnd in friends:  # print list of friends
        print str(serial_no) + ". " + frnd.name
        serial_no=serial_no+1
    user_selected_frnd = input("Enter your choice: ")  # user selecting friend
    user_selected_frnd_index = user_selected_frnd-1
    return user_selected_frnd_index  # to return the selected friend index



def send_message():  # function for sending message
    selected_friend = select_frnd()  # calling the select_friend function
    original_image = raw_input("What is the origin name of the image : ")  # take name of original image as input
    secret_text = raw_input("Enter the secret message : ")  # entering the secret message
    output_path = "output.jpg"  # name of image after encoding the message
    Steganography.encode(original_image, output_path,secret_text)  # calling encode() function to encode message in image
    print "Message Encoded"
    # dictionary to store details of a message
    new_chat = ChatMessage(secret_text,True)

    friends[selected_friend]['chats'].append(new_chat)  # appending ghats in the friends list
    print "Your secret message is ready "


def read_message():  # function for reading message
    selected_friend=select_frnd()  # calling select_friend function
    output_path=raw_input("Which image you want to decode? ")  # the name of image to be decoded
    secret_text=Steganography.decode(output_path)  # calling decode()function to decode
    print "Decoded message is "+secret_text # printing the secret text
    # dictionary to store details of message
    new_chat = ChatMessage(secret_text,False)

    friends[selected_friend].chats.append(new_chat)
    print "Your secret message has been saved"


def add_friend():  # function to add friend
    # taking friends detail s input
    frnd = Spy ('','',0,0.0)
    frnd = {'name': "",'age':0,'ratings':0.0,'isonline':True,'chats':[]}  # dictionary for details of friend
    frnd.name =raw_input("What is your friend's name : ")
    frnd.sal = raw_input("What should we call you")
    frnd.age=input("What is the age :")
    frnd.rating=input("What are the ratings : ")
    frnd.is_online = True
    if len(frnd.name)>0 and 12<frnd.age<50 and frnd.rating>spy.rating: # checking for spy details
        # adding the details in the respective lists
        friends.append(frnd)
        with open('friends.csv','a') as friends_data:
            writer = csv.writer(friends_data)
            writer.writerow([frnd.name, frnd.sal, frnd.rating, frnd.age, frnd.is_online])
    else:
        print "The friend cannot be added "
    return len(friends)  # returning length of list friend_name


def add_status(c_status):  # function to add status
    if c_status!=None:  # checking if the status is none
        print "Your current status is : "+c_status  # printing the current status
    else:
        print "Currently you don't have any status"
    existing_status =raw_input("You want to add from old status Y/N? ")  # taking new status from user
    if existing_status.upper()=='N':
        new_status=raw_input("Enter your status : ")  # taking new status as input
        if len(new_status)>0:
            updated_status=new_status
            old_status.append(updated_status)  # adding the new status in the status list
        else:
            print "Enter a valid status "
    elif existing_status.upper()=="Y":  # checking if user want to add an old status
        serial_no=1
        for status in old_status:  # printing the old status
            print str(serial_no)+". "+status
            serial_no=serial_no+1
        status_choice=input("Enter your choice : ")
        updated_status=old_status[status_choice-1]  # updating the status
    return updated_status  # returning the new updated status


def spy_chat(spy_name,spy_age,spy_rating):  # function spy_chat to display menu
    current_status = None
    choice= -1  # choice variable set to -1
    print 'Here are your options ' + spy_name
    while choice!=0:  # while loop will run until user choose to exit
        print '     MENU     \n 1.Add a status \n 2.Add a friend \n 3.Send a message \n 4.Read a message\n 5.Read chat history \n 0.Exit'  # printing menu
        choice=input("Enter your choice:")  # taking choice input
        if choice == 1:  # choice 1
            current_status=add_status(current_status)
            print "Updated status is : "+current_status
        elif choice == 2:  # choice 2
            friend_no=1  # counter to print no. of friends
            no_of_friends=add_friend()  # calling function add_friend to add friend
            print " You have "+str(no_of_friends)+" number of friends"  # printing number of friends
            for i in friends:  # printing name of friends
                print str(friend_no)+". "+i['name']
                friend_no=friend_no+1
        elif choice == 3:
            send_message()  # calling send_message()function
        elif choice == 4:
            read_message()  # calling the read_message()function
        elif choice == 5:  # to read chat history
            read_history()

        elif choice == 0:  # to exit
            print 'Exit'
        else:  # for any invalid input
                print 'Invalid input'


f=datetime.now()  # calling function now() from datetime library
print f.strftime("%b %d %Y %H:%M:%S")  # use of stringtimeformat
print 'Hello...!! Welcome to ISpy Spychat.'  # printing hello
print 'Let\'s get started'
old_status=["Example status 1","Example status 2","Example status 3","Example status 4"]  # list of old status
frnd1 = Spy('Example','Mr.',23,2.5)
frnd2 = Spy('Example2','Mr.',25,3.5)
friends=[frnd1, frnd2]  # list to store friend details


def load_frnds():
    with open('friends.csv', 'rb') as friends_data:
        reader = csv.reader(friends_data)

        for row in reader:
            frnd  = Spy(name=row[0],salutation=row[1],age=row[3],rating=row[2])
            friends.append(frnd)


load_frnds()

spy_reply=raw_input('Are you a new user? Y/N')
if spy_reply .upper() == 'N':
    print'Welcome back ' +spy.name+ " your age is" +  str(spy.age)+ ' and ypur rating is ' + str(spy.rating)
    spy_chat(spy.name,spy.age,spy.rating)  # calling spy_chat



elif spy_reply.upper() == 'Y':
    spy = Spy("","",0,0.0)
    spy.name=raw_input('Enter your name ')  # take name as input

    if len(spy.name)>2:  # checking for length of the name
        print 'Welcome '+ spy.name + ' we are happy to have you with us.'  # concatenating strings
        salutation=raw_input('What should we call you (Mr.or Ms.) ' )
        if salutation == 'Mr.'or salutation == 'Ms.':  # using if
            spy.name=salutation+" "+spy.name
            print 'Alright '+spy.name+'. I\'d like to know a little bit more about you...'
            spy.age=input('What\'s your age ')
            if 50<=spy.age<=12:  # nested if statement to check range of age
                print 'You are not eligible to be a spy'
            else:
                spy.rating=input('What are your ratings ')  # taking ratings as input
                if spy.rating > 5:
                    print 'Great Spy!!'
                elif spy.rating > 3.5:  # elif statement for more than one condition
                    print 'Average Spy'
                elif spy.rating > 2.5:
                    print 'Need to work hard!!'
                else:
                    print 'Who hired you'
                spy_is_online = True
                print 'Authentication has been completed. Welcome ' + spy.name + '.Your age is ' + str(spy.age) + ' and your rating is ' + str(spy.rating)  # typecasting of integer to string
                spy_chat(spy.name,spy.age,spy.rating)  # calling function spy_chat

        else:
            print 'Please enter a vaild salutation'

    else:
        print 'Ooops! Please enter a valid name '