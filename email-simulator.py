
# Email simulater - using classes and error handling

"""
In this workshop, you are going to build an Email Simulator that simulates sending, receiving, and managing emails between different users. You'll learn about classes, objects, and how to organize code in an object-oriented way.
"""

# how the code begun
class Email:
    def __init__(self, sender, receiver, subject, body):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body
        self.read = False

    def mark_as_read(self):
        self.read = True

email_obj = Email('alice@example.com', 'bob@example.com', 'Hello', 'Hi Bob!')
print(email_obj.sender)
print(email_obj.subject)
print(email_obj.read)
email_obj.mark_as_read()
print(email_obj.read)

# just upgradig slowly. 
class Email:
    def __init__(self, sender, receiver, subject, body):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body
        self.read = False

    def mark_as_read(self):
        self.read = True

class User:
    def __init__(self, name):
        self.name = name
        self.inbox = []

    def send_email(self, receiver, subject, body):
        email = Email(sender=self, receiver=receiver, subject=subject, body=body) # creating a new email
       
        receiver.inbox.append(email) # adding the email to the receiver's box

class Inbox: # handles emails operations
    def __init__(self):
        self.emails = []


# progress so far
class Email:
    def __init__(self, sender, receiver, subject, body):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body
        self.read = False

    def mark_as_read(self):
        self.read = True

class User:
    def __init__(self, name):
        self.name = name
        self.inbox = Inbox()

    def send_email(self, receiver, subject, body):
        email = Email(sender=self, receiver=receiver, subject=subject, body=body)
        receiver.inbox.receive_email(email)

class Inbox:
    def __init__(self):
        self.emails = []
    
    def receive_email(self, email):
        self.emails.append(email)

alice = User("Alice")
bob = User("Bob")

alice.send_email(bob, "Hello", "Hi Bob, how are you?")

print(len(bob.inbox.emails))


##
class Email:
    def __init__(self, sender, receiver, subject, body):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body
        self.read = False

    def mark_as_read(self):
        self.read = True

    def display_full_email(self):
        self.mark_as_read()
        print('\n--- Email ---')
        print(f'From: {self.sender.name}')
        print(f'To: {self.receiver.name}')
        print(f'Subject: {self.subject}')
        print(f'Body: {self.body}')
        print('------------\n')

    def __str__(self):
        status = 'Read' if self.read else 'Unread'
        return f"[{status}] From: {self.sender.name} | Subject: {self.subject}"
class User:
    def __init__(self, name):
        self.name = name
        self.inbox = Inbox()

    def send_email(self, receiver, subject, body):
        email = Email(sender=self, receiver=receiver, subject=subject, body=body)
        receiver.inbox.receive_email(email)

class Inbox:
    def __init__(self):
        self.emails = []

    def receive_email(self, email):
        self.emails.append(email)

    def list_emails(self):
        if not self.emails: # checks if inbox is empty by checking the email list
            print('Your inbox is empty.\n')
            return

# Final Full Code

import datetime

class Email:
    def __init__(self, sender, receiver, subject, body):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body
        self.timestamp = datetime.datetime.now()
        self.read = False

    def mark_as_read(self):
        self.read = True

    def display_full_email(self):
        self.mark_as_read()
        print('\n--- Email ---')
        print(f'From: {self.sender.name}')
        print(f'To: {self.receiver.name}')
        print(f'Subject: {self.subject}')
        print(f"Received: {self.timestamp.strftime('%Y-%m-%d %H:%M')}")
        print(f'Body: {self.body}')
        print('------------\n')

    def __str__(self):
        status = 'Read' if self.read else 'Unread'
        return f"[{status}] From: {self.sender.name} | Subject: {self.subject} | Time: {self.timestamp.strftime('%Y-%m-%d %H:%M')}"
class Inbox:
    def __init__(self):
        self.emails = []

    def receive_email(self, email):
        self.emails.append(email)

    def list_emails(self):
        if not self.emails:
            print('Your inbox is empty.\n')
            return
        print('\nYour Emails:')
        for i, email in enumerate(self.emails, start=1):
            print(f'{i}. {email}')


    def read_email(self, index):
        if not self.emails:
            print('Inbox is empty.\n')
            return
        actual_index = index - 1
        if actual_index < 0 or actual_index >= len(self.emails):
            print('Invalid email number.\n')
            return
        self.emails[actual_index].display_full_email()

    def delete_email(self, index):
        if not self.emails:
            print('Inbox is empty.\n')
            return
        actual_index = index - 1
        if actual_index < 0 or actual_index >= len(self.emails):
            print('Invalid email number.\n')
            return
        del self.emails[actual_index]
        print('Email deleted.\n')
        
class User:
    def __init__(self, name):
        self.name = name
        self.inbox = Inbox()

    def send_email(self, receiver, subject, body):
        email = Email(sender=self, receiver=receiver, subject=subject, body=body)
        receiver.inbox.receive_email(email)
        print(f'Email sent from {self.name} to {receiver.name}!\n')

    def check_inbox(self):
        print(f"\n{self.name}'s Inbox:")
        self.inbox.list_emails()

    def read_email(self, index):
        self.inbox.read_email(index)

    def delete_email(self, index):
        self.inbox.delete_email(index)

def main():
    tory = User('Tory')
    ramy = User('Ramy')        
    
    tory.send_email(ramy, 'Hello', 'Hi Ramy, just saying hello!')
    ramy.send_email(tory, 'Re: Hello', 'Hi Tory, hope you are fine.')
    ramy.check_inbox()
    ramy.read_email(1)
    ramy.delete_email(1)
    ramy.check_inbox()
    
if __name__ == '__main__':
    main()