import json
import os
import random
import time


class Student(object):
    def __init__(self, name, ident):
        self.name = name
        self.ident = ident
        self.correct_ans_counter = 0

    def train(self):
        print("Welcome to train mode, here you'll get feedback after each question..\nLets begin!(type exit in any time to stop training)")
        train_file = open_file("train_data", "train")
        suffle_q = train_file['questions']
        random.shuffle(suffle_q)
        for question in suffle_q:
            q_type = question['type']
            if q_type == 1:
                print("Write the following word in english:")
                ans = input(question['q'] + "\nIn english: ")
                if ans == "exit":
                    return
                self.check_train_ans(ans, question['a'])
            else:  # dictation
                ans_option_list = []
                for option in question['a']:
                    ans_option_list.append(option)
                random.shuffle(ans_option_list)
                print("Chose the missing word to complete the sentence (1-4):\n" + question['q'])
                for index, a in enumerate(ans_option_list):
                    print("{}.  {}".format(index + 1, a))
                ans = None
                while ans is None:
                    try:
                        ans = input("your choice is: ")
                        if ans == "exit":
                            return
                        ans = int(ans)
                    except ValueError:
                        print("please enter number from the range 1-4")
                        ans = None
                    if ans != None and ans not in range(1, 5):
                        ans = None
                self.check_train_ans(ans_option_list[ans - 1], question['a'][0])




    def exam(self):
        correct_ans_counter = 0
        print("Choose exam from the list and enter his name:")
        for root, dirs, files in os.walk("./Exams"):
            for i, filename in enumerate(files):
                print("{}.\t{}".format(i+1, filename[:-5]))
        choose = input()
        exam = None
        while exam is None:
            try:
                exam = open_file(choose, "exam")
            except FileNotFoundError:
                choose = input("Wrong file name, please enter again the file name\n")

        res_file = open("./checked_exams/"+choose+"-"+self.name+".txt", "w+", encoding='utf-8')
        res_file.write("{}\nStudent name:   {}\nStudent ID: {}\n".format(time.strftime("%d/%m/%Y %H:%M:%S"), self.name, self.ident))
        for question in exam['questions']:
            q_type = question['type']
            if q_type == 1:
                print("Write the following word in english:")
                ans = input(question['q']+"\nIn english: ")
                self.check_and_write_ans(question['q'], ans, question['a'], res_file)
            else: # dictation
                ans_option_list = []
                for option in question['a']:
                    ans_option_list.append(option)
                random.shuffle(ans_option_list)
                print("Chose the missing word to complete the sentence (1-4):\n"+question['q'])
                for index, a in enumerate(ans_option_list):
                    print("{}.  {}".format(index+1, a))
                ans = None
                while ans is None:
                    try:
                        ans = input("your choice is: ")
                        ans = int(ans)
                    except ValueError:
                        print("please enter number from the range 1-4")
                        ans = None
                    if ans != None and ans not in range(1,5):
                        ans = None

                self.check_and_write_ans(question['q'], ans_option_list[ans-1], question['a'][0], res_file)
        res_file.write("Your final grade:   "+ str(int((100/len(exam['questions']))*self.correct_ans_counter)))
        res_file.close()

    def check_and_write_ans(self, question, student_ans, correct_ans, res_file):
        if student_ans != correct_ans:
            res_file.write(
                "question: '{}', Your answer: {}, Correct answer: {}  X\n".format(question, student_ans, correct_ans))
        else:
            res_file.write(
                "question: '{}', Your answer: {}, Correct answer: {}  √\n".format(question, student_ans, correct_ans))
            self.correct_ans_counter += 1

    def check_train_ans(self, student_ans, correct_ans):
        if student_ans != correct_ans:
            print("WRONG!(X) - The correct answer is: "+ correct_ans + "\n")

        else:
            print("CORRECT!(√)\n")


def open_file(file_name, flag):
    if(flag == "exam"):
        with open("./Exams/"+file_name+".json", 'r', encoding="utf-8") as json_file:
            data = json.load(json_file, encoding='utf-8')
    else:
        with open("./"+file_name+".json", 'r', encoding="utf-8") as json_file:
            data = json.load(json_file, encoding='utf-8')

    return data

amir = Student("Amir","203881818")
amir.train()