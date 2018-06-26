from Teacher import Teacher
from Student import Student
import os
import getpass

# User interface
if __name__ == '__main__':
    print("Welcome to english exams system")
    user_type = input("Are you ?(please enter 1 or 2) \n1.Student\n2.Teacher\n")
    while user_type != "1" and user_type != "2":
        print("Wrong input! please enter 1 or 2")
        user_type = input("Are you ?(please enter 1 or 2) \n1.Student\n2.Teacher\n")

    if user_type == "1":
        student_name = input("Please enter your name:\n")
        student_id = input("Enter ID:\n")
        student = Student(student_name, student_id)
        choice = None
        while choice is None:
            try:
                choice = input("please choose one of the option:\n1. Practice questions.\n2. Start Exam.\n")
                choice = int(choice)
            except ValueError:
                print("please enter the number of your choice from the range 1-2")
                choice = None
            if choice != None and choice not in range(1, 3):
                choice = None
        if choice == 1:
            student.train()
        else:
            student.exam()

    elif user_type == "2":
        # Add password (not working on pycharm! only cmd)
        '''
        p = "null"  # user's input start value
        pas = "password"  # password value
        while p != pas:
            p = getpass.getpass("Insert your password: ")  # password input
        print("Password confirmed")  # when you get the password, the output is "ay"
        '''
        teacher_name = input("Please enter your name:\n")
        choice = None
        while choice is None:
            try:
                choice = input("please choose one of the option:\n1. Create new Exam.\n2. Create exam report.\n")
                choice = int(choice)
            except ValueError:
                print("please enter the number of your choice from the range 1-2")
                choice = None
            if choice != None and choice not in range(1, 3):
                choice = None
        if choice == 1:
            exam_name = input("Insert the exam name:\n")
            teacher = Teacher(teacher_name, exam_name)
            teacher.create_new_test()
        elif choice == 2:
            print("please Enter the name of the test you want to create a report:\nExam list: ")
            files_list = []
            for root, dirs, files in os.walk("./Exams"):
                for i, filename in enumerate(files):
                    print("{}.\t{}".format(i + 1, filename[:-5]))
                    files_list.append(filename[:-5])
            exam_name = input()
            while exam_name not in files_list:
                print("There is no such test in the system, please try again")
                exam_name = input()
            teacher = Teacher(teacher_name, exam_name)
            teacher.create_exam_report(exam_name)

    print("Thank you, see you soon...")
