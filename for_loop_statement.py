for letters in "ROCKline SHIVA":
    print(letters)

Numbers = (1,22,333,4444)
for numbers in Numbers:
    print(numbers)

for I in range(5):
    print("Q")

students = ["ram","sai","charan"]
for names in range(len(students)):
    print(students[names])

for numbers in range(1,11):
    print(numbers)

for no in range(2):
    if no ==0:
        print("first number")
    if no==1:
        print("second number")
    else:
        print("third number")

no1 = [1,2,3,4,5]
no2 = [11,22,33,44,55]
for x in no1:
    for y in no2:
        print(x,y)

no = [1,2,3,4,5]
even=[]
odd=[]
for x in no:
    if x % 2 == 0:
        even.append(x)
        print(even)
    else:
        odd.append(x)
        print(odd)