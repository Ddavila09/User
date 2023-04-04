class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
    
    def display_info(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Is Rewards Member: {self.is_rewards_member}")
        print(f"Gold Card Points: {self.gold_card_points}")

    def enroll(self):
        if not self.is_rewards_member:
            self.is_rewards_member = True
            self.gold_card_points = 200
            print("User enrolled.")
        else:
            print("Already a member.")

    def spend_points(self, amount):
        if self.gold_card_points >= amount:
            self.gold_card_points -= amount
            print((amount), "Points spent.")
        else:
            print("Not enough points.")
        

user1 = User("David", "Davila", "DavidD@mail.com", 29)
user2 = User("Amy", "Davila", "AmyD@mail.com", 29)
user3 = User("Loki", "Davila", "LokiD@mail.com", 3)


user1.spend_points(50)
user1.display_info()
user1.enroll()
print(user1.gold_card_points)

user2.display_info()
user2.enroll()
user2.spend_points(80)
print(user2.gold_card_points)

user3.display_info()
user3.spend_points(40)
