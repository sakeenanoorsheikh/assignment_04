def add_three_copies(mylist, data):
    """Add three copies of data to the given list(mutable behavior)."""
    mylist.append(data)
    mylist.append(data)
    mylist.append(data)

def main():
    message = input("Enter a message to copy: ") 
    mylist = []  
    print("List before:", mylist)
    add_three_copies(mylist, message)
    print("List after:", mylist)

if __name__ == "__main__":
    main()    


  