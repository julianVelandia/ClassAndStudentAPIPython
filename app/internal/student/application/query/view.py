class View:
    def __init__(self, email):
        self.email = email

    def get_email(self):
        return self.email

    @classmethod
    def new_view(cls, email):
        return cls(email)
