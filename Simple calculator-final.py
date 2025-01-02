# hello this is my code, it is a simple robot, that should be able to do many things
# hours i've spent on this code :12
# maybe only god knows, how it works

word = ""
while len(word) == 0:
    word = input("Type any character to begin: ")
print("Hello, this is an artificial intelligence machine, please input text from the following menu")
print("OPTIONS: user/calculator")

def user1():
    f_name = input("What is your first name: ")
    l_name = input("What is your last name: ")
    age = int(input("How old are you: "))
    if age >= 18:
        print("You are an adult")
    elif age > 0 and age < 18:
        print("You are a kid")
    else:
        print("You have an invalid age")

def calculator():
    print("This is a calculator")
    print("Options: add, subtract, multiply, divide")
    operator = input("Choose an operation: ")
    num1 = float(input("Add first number: "))
    num2 = float(input("Add second number: "))
    if operator == "add":
        result = num1 + num2
        print(result)
    elif operator == "subtract":
        result = num1 - num2
        print(result)
    elif operator == "multiply":
        result = num1 * num2
        print(result)
    elif operator == "divide":
        result = num1 / num2
        print(result)
    else:
        print("Operator is invalid!")





func1 = input("Input text: ")
if func1 == "user":
    user1()
elif func1 == "calculator":
    calculator()
else:
    print("Please input valid text or rerun program")