class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def sent(self):
        self.is_sent = True
        return self.is_sent

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


messages = list()
command = input()

while command != "Stop":
    data = command.split()
    who_sends = data[0]
    who_receives = data[1]
    what_is_the_content = data[2]
    email = Email(who_sends, who_receives, what_is_the_content)
    messages.append(email)
    command = input()

new_command = input()
index = list(map(int, new_command.split(", ")))
for number in index:
    messages[number].sent()

for email in messages:
    print(email.get_info())
