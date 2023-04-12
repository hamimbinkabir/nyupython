DOLLARS_TO_CENTS = 100
QUARTERS_TO_CENTS = 25
DIMES_TO_CENTS = 10
NICKELS_TO_CENTS = 5
PENNIES_TO_CENTS = 1

def get_int_input(prompt: str) -> int:
    num = -1
    while True:
        try:
            num = int(input(prompt))
            break
        except ValueError:
            print("Error: Enter an integer, try again...")
    return num

def main():
    print("Please enter the number of coins:")
    num_quarters = get_int_input("# of quarters: ")
    num_dimes = get_int_input("# of dimes: ")
    num_nickels = get_int_input("# of nickels: ")
    num_pennies = get_int_input("# of pennies: ")
    total_in_cents = num_quarters * QUARTERS_TO_CENTS + \
                     num_dimes * DIMES_TO_CENTS + \
                     num_nickels * NICKELS_TO_CENTS + \
                     num_pennies * PENNIES_TO_CENTS
    num_dollars = total_in_cents // DOLLARS_TO_CENTS
    num_cents = total_in_cents % DOLLARS_TO_CENTS
    print(f"The total is {num_dollars} dollars and {num_cents} cents")

if __name__ == "__main__":
    main()