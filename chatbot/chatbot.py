import json

from datetime import datetime
from util import check_email_regex, check_name_regex

"""
each of the points in the flowchart will have a distinct function that 
will return the possible options as their return value. 

if the possible options are only Yes and No, the function will return True or False
if there are more than two possible options, the return value will be a descriptive 
string, or necessary object to continue the flow
"""

"""
----TRACKING NUMBER FUNCTIONS----
"""

# lets the customer know that the tracking number should be in their email and reminds 
# them to check their spam folder. asks if they were able to find the number 
# returns True (yes) or False (no)
def remind_and_confirm_tracking_number():
    print("When you ordered your package, you should have receieved a confirmation email with your tracking number from ___ @ ___ .com.")
    print("Please check your inbox, as well as your spam and junk mail folders to see if you can find it.")

    result = input("Were you able to find it? Please type 'yes' or 'no' \n").lower().strip()

    while result != 'yes' and result != 'no':
            result = input("Invalid value. Please type 'yes' or 'no'. \n").lower().strip()
    
    if result == 'yes':
        print("Great! Let's locate your package now.")
        return True
    else:
        print("No problem. You have the option of submitting a service request instead.")
        return False


# asks the customer if they have a tracking number and returns True (yes, they have it)
# or False (no, they don't have it)
def has_tracking_number():
    result = input("First, do you have your tracking number on hand? Please type 'yes' or 'no'. \n").lower().strip()

    while result != 'yes' and result != 'no':
            result = input("Invalid value. Please type 'yes' or 'no'. \n").lower().strip()
    
    if result == 'yes':
        return True
    else:
        return remind_and_confirm_tracking_number()
    
# collects and returns the tracking number
def collect_tracking_number():
    tracking_number = input("Enter your tracking number below. It should be a number that's ten digits long.\n")

    while len(tracking_number) != 10 or not tracking_number.isdigit():
        tracking_number = input("Invalid value. Please type in a tracking number that is 10 digits long.\n")

    return tracking_number


# looks up the package given the tracking number and returns the package information in the form of a dict 
# returns None if no such package exists. We only ever open the database if we get to this function.
def lookup_package(tracking_number, database_file):
    packages = []
    try:
        with open(database_file, 'r') as f:
            packages = json.load(f)
    except Exception as e:
        print("We're sorry, something went wrong with our packages database. We're working on fixing it! Please try again later.")
        return -1 # can't just check for a falsey value, since no such package may exist
    
    result = "yes"
    while result == "yes":
        for package in packages:
            if str(package["Tracking Number"]) == tracking_number:
                return package 
            
        result = input("Sorry, I couldn't find your package in the database. Would you like to try entering your tracking number again? Please type 'yes' or 'no'\n").lower().strip()
        while result != 'yes' and result != 'no':
            result = input("Invalid value. Please type 'yes' or 'no'. \n").lower().strip()

        if result == "yes":
            tracking_number = collect_tracking_number()
        else:
            print("I'm sorry I wasn't able to find your package in our database. You have the option of submitting a service request.")
            return None
        
    return None

# given the package (dict), display the package information to the customer
# returns the package status 
def display_package_info(package):
    print(f"Your package is currently at: {package["Current Location"]}.")
    package_status = package["Status"]

    if package_status == "On Track":
        print("Great news! Your package is on track.")
        print(f"It is expected to be delivered on {package["Expected Delivery Date"]}.")
        return package_status

    elif package_status == "Delayed":
        print("We're sorry, but your package has been delayed.")
        print ("You have the option of submitting a service request, so that a member of our team can follow up with more information.")
        return package_status
    
    elif package_status == "Delivered":
        print(f"Your package is marked as delivered. It was delivered on {package["Expected Delivery Date"]}.")
        print("If you have not received your package, you have the option of submitting a service request, so that a member of our team can follow up with further instructions.")
        return package_status
    
"""
----NO TRACKING NUMBER FUNCTIONS----
"""

# asks the customer whether they would like to escalate their specific problem to the 
# service department. returns True (yes) or False (no)
def confirm_escalation():
    result = input("Would you like to submit a service request? Please type 'yes' or 'no'. \n").lower().strip()

    while result != 'yes' and result != 'no':
            result = input("Invalid value. Please type 'yes' or 'no'. \n").lower().strip()
    
    if result == 'yes':
        return True
    else:
        return False

# collects information to file a complaint with the service department
# optionally, include the package information. returns the complaint in a dict form.
def collect_complaint(package=None):
    print("Good news! I can help you submit your service request right here in the chat window. But first, I'll need to collect some more information.")

    name = input("Please enter your first and last name.\n") 
    while not check_name_regex(name):
        name = input("Invalid value. Please enter your first and last name.\n")
    
    email_address = input("Thanks! Now, please enter the email address you used when you ordered the package.\n")
    while not check_email_regex(email_address):
        email_address = input("Invalid value. Please enter a valid email address.\n")

    problem_description = input("Thanks! Now, please enter a brief description of your issue, so our team can get started on fixing it right away.\n")

    complaint = {
        "Time": datetime.now(),
        "Name": name, 
        "Email Address": email_address, 
        "Package Information": package,
        "Problem Description": problem_description 
    }

    # TODO: create a file for complaints and dump the complaints in there 

    print("Thank you so much! I was able to generate a service request for you. A member of our service team should be in touch with you shortly.")  
    return complaint 

# thanks the customer and exits the conversation 
def end_conversation():
    print("Thank you for using TrackBot! Have a lovely day :)") 
    return


"""
----MAIN CHATBOT FLOW--------------------------------------------------------------------------------------------------------------
"""

def chatbot_flow():
    print("Hi! My name is TrackBot. I'm here to help you find your lost package. Let's get started.")

    exists_tracking_number = has_tracking_number()

    # they have the tracking number:
    if exists_tracking_number:
        
        tracking_number = collect_tracking_number()

        package = lookup_package(tracking_number, "packages.json")

        if package == -1: # there is something wrong with the db, check this FIRST
            end_conversation()
            return
        
        elif package: # package exists
            package_status = display_package_info(package)
            if package_status == "On Track": # we don't need to collect a complaint, everything is tickety-boo.
                end_conversation() 
                return

            elif package_status == "Delayed" or package_status == "Delivered": # something is wrong, give option to complain.
                escalate = confirm_escalation()
                if escalate:
                    collect_complaint()
                    end_conversation()
                    return
                else:
                    end_conversation()
                    return 

        else: # no such package in the db.
            escalate = confirm_escalation()
            if escalate:
                collect_complaint()
                end_conversation()
                return
            else:
                end_conversation()
                return

    # the customer doesn't have the tracking number on hand
    else: 
        escalate = confirm_escalation()
        if escalate:
            collect_complaint()
            end_conversation()
            return
        else:
            end_conversation()
            return()
             



chatbot_flow()