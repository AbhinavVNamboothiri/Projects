# Python Slot Machine

import random
import math

def spin_row():
    symbols = ["🍉", "🍋", "⭐", "🔔", "🍒"]
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("**************")
    print(" | ".join(row))    
    print("**************")

def ger_payouts(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "⭐":
            return bet * 10
        elif row[0] == "🔔":
            return bet * 5
        elif row[0] == "🍒":
            return bet * 2
        elif row[0] == "🍉":
            return bet * 1
        elif row[0] == "🍋":
            return bet * 1
    else:
        return 0    

def main():
    balance = 100
    
    print("***********************************")
    print("        Welcome to Slot Machine")
    print("Symbols: 🍉 🍋 ⭐ 🔔 🍒 ")
    print("***********************************")

    while balance > 0:
        print(f"Current balance: ${balance}")
        
        bet = input("Enter your bet amount: ")

        if not bet.isdigit():
            print("Please enter a valid bet amount.")
            continue

        bet = int(bet)

        if bet > balance:
            print("You don't have enough balance.")
            continue

        if bet <= 0:
            print("Bet amount must be greater than 0.")
            continue

        balance -= bet 

        row = spin_row()
        print("Spinning...\n")
        print_row(row)

        payout = ger_payouts(row, bet)

        if payout > 0:
            print(f"You won ${payout}")
        else:
            print("You lost.")

        balance += payout

        play_again = input("Do you want to play again? (yes/no): ")

        if play_again.lower() != "yes":
            break
        
    print("******************************************** ")
    print(f"Game Over! Your final balance is ${balance}")
    print("********************************************")


if __name__ == "__main__":
    main()