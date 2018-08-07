import QuestionLogic


def main():
    QuestionLogic.load_questions_from_csv()
    chosen_questions = QuestionLogic.get_random_questions(1, "Memes")
    print(chosen_questions[0].question_text)

    print(QuestionLogic.get_random_categories(2, QuestionLogic.get_categories()))


if __name__ == '__main__':
    main()
