# Define Node class to store student data
class Node:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks
        self.next = None  # pointer to next node


# Define LinkedList class to manage all student records
class LinkedList:
    def __init__(self):
        self.head = None  # initially empty list

    def insert(self, name, roll, marks):
        """Insert a new student record at the end"""
        new_node = Node(name, roll, marks)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
        print("Data Inserted Successfully.")

    def delete(self, roll):
        """Delete student record by roll number"""
        temp = self.head
        prev = None
        while temp and temp.roll != roll:
            prev = temp
            temp = temp.next
        if temp is None:
            print("Record not found.")
            return
        if prev is None:
            self.head = temp.next
        else:
            prev.next = temp.next
        print("Record deleted successfully.")

    def update(self, roll):
        """Update student record by roll number"""
        temp = self.head
        while temp and temp.roll != roll:
            temp = temp.next
        if temp is None:
            print("Record not found.")
        else:
            temp.name = input("Enter Updated Name: ")
            temp.marks = input("Enter Updated Marks: ")
            print("Record updated successfully.")

    def search(self):
        """Search record by roll number, name, or marks"""
        print("Search by:\n1. Roll Number\n2. Name\n3. Marks")
        opt = input("Enter option (1-3): ")
        if opt == "1":
            roll = input("Enter Roll Number: ")
            temp = self.head
            while temp:
                if temp.roll == roll:
                    print(f"Record Found: Name: {temp.name}, Roll No: {temp.roll}, Marks: {temp.marks}")
                    return
                temp = temp.next
        elif opt == "2":
            name = input("Enter Name: ")
            temp = self.head
            while temp:
                if temp.name.lower() == name.lower():
                    print(f"Record Found: Name: {temp.name}, Roll No: {temp.roll}, Marks: {temp.marks}")
                    return
                temp = temp.next
        elif opt == "3":
            marks = input("Enter Marks: ")
            temp = self.head
            while temp:
                if temp.marks == marks:
                    print(f"Record Found: Name: {temp.name}, Roll No: {temp.roll}, Marks: {temp.marks}")
                    return
                temp = temp.next
        print("Record not found.")

    def display(self):
        """Display all student records"""
        if self.head is None:
            print("No records to display.")
            return
        temp = self.head
        print("Student Records:")
        while temp:
            print(f"Name: {temp.name}, Roll No: {temp.roll}, Marks: {temp.marks}", end=" -> ")
            temp = temp.next
        print("NULL")


# Main menu
def menu():
    ll = LinkedList()
    while True:
        print("\nChoose Operation to Perform:")
        print("1. Insert")
        print("2. Delete")
        print("3. Update")
        print("4. Search")
        print("5. Display")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            name = input("Enter Student Name: ")
            roll = input("Enter Roll Number: ")
            marks = input("Enter Marks: ")
            ll.insert(name, roll, marks)
        elif choice == "2":
            roll = input("Enter Roll Number of the student to delete: ")
            ll.delete(roll)
        elif choice == "3":
            roll = input("Enter Roll Number of the student to update: ")
            ll.update(roll)
        elif choice == "4":
            ll.search()
        elif choice == "5":
            ll.display()
        elif choice == "6":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter 1-6.")


# Run the program
menu()
