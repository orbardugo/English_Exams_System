import codecs
import json


class Teacher(object):
    def __init__(self, teacher_name, exam_name):
        self.teacher_name = teacher_name
        self.exam_name = exam_name
        self.data = {"exam name": exam_name, "teacher name": teacher_name, "questions": []}

    def create_new_test(self):
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
        with codecs.open(self.exam_name+'.json', 'wb', encoding='utf-8') as exam_file:
            json.dump(self.data, exam_file, ensure_ascii=False)

    def create_dictation_q(self):
        q = input("Enter the hebrew word:\n")
        a = input("Enter the english translate:\n")
        self.data['questions'].append({'type': 1, 'q': q, 'a': a})
        return

    def create_sentence_q(self):
        q = input("Insert the sentence so that the missing word is marked as a line ______: \n")
        a1 = input("Insert the true missing word:")
        a2 = input("Insert false option:")
        a3 = input("Insert second false option:")
        a4 = input("Insert third false option:")
        self.data['questions'].append({'type': 2, 'q': q, 'a1': a1, 'a2': a2, 'a3': a3, 'a4': a4})

