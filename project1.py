#Define the menu of restaurant a.k.a warkop ala-ala
#Restauran ala-ala aja

menu = [
'Mie Ayam', 'Bakso Tenis', 'Nasi Goreng', 'Kwetiaw', 'Ketoprak'
'Kopi', 'Teh Manis', 'Es Jeruk', 'Teh Sereh Lemongrass', 'Es Cendol Telang'
]

#Harga satuan item
price = { 'Mie Ayam': 14000, 'Bakso Tenis': 12000, 'Nasi Goreng': 10000, 'Kwetiaw': 15000, 'Ketoprak': 8000, 'Kopi': 5000, 'Teh Manis': 4000, 'Es Jeruk': 6000, 'Teh Sereh Lemongrass': 5500, 'Es Cendol Telang': 7000 }

#kasih ucapan welcome duls
print("Welcome to our SNAPE Sesebeuhan!")

print("Here is our menu:")
for i, item in enumerate(menu, start=1):
    print(f"{i}. {item} - ${price[item]}")

total_order = 0

pilihan_1 = input("Please enter the first item you would like to order (Number or Name): ").lower().strip()

item_1 = None
if pilihan_1.isdigit():
    index = int(pilihan_1) - 1
    if 0 <= index < len(menu):
        item_1 = menu[index]
    else:
        for m in menu:
            if m.lower() == pilihan_1:
                item_1 = m
                break

if item_1 in menu:
    total_order += price[item_1]   #total pesanan + harga item yang dipesan
    print(f"{item_1} has been added to your order.")
    print(f"Total so far: ${total_order}")
else:
    print(f"Sorry, {pilihan_1} is not on the menu.")

#memasukkan input untuk item kedua
another_order = input(f"\nDo you want to another item? (y/n): ").strip().lower()

if another_order == "y":
    pilihan_2 = input("Please enter the second item you would like to order (Number or Name): ").lower().strip()
    item_2 = None
    if pilihan_2.isdigit():
        index = int(pilihan_2) - 1
        if 0 <= index < len(menu):
            item_2 = menu[index]
    else:
        for m in menu:
            if m.lower() == pilihan_2:
                item_2 = m
                break

    if item_2 in menu:
        total_order += price[item_2]
        print(f"{item_2} has been added in your order. Total so far: ${total_order}")
    else:
        print(f"Sorry, {pilihan_2} is not on the menu.")

print(f"\nThe total amount of your order is: ${total_order}")
print("Thank you for dining with us! Enjoy your meal!")

