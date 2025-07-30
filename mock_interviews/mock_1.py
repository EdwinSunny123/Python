# Single Line Comment

"""
This
is a
multi-line
comment
"""

#------------------------------------------ Task 1: Calculator Program ----------------------------------------------


num1 = int(input('Enter your number: '))
num2 = int(input('Enter your number: '))
print('sum:', num1 + num2)
print('substract:' , num1 - num2)
print('multiply:', num1 * num2)
print('divide:', num1 / num2)

#------------------------------------------ Task 2: Even/Odd and Prime Check ----------------------------------------------

num3 = int(input("Enter your number :"))
if num3 % 2 == 0:
    print('even number')

else:
    print('odd number')

num4 = int(input('Enter your number:'))  
if num4 > 1:
    print('prime number')
    
else:
    print('not prime number')


#------------------------------------------ Task 3: Multiplication Table Generator ----------------------------------------------

a = int(input("Enter your number :"))
print("Multiplication table of :", a)
print(a, "* 1 =", a*1)
print(a, "* 2 =", a*2)
print(a, "* 3 =", a*3)
print(a, "* 4 =", a*4)
print(a, "* 5 =", a*5)
print(a, "* 6 =", a*6)
print(a, "* 7 =", a*7)
print(a, "* 8 =", a*8)
print(a, "* 9 =", a*9)
print(a, "* 10 =", a*10)

#------------------------------------------ Task 4: Find Maximum of 3 Numbers----------------------------------------------

num5 = int(input('Enter your number:'))
num6 = int(input('Enter your number:'))
num7 = int(input('Enter your number:'))

#using if--else statement
if num5 >= num6 and num5 >= num7:
    print(num5)
elif num6 >= num5 and num6 >= num7:
    print(num6)
else:
    print(num7)

#-------------------------------------------Task 5: Simple Total Marks Calculator of Students------------------------------------------

# Calculating total marks of a student in a subject
marks_history = float(input("Enter marks in history:"))
marks_science = float(input("Enter marks in science:"))
marks_maths = float(input("Enter marks in maths:"))
marks_english = float(input("Enter marks in english:"))
marks_geography = float(input("Enter marks in geography:"))
marks_marathi = float(input("Enter marks in marathi:"))
marks_hindi = float(input("Enter marks in hindi:"))
marks_sanskrit = float(input("Enter marks in sanskrit:"))
total_marks = marks_history + marks_science + marks_maths + marks_english + marks_geography + marks_marathi + marks_hindi + marks_sanskrit
print("Total Marks :", total_marks)



