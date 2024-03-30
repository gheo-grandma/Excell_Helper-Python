To test this, create a file called conf.py and copy this code:

class Credentials():
    def __init__(self):
        self.sender_email = '<something>@gmail.com'
        self.receiver_email = '<something>@gmail.com'
        self.pw = '<something>'
        

    def get_sender(self):
        return self.sender_email

    def get_receiver(self):
        return self.receiver_email
    
    def get_pw(self):
        return self.pw


Instead of "something", insert your values.

This is a security system to prevent sharing sensitive informations.



WHAT DOES THIS PROGRAM DO?
This program is meant to support my girlfriend at work: it scans an excel file where she keeps stored the names of the employee who take certain courses.
Since many courses expire and need to be taken again, this program checks for any course that expires soon and sends her an email with employee's name, course and days left before expiration.
The program creates nested dictionaries in the form of {name : {course : day_left, course : days_left }, name : {course : days_left}}; sort of like a JSON file.