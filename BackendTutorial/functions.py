def my_function():
    print("Hello,How are you doing")


my_function()


def my_function2():
    print("Hello, I am doing good.")
    print("What about you ?")


my_function2()


def my_name(name):
    print("Hello," + name)


my_name("John")


#create a function that takes two numbers and performs summation and displays the sum
def sum2numbers(num1, num2):
    num3 = num1 + num2
    print(num3)

sum2numbers(1, 2)

def multiply(x,y):
    z = x * y
    return z

print(multiply(2,3))

#Question 1
#Create a function where if name is Alice or Bob, use a personalized greeting else use a general greeting
def greet(name):
    if name == "Alice" or name == "Bob":
        return f"Hello, {name}. Nice to meet you!"
    else:
        return f"Hello"

print(greet("Alice"))
print(greet("Bob"))
print(greet("Helena"))

#Question 2
#Find the maximum of 3 numbers
def max3number(a,b,c):
    if a > b and a > c:
        return f"Maximum number is {a}"
    elif b > a and b > c:
        return f"Maximum number is {b}"
    else:
        return f"Maximum number is {c}"

print(max3number(1,3,2))

#Question 3
#Sum of a list of numbers
def addition(numbers):
    total= sum(numbers)
    return total

nums=[1,3,4,6]
print("Sum of list:",sum(nums))



