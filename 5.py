# Initialize an empty list to work as a Queue
queue = []

def add_event():
    """Add a new event to the queue"""
    event = input("Enter the event name: ")
    queue.append(event)
    print(f"Event '{event}' added successfully!")

def process_event():
    """Process the first event in the queue (FIFO order)"""
    if queue:
        event = queue.pop(0)
        print(f"Processing event: {event}")
    else:
        print("No events to process.")

def display_events():
    """Display all pending events"""
    if queue:
        print("Pending Events:")
        for i, event in enumerate(queue, start=1):
            print(f"{i}. {event}")
    else:
        print("No pending events!")

def cancel_event():
    """Cancel a specific event by name"""
    if queue:
        event = input("Enter the event name to cancel: ")
        if event in queue:
            queue.remove(event)
            print(f"Event '{event}' has been canceled.")
        else:
            print(f"Event '{event}' not found in the queue.")
    else:
        print("No events to cancel.")

def menu():
    """Main menu loop"""
    while True:
        print("\n--- Event Processing System ---")
        print("1. Add event")
        print("2. Process Next Event")
        print("3. Display Pending Events")
        print("4. Cancel Event")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_event()
        elif choice == "2":
            process_event()
        elif choice == "3":
            display_events()
        elif choice == "4":
            cancel_event()
        elif choice == "5":
            print("Exiting Event Processing System. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1-5.")

# Start the program
menu()
