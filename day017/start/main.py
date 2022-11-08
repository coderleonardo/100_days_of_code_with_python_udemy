class User:
    # constructor
    # is call every time that we create a new object
    def __init__(self, user_id, username):
        # initialize attributes
        print("__init__")

        self.id = user_id
        self.username = username
        self.followers = 0 # we can set default attributes
        self.following = 0

    # method
    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001", "Leonardo")
user_2 = User("002", "Ana")

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)