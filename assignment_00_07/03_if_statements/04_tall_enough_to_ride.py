def main():
    
    while True:
        user_input = input("How tall are you? ")

        if user_input == "":
            print("Exiting the program!")
            break

        try:
            height = float(user_input)
        except ValueError:
            print("Please enter a valid number!\n")
            continue

        height = int(height)

        if height >= 50:
            print("You are tall enough to ride!\n")
        else:
            print("You are not tall enough to ride, but maybe next year!\n")

if __name__ == "__main__":
    main()
