from decimal import Decimal, InvalidOperation
import sys


PIN = "1234"
STARTING_BALANCE = Decimal("1000.00")
COLORS = {
	"blue": "\033[94m",
	"cyan": "\033[96m",
	"green": "\033[92m",
	"red": "\033[91m",
}
RESET_COLOR = "\033[0m"


def colorize(message, color):
	if not sys.stdout.isatty():
		return message
	return f"{COLORS[color]}{message}{RESET_COLOR}"


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
	transactions = []
	print(colorize("Welcome to the ATM", "cyan"))

	for attempt in range(3):
		entered_pin = input("Enter your PIN: ")
		if entered_pin == PIN:
			break
		remaining = 2 - attempt
		if remaining:
			print(colorize(
				f"Incorrect PIN. {remaining} attempt(s) remaining.", "red"
			))
	else:
		print(colorize("Too many incorrect attempts. Goodbye.", "red"))
		return

	while True:
		print(colorize("\nATM Menu", "blue"))
		print("1. Check balance")
		print("2. Deposit cash")
		print("3. Withdraw cash")
		print("4. Transaction history")
		print("5. Exit")
		choice = input("Choose an option (1-5): ").strip()

		if choice == "1":
			print(colorize(f"Your balance is ${balance:.2f}", "cyan"))
		elif choice == "2":
			amount = read_amount("Deposit amount: $")
			if amount is not None:
				balance += amount
				transactions.append(
					f"Deposit: +${amount:.2f} | Balance: ${balance:.2f}"
				)
				print(colorize(
					f"Deposit successful. New balance: ${balance:.2f}", "green"
				))
		elif choice == "3":
			amount = read_amount("Withdrawal amount: $")
			if amount is not None:
				if amount > balance:
					print(colorize("Insufficient funds.", "red"))
				else:
					balance -= amount
					transactions.append(
						f"Withdrawal: -${amount:.2f} | Balance: ${balance:.2f}"
					)
					print(colorize(
						f"Withdrawal successful. New balance: ${balance:.2f}",
						"green",
					))
		elif choice == "4":
			if transactions:
				print(colorize("Transaction history:", "cyan"))
				for transaction in transactions:
					print(transaction)
			else:
				print("No transactions have been made this session.")
		elif choice == "5":
			print("Thank you for using the ATM. Goodbye!")
			break
		else:
			print(colorize("Please choose a valid option (1-5).", "red"))


if __name__ == "__main__":
	main()
