class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __str__(self):
        return f"User(username='{self.username}', email='{self.email}')"

class Moderator(User):
    def __init__(self, username, email):
        super().__init__(username, email)

    def send_message(self, message):
        print(f"Moderator '{self.username}' sends message: {message}")