with open("orders.txt", "w") as file:
    file.write("""Widget
10
50
Hammer
2
10
Saw
4
8
Drill
1
100
Nails
50
0.5
""")
  
with open("orders.txt", "r") as file:
    lines = file.readlines()

total_extended_price = 0
order_count = 0

print("\nOrder Details:")
print(f"{'Item':<10}{'Quantity':<10}{'Price':<10}{'Extended Price':<15}")

for i in range(0, len(lines), 3):
    item = lines[i].strip()
    quantity = int(lines[i + 1].strip())
    price = float(lines[i + 2].strip())

    extended_price = quantity * price
    total_extended_price += extended_price
    order_count += 1

    print(f"{item:<10}{quantity:<10}{price:<10.2f}{extended_price:<15.2f}")

average_order = total_extended_price / order_count if order_count > 0 else 0

print(f"\nTotal Extended Price: ${total_extended_price:.2f}")
print(f"Number of Orders: {order_count}")
print(f"Average Order Price: ${average_order:.2f}")

