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
    print(f"{i}. {item} - Rp{price[item]}")

total_order = 0

while True:
    pilihan = input("Enter item (Number/Name), or 'done' to finish ordering: ").lower().strip()

    if pilihan == 'done':
        break

item = cari_item(pilihan)
if item:
    total_order += price[item]
    print(f"{item} has been added to your order. Total so far:" Rp{total_order}")
else:
    print(f"Sorry, {pilihan} is not on the menu.")

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


print(f"\nThe total amount of your order is: ${total_order}")
print("Thank you for dining with us! Enjoy your meal!")

