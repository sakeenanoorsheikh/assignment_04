DAYS_PER_YEAR = 365
HOURS_PER_DAY = 24
MINT_PER_HOUR = 60
SEC_PER_MINT = 60

def main():

    total_second = DAYS_PER_YEAR * HOURS_PER_DAY * MINT_PER_HOUR * SEC_PER_MINT


    print(f"There are {total_second} seconds in the year!")

if __name__ == "__main__":
    main()
