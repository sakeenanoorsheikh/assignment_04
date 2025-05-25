def find_average(num1, num2):

    return (num1 + num2) / 2

def main():

    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    average = find_average(num1, num2)
    print(f"The average of {num1} and {num2} is: {average}")

if __name__ == "__main__":
    main()