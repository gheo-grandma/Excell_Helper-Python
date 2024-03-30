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