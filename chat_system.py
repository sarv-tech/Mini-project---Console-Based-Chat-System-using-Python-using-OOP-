# Q. Letʼs create a Chat System using OOPs concepts We have to create classes : 
# •User 
# •Message 
# •ChatRoom

# And we have to implement functions:
# •sending messages
# •viewing chat history
# •user joining and leaving the chatroom



class Message:
    message_counter = 1              # class variable to generate unique message IDs

    def __init__(self, sender, content):
        self.sender = sender                 # stores User object who sent the message
        self.content = content                # actual message text
        self.id = Message.message_counter       # a  ssign unique ID
        Message.message_counter += 1            # increment ID for next message

    def __str__(self):
        return f"({self.id}) {self.sender.username}: {self.content}"


class User:
    def __init__(self, username):
        self.username = username                # username of the user
        self.chatroom = None                       # stores current chatroom reference

    def join_chatroom(self, chatroom):
        if self.chatroom:                           # check if user already in a chatroom
            print(f"{self.username} is already in a chatroom.")
        else:
            chatroom.add_user(self)                   # add user to chatroom
            self.chatroom = chatroom                   # set current chatroom
            print(f"{self.username} joined {chatroom.name}")

    def leave_chatroom(self):
        if not self.chatroom:                  # check if user is not in any chatroom
            print(f"{self.username} is not in any chatroom.")
        else:
            self.chatroom.remove_user(self)         # remove user from chatroom
            print(f"{self.username} left {self.chatroom.name}")
            self.chatroom = None                     # reset chatroom reference

    def send_message(self, content):
        if not self.chatroom:                    # user must be inside a chatroom
            print(f"{self.username} cannot send a message (not in a chatroom).")
        else:
            self.chatroom.broadcast(self, content)


class ChatRoom:
    def __init__(self, name):
        self.name = name                # chatroom name
        self.users = []                 # list of users in the chatroom
        self.messages = []              # list to store chat history

    def add_user(self, user):
        self.users.append(user)             # add user to chatroom

    def remove_user(self, user):
        self.users.remove(user)              # remove user from chatroom

    def broadcast(self, sender, content): 
        message = Message(sender, content)     # create new message object
        self.messages.append(message)         # store message in history
        print(message)

    def show_chat_history(self):
        print(f"\nChat History of {self.name}:")
        for msg in self.messages:
            print(msg)

# create a chatroom
if __name__ == "__main__":
    room = ChatRoom("Developer Club")

# Create Users
    u1 = User("Sarvesh")
    u2 = User("Rohan")
    u3 = User("Tommy")

# users joining chatroom
    u1.join_chatroom(room)
    u2.join_chatroom(room)

# users sending messages
    u1.send_message("Hi Everyone!!")
    u2.send_message("Hi Sarvesh!")

    u3.join_chatroom(room)
    u3.send_message("Hi Guys, What are you Doing?")

# display full chat history
    room.show_chat_history()

# users leaving chatroom
    u1.leave_chatroom()
    u2.leave_chatroom()
    u3.leave_chatroom()
