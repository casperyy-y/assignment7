with open("students.txt", "w") as file:
    file.write("""Jones
I
12
Adams
I
10
Baker
O
12
Smith
O
16
Taylor
I
15
""")

with open("students.txt", "r") as file:
    lines = file.readlines()

total_tuition = 0
student_count = 0

print("\nStudent Tuition Details:")
print(f"{'Student':<10}{'Credits':<10}{'Tuition':<10}")

for i in range(0, len(lines), 3):
    last_name = lines[i].strip()
    district_code = lines[i + 1].strip().upper()
    credits = int(lines[i + 2].strip())

    tuition_rate = 250.00 if district_code == "I" else 500.00
    tuition = credits * tuition_rate
    total_tuition += tuition
    student_count += 1

    print(f"{last_name:<10}{credits:<10}{tuition:<10.2f}")

print(f"\nTotal Tuition: ${total_tuition:.2f}")
print(f"Number of Students: {student_count}")
