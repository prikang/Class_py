# 1. Asks the user for the number and print the multiplication table of that specific number.
# Number=int(input("Enter the number: "))
# for i in range(1,11):
#     result= i*Number
#     print(f"{Number} X {i} = {result}")

#  2. You have got the student marks as {1:70, 2:30, 3:90, 4:75, 5:88, 6:86, 7:76, 8:66, 9:40} get the lists of student roll who has pass the exam
student_marks = {1:70, 2:30, 3:90, 4:75, 5:88, 6:86, 7:76, 8:66, 9:40}
passing_marks=50
passed_students = [roll for roll, marks in student_marks.items() if marks >= passing_marks]
print("Roll of students who passed the exam: ", passed_students)



#  3. Get the input from user and define the odd and even
# Num=int(input("Enter the number: "))
# if Num%2==0:
#     print("The user input is even")
# else:
#     print("The use input is odd")