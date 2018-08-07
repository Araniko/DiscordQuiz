import csv

# Categories:

# In-depth - Framedata moves
# In-depth - Killpercents
# Yoshi properties
# Know your Moves - Airials
# KYM - Grounded
# KYM - Specials
# Know your stages
# Yoshi Lore
# Matchups
# Changes in Smash 4

import random


class Question:

    def __init__(self, text, answer1, answer2, answer3, answer4):
        self.question_text = text
        self.correct_answer = answer1
        self.wrong_answer1 = answer2
        self.wrong_answer2 = answer3
        self.wrong_answer3 = answer4


questions = dict()


def get_questions():
    return questions


def load_questions_from_csv():
    global questions

    with open('../res/Questions.csv', newline='') as questionsFile:
        csv_rows = list(csv.reader(questionsFile, delimiter=';', quotechar='\''))
        for row in csv_rows[1:]:
            if row[0] not in questions.keys():
                questions[row[0]] = list()
            question = Question(row[1], row[2], row[3], row[4], row[5])
            questions[row[0]].append(question)


def get_random_questions(amount, question_category):
    global questions

    question_positions = random.sample(range(0, len(questions[question_category])), amount)
    chosen_questions = list()
    for number in question_positions:
        chosen_questions.append(questions[question_category][number])
    return chosen_questions


def get_categories():
    return list(questions.keys())


def get_random_categories(amount, categories):
    chosen_categories = list()

    category_positions = random.sample(range(0, len(categories)), amount)
    for position in category_positions:
        chosen_categories.append(categories[position])
    return chosen_categories
