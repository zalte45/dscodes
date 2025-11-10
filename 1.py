members=[]
m=int(input("\nEnter the Number of member you wanted to enter:"))
for i in range(0,m):
    m_no=int(input(f"\nEnter the no of books borrowed by {i+1}th member:"))
    members.append(m_no)
print(f"\nThe books borrowed by members are :",members)

books=[]
b=int(input("\nEnter the number of books wanted to register:"))
for i in range(0,b):
    b_no=int(input(f"\nEnter the number of time {i+1} book borrwed:"))
    books.append(b_no)
    
print("\nThe Record of books are:",books)


count=0
sum=0

for i in range(0,m):
    if members[i]==0:
        count=count+1
    else:
        sum=sum+members[i]
        
print("\nThe sum of books borrowed by all library members",sum)
print("\nThe number of members who have not borrowed any book are:",count)


if m > 0:
    avg = round(sum/ m)
    print("\nThe avg number of books borrowed by all members are :",avg)
else:
    avg = 0



high=0
high_book_id=0
for i in range(0,b):
    if books[i]>=high:
        high=books[i]
        high_book_id=i+1
          
print(f"\nThe book which borrowed most is , book number: {high_book_id} and the number of time it borrowed is {high}")

low_book_id=0         
low=books[0]
for i in range(0,b):
    if books[i]<low:
        low=books[i]
        low_book_id=i+1
        
print(f"\nThe book which borrwed lowest is :{low_book_id} and the number of time it borrowed is:{low}")

max_frequency = 0
most_frequent_count = 0

for borrow_count in books:
    freq = books.count(borrow_count)
    if freq > max_frequency:
        max_frequency = freq
        most_frequent_count = borrow_count
        
        
print(f"\nThe most frequent borrow count is: {most_frequent_count}")

print("\n--- Library Record Process Completed Successfully ---")

