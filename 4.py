text=""
undo_stack=[]
redo_stack=[]

def type_text(new_text):
    global text
    undo_stack.append(text)
    text+=new_text
    redo_stack.clear()
    print("The text now:",text)
    
def undo():
    global text
    if undo_stack:
        redo_stack.append(text)
        text=undo_stack.pop()
        print("The text is undo:",text)
    else:
        print("The stack is empty")
        
        
def redo():
    global text
    if redo_stack:
        undo_stack.append(text)
        text=redo_stack.pop()
        print("Redo text:",text)
    else:
        print("The stack is empty")
        
def menu():
    while True:
        print("Enter you choice:\n1.Add text\n2.redo the text \n3.Undo the text \n4.Exit")
        choice=int(input())
        if choice==1:
            a=input("Enter the text to add:")
            type_text(a)
        elif choice==2:
            redo()
        elif choice==3:
            undo()
        elif choice==4:
            exit()
            break
        else:
            print("Invalid input")
menu()
        
        
