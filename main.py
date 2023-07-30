import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    
    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        
        columns.append(column)
    
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()


def deposit():
    while True:
        jlh_deposit = input ("Berapa deposit yang ingin anda masukkan? Rp.")
        if jlh_deposit.isdigit():
            jlh_deposit = int(jlh_deposit)
            if jlh_deposit > 0:
                break
            else:
                print ("Deposit tidak boleh 0 atau kosong.")
        else:
            print ("Deposit harus berupa angka.")
    
    return jlh_deposit

def get_number_of_lines():
    while True:
        lines = input ("Berapa kali anda ingin mencoba (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <=MAX_LINES:
                break
            else:
                print("Berapa kali anda ingin mencoba?")
        else:
            print("Harus berupa angka.")
    
    return lines

def get_bet():
    while True:
        amount = input ("Berapa bet anda? Rp.")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print (f"bet berkisar dari ${MIN_BET} - ${MAX_BET}.")
        else:
            print ("bet harus berupa angka.")
    
    return amount

def spin(balance):
    lines = get_number_of_lines()

    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(
                f"Saldo anda tidak cukup. Saat ini saldo anda adalah Rp. {balance}"
            )
        else:
            break

    print (f"Anda bertaruh Rp.{bet} sebanyak {lines} kali. Total bet: {total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)

    print(f"Anda memenangkan Rp.{winnings}")
    print(f"Anda menang pada baris:", *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Saldo saat ini adalah Rp.{balance}")
        answer = input("Tekan Enter untuk bermain (q untuk keluar dari program).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"Saldo anda sekarang Rp.{balance}")

main()