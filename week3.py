
'''
#Recursive function to count up from a negative number to zero
def count_up(number):
    if number >=0:
        print("Blastoff!")
    else:
        print(number)
        count_up(number + 1)

#Recursive function to count down from a positive number to zero
def count_down(number):
    if number <= 0:
        print("Blastoff!")
    else:
        print(number)
        count_down(number - 1)

#Get input from the user
number = int(input("Input a number: "))

#Decide which function to call based on the input
if number > 0:
   count_down(number)
elif number < 0:
    count_up(number)
else:
    count_down(number) #Zero: Call count down

'''


# Program without error handling (deliberate mistake for demonstration)
numerator = int(input("Input a numerator: "))
denominator = int(input("Input a denominator: "))

def division(numerator, denominator):
    result = numerator / denominator  # This will cause a ZeroDivisionError if denominator is 0
    print("Result:", result)

division(numerator, denominator)



# Program with error handling
numerator = int(input("Input a numerator: "))
denominator = int(input("Input a denominator: "))

def division(numerator, denominator):
    try:
        result = numerator / denominator
        print("Result:", result)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero. Please enter a non-zero denominator.")

division(numerator, denominator)


'''
First error:
Input a numerator: 4
Input a denominator: 2
Traceback (most recent call last):
  File "C:\Users\hp\Desktop\practice\week3.py", line 42, in <module>
    division(numerator, denominator)
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: division() takes 0 positional arguments but 2 were given


Likely Cause:
I wrote the function without parameter which makes it to accept only one parameter:

def division():   # ← No parameters here!
    ...
But then I called it like this:

division(numerator, denominator)
That causes Python to say: "Hey! I wasn't expecting any arguments!"

✅ How to Fix It:
Make sure your function is defined with parameters, like this:


def division(numerator, denominator):
    if denominator == 0:
        print("Please enter a number different from 0!")
    else:
        x = numerator / denominator
        print(x)
Then the call below will work correctly:

division(numerator, denominator)

Second error:
 File "C:\Users\hp\Desktop\practice\week3.py", line 45

    ^^^
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 104-105: truncated \UXXXXXXXX escape

This is a common Windows path error caused by how python interprets backslashes(\) in strings as escape sequences like (\n, \t, or \uxxxx..... for unicode)
The error means that somewhere in your code or in a file path Python is trying to inpterpret something like:
        C:\Users\hp\Desktop\practice\week3.py
as if \U is the start of a Unicode escape which is invalid because it's not followed by enough digits.

How to fix it:
1. use raw strings by adding r in front:
    path = r"C:\Users\hp\Desktop\practice\week3.py"

2. use double backslashes:
    path = "C:\\Users\\hp\\Desktop\\practice\\week3.py"

3. use forward slashes
    path = "C:/Users/hp/Desktop/practice/week3.py"



'''















