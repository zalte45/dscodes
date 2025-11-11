array=[]

def create():
    global array
    array=[]
    n= int(input("Enter how many customer account IDs you want store:"))
    for i in range(n):
        id =int(input("Enter Customer account ID:"))
        array.append(id)
    print("Customer Account IDs:", array)

def linear():
    global array
    key = int(input("Enter the Customer Account ID to search: "))
    found = False
    for i in range(len(array)):
        if array[i] == key:
            print("Customer Account ID", key, "found at position", i)
            found = True
            break

    if not found:
        print("Customer Account ID", key, "not found")

def binary():
    global array
    key = int(input("Enter the Customer Account ID to search: "))

    print("Customer Account IDs before sorting:", array)
    array.sort()
    print("Customer Account IDs after sorting:", array)

    low = 0
    high = len(array) - 1 
    # high = n-1 

    while low <= high:
        mid = (low + high) // 2

        if array[mid] == key:
            print("Customer Account ID", key, "found at position", mid)
            return mid
        elif array[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def mainmenu():
    print("*************** MENU ***************")
    print("1. Create database")
    print("2. Search Customer Account ID using Linear Search")
    print("3. Search Customer Account ID using Binary Search")
    print("4. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        create()
        mainmenu()

    elif ch == 2:
        linear()
        mainmenu()

    elif ch == 3:
        binary()
        mainmenu()

    elif ch == 4:
        print("Exiting the program...")

    else:
        print("Invalid input! Please enter a choice between 1 and 4.")
        mainmenu()

# Start the program
mainmenu()

