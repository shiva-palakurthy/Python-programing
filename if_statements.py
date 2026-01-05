#if-else statements
is_boy = False
if is_boy:
    print("You are a boy.")
else:
    print("You are a girl")

password = "Mr.rockline"
enter_password = input("enter the password")
if password == enter_password:
    print("welcome ")
else:
    print("incorrect password")
print(enter_password)


Name = "shiva"
user_name = input("What is your name? ")
if user_name == Name:
    print("Welcome, " + user_name)
else:
    print("incorrect user")


Number = float(input("Enter a number:"))
if Number/2*Number==Number:
    print("The number is even")
else:
    print("The number is odd")

m=int(input("Enter a number:"))
if m>10:
    print("m ia greater than 10")
else:
    print("m ia less than 10")

#Elif statements
number = int(input("Enter a number:"))
if number > 0 :
    print("it is positive number")
elif number < 0 :
    print("it is negative number")
else:
    print("it is zero")

a = 10
b = 10

if a>b :
    print("hello")
elif a<b:
    print("bye")
else:
    print("goodbye")

def max_number(n1,n2,n3):
    if n1>=n2 and n1>=n3:
        return n1
    elif n2>=n1 and n2>=n3:
        return n2
    else:
        return n3

print(max_number(1,2,3))
print(max_number(12,22,33))
print(max_number(111111,21111,311))

#building a better calculator
number_1 = float(input("Enter the first number:"))
operator = input("Enter operator:")
number_2 = float(input("Enter the second number:"))

if operator == "+":
    print(number_1 + number_2)
elif operator == "-":
    print(number_1 - number_2)
elif operator == "*":
    print(number_1 * number_2)
elif operator == "/":
    print(number_1 / number_2)
elif operator == "%":
    print(number_1 % number_2)
else:
    print("enter the correct operator")

