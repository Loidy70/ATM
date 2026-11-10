from decimal import Decimal, InvalidOperation


PIN = "1234"
STARTING_BALANCE = Decimal("1000.00")


def read_amount(prompt):
	try:
		amount = Decimal(input(prompt)).quantize(Decimal("0.01"))
	except (InvalidOperation, ValueError):
		print("Please enter a valid amount.")
		return None

	if amount <= 0:
		print("Amount must be greater than zero.")
		return None
	return amount


def main():
	balance = STARTING_BALANCE
	print("Welcome to the ATM")

	for attempt in range(3):
		entered_pin = input("Enter your PIN: ")
		if entered_pin == PIN:
			break
		remaining = 2 - attempt
		if remaining:
			print(f"Incorrect PIN. {remaining} attempt(s) remaining.")
	else:
		print("Too many incorrect attempts. Goodbye.")
		return

	while True:
		print("\nATM Menu")
		print("1. Check balance")
		print("2. Deposit cash")
		print("3. Withdraw cash")
		print("4. Exit")
		choice = input("Choose an option (1-4): ").strip()

		if choice == "1":
			print(f"Your balance is ${balance:.2f}")
		elif choice == "2":
			amount = read_amount("Deposit amount: $")
			if amount is not None:
				balance += amount
				print(f"Deposit successful. New balance: ${balance:.2f}")
		elif choice == "3":
			amount = read_amount("Withdrawal amount: $")
			if amount is not None:
				if amount > balance:
					print("Insufficient funds.")
				else:
					balance -= amount
					print(f"Withdrawal successful. New balance: ${balance:.2f}")
		elif choice == "4":
			print("Thank you for using the ATM. Goodbye!")
			break
		else:
			print("Please choose a valid option (1-4).")


if __name__ == "__main__":
	main()
