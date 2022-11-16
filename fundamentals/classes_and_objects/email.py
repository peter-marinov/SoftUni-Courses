# class Animal:
#     species = 'Humans'
#
#     def __init__(self, name):
#         self.name = name
#
# test_obj = Animal('Ivan')
# print(test_obj.name)
# print(test_obj.species)

class Email:
    def __init__(self,sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"

emails = []

while True:
    command = input()

    if command == "Stop":
        break

    sender, receiver, content = command.split(' ')
    email = Email(sender, receiver, content)
    emails.append(email)

send_email = [emails[int(x)].send() for x in input().split(', ')]
print(emails[0].sender)
for email in emails:
    print(email.get_info())