# TASK 1

# Name: Aditya
# Roll no: 2501060126
# Course: BCA(AI & DS)
# Semeter: 1st
# Subjet: Problem Solving with Python
# Assignment: Unit 1- Mini project
# Title: Student Profile COnsole App
# Date: 13-11-2025

print('''---------------------------------------------------------
        |WELCOME TO STUDENT PROFILE CONSOLE APP|
  |THIS ALLOWS YOU TO CREATE AND VIEW STUDENT PROFILES|
---------------------------------------------------------''')


# # TASK 2


stud_name= str(input("Student's Name: "))
roll_no= int(input("Roll Number: "))
program= str(input("Program: "))
uni_name= str(input("University Name: "))
city= str(input("City: "))
age= int(input("Age: "))
hobby= str(input("Hobby: "))


# TASK 3

num_1= int(input("Enter Number 1: "))
num_2= int(input("Enter Number 2: "))

# Arithmetic Operators
print("Addition: ", num_1 + num_2)
print("Subtraction: ", num_1 - num_2)
print("Multiplication: ", num_1 * num_2)
print("Division: ", num_1 / num_2)
print("Modulus: ", num_1 % num_2)
print("square of Number 1: ", num_1 ** 2)
print("square of Number 2: ", num_2 ** 2)
print("Integer Division: ", num_1 // num_2)
print("--------------------------------")

# Assignment Operators
a = num_1
a += num_2
print("Assignment Addition: ", a)
a -= num_2
print("Assignment Subtraction: ", a)
a *= num_2
print("Assignment Multiplication: ", a)
a /= num_2
print("Assignment Division: ", a)
a %= num_2
print("Assignment Modulus: ", a)
a **= 2
print("Assignment Square: ", a)
a //= num_2
print("Assignment Integer Division: ", a)
print("--------------------------------")

# Comparison Operators
if num_1<num_2:
    print("Number 1 is less than Number 2")
elif num_1>num_2:
    print("Number 1 is greater than Number 2")
elif num_1==num_2:
    print("Number 1 is equal to Number 2")
print("--------------------------------")

# Logical Operators
if num_1>0 and num_2>0:
    print("Both numbers are positive")
elif num_1>0 or num_2>0:
    print("At least one number is positive")
elif not(num_1>0):
    print("Number 1 is not positive")
elif not(num_2>0):
    print("Number 2 is not positive")
print("--------------------------------")

# Identity Operators
if num_1 is num_2:
    print("Number 1 and Number 2 are identical")
elif num_1 is not num_2:
    print("Number 1 and Number 2 are not identical")
print("--------------------------------")

# Membership Operators
list = [1,"name",1.345,True, num_1]
if num_1 in list:
    print("Number 1 is present in the list")
elif num_1 not in list:
    print("Number 1 is not present in the list")
elif num_2 in list:
    print("Number 2 is present in the list")
elif num_2 not in list:
    print("Number 2 is not present in the list")
print("--------------------------------")


# TASK 4

# string concatenation
str=("Student Name: " + stud_name + "\nRoll no: " + str(roll_no) + "\nProgram: " + program + "\nUniversity Name: " + uni_name + "\nCity: " + city + "\nAge: " + str(age) + "\nHobby: " + hobby)
print(str)
print("--------------------------------")

# f-strings

f_str= (f"Student Name: {stud_name}")
print(f_str)
print("--------------------------------")

# Escape sequences

New_Line=(f"Student Name: {stud_name}\nRoll no:{roll_no}")
print(New_Line)
Tab_Space=(f"University\tname: {uni_name}\\City: {city}")
print(Tab_Space)
Back_slash=(f"program: {program}\City: {city}")
print(Back_slash)
Quotes=(f"hobby: {hobby}\Age: {age}")
print(Quotes)
print("--------------------------------")

# String Functions

len = len(stud_name)
print("Length of Student Name: ", len)
University_name= uni_name.endswith("University")
print("Does University Name end with 'University'? ", University_name)
programm= program.count("A")
print("Count of 'A' in Program: ", programm)
cityy= city.upper()
print("City in Uppercase: ", cityy)
hobbyy= hobby.find("ing")
print("Index of 'ing' in Hobby: ", hobbyy)
stud_namee= stud_name.startswith("A")
print("Does Student Name start with 'A'? ", stud_namee)

# TASK 5
profile=(f'''-------------------------------------------
        |Student Profile System|
-------------------------------------------
      Name:         {stud_name}
      Roll no:      {roll_no}
      Course:       {program}
      University:   {uni_name}
      City:         {city}
      Age:          {age}
      Hobby:        {hobby}
-------------------------------------------
WELCOME TO PYTHON PROGRAMMING!!''')
print(profile)


# TASK 6 ( Bonus Task)
while True:
    ask =(input("Do you Want to Save Your Profile? (y/Y/n/N): "))
    if ask in('n','N'):
        break
    elif ask in('y','Y'):
        file=open("Student_Profile.txt","w")
        file.write(profile)
        file.close()
        file1=open("Student_Profile.txt","r")
        print(file1.read())
        file.close()