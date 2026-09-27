#Define the menu of restaurant
menu = {
'Pizza', 
'Pasta', 
'Salad', 
'Soup',
'Coffe',
'Tea'
}

price = { 'Pizza': 75, 'Pasta': 50, 'Salad': 45, 'Soup': 30, 'Coffe': 20, 'Tea': 18 }

#dikasih ucapan welcome duls
print("Welcome to our SNAPE Reastaurant!")
print("Here is our menu:")

#Perulangan For
for item in menu:
    print(f"{item}: ${price[item]}")
