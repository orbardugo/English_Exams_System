import json
import os





class Student(object):
    def __init__(self, name, ident):
        self.name = name
        self.ident = ident

    def exam(self):
        correct_ans_counter = 0
        print("Choose exam from the list and enter his name:")
        for root, dirs, files in os.walk("./Exams"):
            for i, filename in enumerate(files):
                print("{}.\t{}".format(i+1, filename[:-4]))
        choose = input()

        exam = None
        while exam is None:
            try:
                exam = open_file(choose)
            except FileNotFoundError:
                choose = input("Wrong file name, please enter again the file name\n")

        res_file = open(choose+"-"+self.name,"w+")


        for question in exam['questions']:
            q_type = question['type']
            if q_type == 1:#dictation
                print(question['q'])
                ans = input("Please enter the missing word in order:\t")
                check_and_write_ans(ans, question['a'], res_file)



def open_file(file_name):
    with open("./Exams/"+file_name+".txt") as json_file:
        exam = json.load(json_file)
    return exam


def check_and_write_ans(student_ans, correct_ans, res_file):
    if student_ans != correct_ans:
        res_file.write("answer: {}, correct answer: {}  X")
    else:
        res_file.write("answer: {}, correct answer: {}  √")

Or = Student("Or Bardugo", "302891551")
Or.exam()