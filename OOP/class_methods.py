class Youtube:
    def __init__(self, username, subscribers=0, subscription=0):
        self.username = username
        self.subscribers = subscribers
        self.subscription = subscription

    def subscribe(self, user):
        user.subscribers += 1
        self.subscription +=1


user1 = Youtube("Prabhat")
user2 = Youtube("Elshad")
user1.subscribe(user2) 
print(user1.subscribers)
print(user1.subscription)
print(user2.subscribers)
print(user2.subscription)