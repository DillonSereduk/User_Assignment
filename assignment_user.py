# For this assignment you will create the user class and add a couple methods!

# Attributes:
# On instantiation of a user, the following attributes should be passed in as arguments:

class User:

    def __init__(self, first_name, last_name, email, age):

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0



# Methods:
# display_info(self) - Have this method print all of the users' details on separate lines.

    def display_info(self):
        print("==========================================")
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Member: {self.is_rewards_member}")
        print(f"Current points: {self.gold_card_points}")
        print("===========================================")

    def enroll(self):
        
        if self.is_rewards_member:
            print("User already a member.")
            return False
        self.is_rewards_member = True
        self.gold_card_points = 200

    def spend_points(self, amount):
        if self.gold_card_points < amount:
            "You don't have enough points :("
        # decrease the user's points by the amount specified.
        self.gold_card_points -= amount
        # Add logic in the spend points method to be sure they have enough points to spend that amount and handle appropriately.
        


my_user = User("Dillon", "Sereduk", "blablabla@gmail.com", 20)
user_2 = User("Alex", "Buggs", "@hahahahgmail.com", 21) 

my_user.enroll()
my_user.display_info()
user_2.display_info()
