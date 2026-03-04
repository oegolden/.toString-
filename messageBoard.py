import sqlite3

class MessageBoard:
    def __init__(self, moderator, name):
        self.moderator = moderator
        self.name = name
        self.messages = []
        
    def add_message(self, message):
        self.messages.append(message)

    def get_messages(self):
        return self.messages
    
    def clear_messages(self, user, message_id):
        if user == self.moderator:
            self.messages.clear()
        else:
            user.send_message(f"You do not have permission to clear messages. Only the moderator '{self.moderator}' can clear messages.")