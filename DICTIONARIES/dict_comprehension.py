import random
city_names = ['Paris', 'Gaya', 'Patna', 'Delhi']

# new_dict = {new_key:new_value for city in city_name}

new_dict = {city: random.randint(20,30) for city in city_names}
print(new_dict)

above25 = {city: temp for (city, temp) in new_dict.items() if temp > 25}
print(above25)

order = {
    "starter": {1: "Salad", 2: "Soup"},    
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},    
    "dessert": {1: ["Ice Cream"], 2: []},
}
print(order["main"][1][0])