import csv
from difflib import SequenceMatcher



class exam_demo:
    qid=0
    job_name = ''
    job_company = ''
    load_question=0
    mark=0
    average=0
    ar_check_sts=0
    question_list = []
    answer_list = []
    file = 'dataset.csv'
    def __init__(self):
        with open(exam_demo.file) as f:
            reader = csv.DictReader(f, delimiter=',')
            for row in reader:

                t1 = row['company']
                t2 = row['job']
                t3 = row['question']
                t4 = row['answer']
                print(exam_demo.job_company, exam_demo.job_name)
                if exam_demo.job_name == t2:
                    exam_demo.question_list.append(t3)
                    exam_demo.answer_list.append(t4)
        # print(exam_demo.question_list)


    def read_question(self,qid):
        if qid<10:
            question=exam_demo.question_list[qid]
            answer=exam_demo.answer_list[qid]
            return question,answer
        else:
            return 'no','no'

    def match_answer(self,user_inut,original_answer):
        return SequenceMatcher(None, user_inut, original_answer).ratio()

# answer='demo sample'
# qid=5
# arn=exam_demo()
# question,answer=arn.read_question(qid)
# # print(question)
# user_input=input("Enter Your Answer")
# mark=arn.match_answer(user_input,answer)
# print(mark)

