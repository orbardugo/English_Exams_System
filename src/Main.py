from Teacher import Teacher
from Student import Student
import getpass

if __name__ == '__main__':
    print("Welcome to english exams system")
    user_type = input("Are you ?(please enter 1 or 2) \n1.Student\n2.Teacher\n")
    while user_type != "1" and user_type != "2":
        print("Wrong input! please enter 1 or 2")
        user_type = input("Are you ?(please enter 1 or 2) \n1.Student\n2.Teacher\n")

    if user_type == "1":
        student_name = input("Please enter your name:\n")
        student_id = input("Enter ID:\n")
        student = Student(student_name,student_id)
        student.exam()

    elif user_type == "2":
        p = "null"  # user's input start value
        pas = "password"  # password value
        while p != pas:
            p = getpass.getpass("Insert your password: ")  # password input
        print("Password confirmed")  # when you get the password, the output is "ay"
        teacher_name = input("Please enter your name:\n")
        exam_name = input("Insert the exam name:\n")
        teacher = Teacher(teacher_name, exam_name)
        teacher.create_new_test()

    print("Thank you, see you soon...")
