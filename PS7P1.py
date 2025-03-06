principal = float(input("Enter initial principal amount: "))
rate = float(input("Enter annual interest rate (as a decimal): "))

total_interest = 0

print(f"{'Year':<5}{'Beginning Balance':<20}{'Ending Balance':<20}")

for year in range(1, 6):
    beginning_balance = principal
    interest = beginning_balance * rate
    ending_balance = beginning_balance + interest
    
    total_interest += interest
    
    print(f"{year:<5}{beginning_balance:<20.2f}{ending_balance:<20.2f}")

    principal = ending_balance

print(f"\nTotal accumulated interest over 5 years: ${total_interest:.2f}")
