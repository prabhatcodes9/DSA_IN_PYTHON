class StarCookie:
    def __init__(self, color, weight):
        self.color = color
        self.weight = weight

star_cookie1 = StarCookie("Red", 15)
print(star_cookie1.weight)
print(star_cookie1.color)

# star_cookie2 = StarCookie()
# star_cookie2.weight = 16
# star_cookie2.color = "Yellow"
# print(star_cookie2.weight)
# print(star_cookie2.color)

class Youtube:
    def __init__(self, username, subscribers):
        self.username = username
        self.subscribers = subscribers

user1 = Youtube("Prabhat", 0)
print(user1.username)
print(user1.subscribers)