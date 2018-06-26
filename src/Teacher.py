import codecs
import glob
import json
import os

from pandas import DataFrame


# Teacher class includes teacher system func as create test and export data to excel
class Teacher(object):
    def __init__(self, teacher_name, exam_name):
        self.teacher_name = teacher_name
        self.exam_name = exam_name
        self.exam_data = {"exam name": exam_name, "teacher name": teacher_name, "questions": []}
        with open("./train_data.json", 'r', encoding="utf-8") as json_file:
            self.train_data = json.load(json_file, encoding='utf-8')

    def create_new_test(self):
        """ Create a new test for specific teacher, questions type of dictation and sentence completion """
        print("Hey "+self.teacher_name+', lets build '+self.exam_name+"(Please fill all english answers lowercase)")
        q_type = input("Chose question to add or finish:\n1.Dictation\n2.Completion of sentence\n3.finish\n")
        while q_type != '3':
            if q_type == '1':
                self.create_dictation_q()
            elif q_type == '2':
                self.create_sentence_q()
            else:
                print("Please insert one of the following options(1,2,3)")
            q_type = input("Chose question type or finish:\n1.Dictation\n2.Completion of sentence\n3.finish\n")
        with codecs.open('./exams/'+self.exam_name+'.json', 'wb', encoding='utf-8') as exam_file:
            json.dump(self.exam_data, exam_file, ensure_ascii=False)    # write to test json
        with codecs.open('./train_data.json', 'wb', encoding='utf-8') as train_file:
            json.dump(self.train_data, train_file, ensure_ascii=False)  # write to train  json

    def create_dictation_q(self):
        """ Create a new dictation question q-question, a-answer """
        q = input("Enter the hebrew word:\n")
        a = input("Enter the english translate:\n")
        self.exam_data['questions'].append({'type': 1, 'q': q, 'a': a})
        self.train_data['questions'].append({'type': 1, 'q': q, 'a': a})
        return

    def create_sentence_q(self):
        """ Create a new sentence complete question q-question, a1- true answer """
        q = input("Insert the sentence so that the missing word is marked as a line ______: \n")
        a1 = input("Insert the true missing word:")
        a2 = input("Insert false option:")
        a3 = input("Insert second false option:")
        a4 = input("Insert third false option:")
        self.exam_data['questions'].append({'type': 2, 'q': q, 'a': [a1, a2, a3, a4]})
        self.train_data['questions'].append({'type': 2, 'q': q, 'a': [a1, a2, a3, a4]})

    def create_exam_report(self, exam_name):
        """ Export names,id and grades of specific exam to an excel file """
        files_list = glob.glob("./checked_exams/"+exam_name+'*')    # get all the exam files
        student_names = []
        student_IDs = []
        student_grades = []
        for file in files_list:
            with open(file, "r", encoding='utf-8') as f:
                for i, line in enumerate(f):
                    if i == 1:
                        student_names.append(fix_string(line))
                    if i == 2:
                        student_IDs.append(fix_string(line))
                student_grades.append(fix_string(line))
        df = DataFrame({'Student Name': student_names, 'ID': student_IDs, 'Grade': student_grades})
        df = df[['Student Name', 'ID', 'Grade']]
        df.to_excel("./Reports/"+exam_name+'.xls', sheet_name=exam_name+' grades', index=False)
        file = "cd ./Reports & start excel "+exam_name
        os.system(file)


def fix_string(line):
    tmp = line.split(':')
    tmp[-1] = tmp[-1].replace('\n', "")
    tmp[-1] = " ".join(tmp[-1].split())
    return tmp[-1]