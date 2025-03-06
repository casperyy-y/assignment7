with open("employee_data.txt", "w") as file:
    file.write("""Adams
50000.00
Baker
75000.00
Smith
45000.00
Johnson
120000.00
Taylor
60000.00
""")

with open("employee_data.txt", "r") as file:
    lines = file.readlines()

total_bonus = 0

print("\nEmployee Bonuses:")
for i in range(0, len(lines), 2):
    last_name = lines[i].strip()
    salary = float(lines[i + 1].strip())

    if salary >= 100000:
        bonus_rate = 0.20
    elif salary >= 50000:
        bonus_rate = 0.15
    else:
        bonus_rate = 0.10

    bonus = salary * bonus_rate
    total_bonus += bonus

    print(f"Employee: {last_name}, Salary: ${salary:.2f}, Bonus: ${bonus:.2f}")

print(f"\nTotal bonuses paid: ${total_bonus:.2f}")
