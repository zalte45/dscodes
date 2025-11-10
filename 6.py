# Initialize an empty list to act as a queue
queue = []

def add_call():
    """Add a new call to the queue"""
    customer_id = input("Enter customer ID: ")
    call_time = input("Enter call time (in minutes): ")
    queue.append((customer_id, call_time))  # store both ID and time as a tuple
    print(f"Call from customer {customer_id} added.")

def answer_call():
    """Answer the first call in the queue (FIFO order)"""
    if queue:
        customer_id, call_time = queue.pop(0)
        print(f"Answered call from customer {customer_id} with call time {call_time} minutes.")
    else:
        print("No calls to answer.")

def view_queue():
    """View all pending calls"""
    if queue:
        print("Pending calls in the queue:")
        for i, (customer_id, call_time) in enumerate(queue, start=1):
            print(f"{i}. Customer ID: {customer_id}, Call Time: {call_time} minutes")
    else:
        print("The call queue is empty.")

def check_empty():
    """Check if the queue is empty"""
    if not queue:
        print("The queue is empty.")
    else:
        print("There are calls waiting in the queue.")

def menu():
    """Main menu loop"""
    while True:
        print("\nChoose an operation:")
        print("1. Add a call")
        print("2. Answer a call")
        print("3. View queue")
        print("4. Check if queue is empty")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_call()
        elif choice == "2":
            answer_call()
        elif choice == "3":
            view_queue()
        elif choice == "4":
            check_empty()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid input! Please enter a number between 1 and 5.")

# Run the program
menu()
