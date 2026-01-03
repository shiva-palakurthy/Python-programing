def say_hello():
    print("Hello World")
print("welcome")
say_hello()
print("bye")

def say_hi(name):
            print("Hello, " + name)
(say_hi("shiva"))
(say_hi("sai"))
(say_hi("ram"))

def say(name,age):
    print("hello " + name + "are you " +age)
(say("shiva","24"))
(say("ram","26"))

# Return Statement
def square(A):    #function called step 2
        return A*A # function return final step

print(square(11)) #function  step1

def cube(num):
       return num*num*num
result = cube(2)
print(result)