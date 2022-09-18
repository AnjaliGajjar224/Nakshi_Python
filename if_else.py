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
# n = int(input("Enter a number: "))

# if n % 2 == 0:
#     print(n,"is Even Number")
# else:
#     print(n,"is Odd Number")

"""
if...elif...else
"""

"""
 A school has following rules for grading system:
    # a. Below 25 - F
    # b. 25 to 45 - E
    # c. 45 to 50 - D
    # d. 50 to 60 - C
    # e. 60 to 80 - B
    # f. Above 80 - A
    # Ask user to enter marks and print the corresponding grade.
"""

marks = int(input("Enter Your Marks: "))

if marks < 25:
    print("Grade F")
elif marks < 45:
    print("Grade E")
elif marks < 50:
    print("Grade D")
elif marks < 60:
    print("Grade C")
elif marks < 80:
    print("Grade B")
else:
    print("GRADE A")