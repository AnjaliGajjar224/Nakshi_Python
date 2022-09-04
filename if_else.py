"""
1. if
2. if..else
3. if...elif...else

Syntax:
-------------
if condition:
    statements
else:
    statements

--> Indentation
"""

# a = int(input("Enter a number: "))

# if a >= 0:
#     print(a, "is Positive")
# else:
#     print(a,"is Negative")

"""
Take a number from the user and check whether the number is even or odd.
"""
n = int(input("Enter a number: "))

if n % 2 == 0:
    print(n,"is Even Number")
else:
    print(n,"is Odd Number")