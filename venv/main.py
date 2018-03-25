# THIS FILE WAS CREATED IN THIS DIRECTORY EARLIER, NOW MOIVED TO ROOT OF THE REPO


print "Hello buddy"
print "Let's get started"
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
            print "Authentication process completed successfully. Welcome " +spy_name+ "age: " + str(spy_age) + " and rating: " + str(spy_rating) + " Glad to have ypou with us."

        else:
            print "Sorry, you are not eligible to be a spy"
    else:
        print "Invalid Information."
else:
    print "Opps! please enter a valid name."
