cid=[]
def create():
    global n
    n=int(input("How many id's you wanted to store in the list :"))
    for i in range(0,n):
        a=int(input("Enter the customers id's you wanted to enter :"))
        cid.append(a)
    print("The create customer id's are as follows:",cid)


def linear():
    target=int(input("Enter the id's wanted to find in the list:"))
    if len(cid)==0:
        print("First Create the data base then re-try")
        return
    else:
        for i in range(0,n):
            if cid[i]==target:
                print(f"The element is found at the index:{i+1}")
                break
            else:
                print("Still finding the element")
    return 1

def binary():
    found=False
    cid.sort()
    target=int(input("Enter the id's wanted to find in the list:"))
    if len(cid)==0:
        print("First Create the data base then re-try")
        return
    else:
        low=0
        high=len(cid)-1
        while low<=high:
            mid=(low+high)//2
            if cid[mid]==target:
                print(f"The item Found at index{mid}")
                found=True
                break
            elif cid[mid]<target:
                low=mid+1
            else:
                high=mid-1
    if not found:
        print("The item is not present")

def menu():
    while True:
        print("\n********MENU***********")
        print("Select what you wanted to do\n 1.Create the data base\n 2.search the element using linar search\n 3.search the element using the binary search\n 4.Exit the program")
        choice=int(input())
        if choice==1:
            create()
        elif choice==2:
            linear()
        elif choice==3:
            binary()
        elif choice==4:
            exit()  
menu()