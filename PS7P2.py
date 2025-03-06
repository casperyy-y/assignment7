a, b = 1, 1

print("First 20 Fibonacci numbers:")
for _ in range(20):
    print(a, end=" ")
    a, b = b, a + b  # Update Fibonacci sequence
