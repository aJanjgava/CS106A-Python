def main():
    while True:
        balance = float(input("Initial balance: "))
        start_year = int(input("Start year: "))
        start_month = int(input("Start month: "))
        end_year = int(input("End year: "))
        end_month = int(input("End month: "))

        if start_year > end_year or (start_year == end_year and start_month > end_month):
            print("Starting date needs to be before the ending date.")

        else:
            interest_rate = float(input("Interest rate ( 0 to quite ): "))

            if interest_rate == 0:
                break

            while start_year != end_year or start_month != end_month:
                print(f"Year {start_year}, month {start_month} balance: {balance} ")
                balance = balance + balance * interest_rate
                start_month += 1
                if start_month > 12:
                    start_month = 1
                    start_year += 1
            print(f"Year {start_year}, month {start_month} balance: {balance}")


if __name__ == '__main__':
    main()
