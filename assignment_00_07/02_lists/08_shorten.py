MAX_LENGTH = 3

def shorten(lst):

    while len(lst) > MAX_LENGTH:
        remove_item = lst.pop()
        print("Removed ", remove_item)


def main():
    lst = []


    n = int(input("Enter number of elements in the list: "))
    for _ in range(n):
        value = input("Enter a value: ")
        lst.append(value)  

    print("original list: ", lst)
    shorten(lst)
    print("shortened list: ", lst)

    
if __name__ == "__main__":
    main()        
