import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ""

    while feedback != "c":
       
        if low > high:
            print("\n❌ Error: Your feedback has led to an impossible range.")
            print("Please make sure you're giving correct hints (H, L, C).")
            return

        guess = random.randint(low, high)
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)? ").lower()

        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
        elif feedback != "c":
            print("⚠️ Invalid input. Please type 'H', 'L', or 'C'.")

    print(f"\n✅ The computer guessed your number, {guess}, correctly!")


computer_guess(10)