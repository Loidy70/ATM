# ATM

A simple command-line ATM simulation written in Python.

## Run

```powershell
python atm.py
```

The demo PIN is `1234`.

## Features

- Check the current balance.
- Deposit and withdraw cash with positive-amount validation and insufficient-funds checks.
- View a history of successful deposits and withdrawals during the current run.
- Display colored prompts and messages in terminals that support ANSI colors.
- Allow up to three PIN attempts per run.

The balance and transaction history are kept in memory and reset when the program exits. The PIN is hard-coded for demonstration purposes; this program is not suitable for real accounts or financial transactions.
