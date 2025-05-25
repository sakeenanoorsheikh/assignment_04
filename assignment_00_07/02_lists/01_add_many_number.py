def sum_of_numbers(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

def main():
    number_list = [10, 20, 30, 40, 50]
    result = sum_of_numbers(number_list)
    print("list:", number_list)
    print("sum of numbers:", result)

if __name__ == "__main__":
    main()


