salary=[]
top=[]
num=int(input("Enter how many employee salaries you wanted to enter in the list:"))
for i in range(0,num):
    a=float(input(f"Enter the number {i+1} employee salary in the floating points numbers :"))
    salary.append(a)
print(salary)

n=len(salary)

def selection():
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if salary[j]<salary[min_index]:
                min_index=j
        salary[min_index],salary[i]=salary[i],salary[min_index]
    return salary

def bubble():
    for i in range(n):
        for j in range(0,n-i-1):
            if salary[j]>salary[j+1]:
                salary[j],salary[j+1]=salary[j+1],salary[j]
    return salary 

def display():
    top_salary = sorted(salary, reverse=True)[:5]
    print("The top five salary are followed:")
    for s in top_salary:
        print(s)
        

#**********MAIN MENU********
while True:
    print("Enter you choice \n 1.Sort the salary using the selecting sort \n 2.Sort the salary using the bubble sort \n 3.Display the top five salary \n 4.Exit")
    choice=int(input())
    if choice==1:
        selection()
        print("The sorted salary by selection sort are:",salary)
    elif choice==2:
        bubble()
        print("The sorted salary using the bubble sort are:",salary)
    elif choice==3:
        display()
    elif choice==4:
        exit()
        break
    else:
        print("Invalid input")
    
            
            
    
        
