class Player:
    def __init__(self, name_string, answers_list, score_int):
        self.name = name_string
        self.answers = answers_list
        self.score = score_int


class GameState:
    players = dict()  # list contains player objects
    current_round = 0
    categories_asked = list()
    questions = list()  # list of question objects

    def add_player(self, player):  # Player object
        global players
        players[player.name] = player

    def remove_player(self, player_name):
        global players
        del players[player_name]

    def add_answer(self, position, player_name):
        global players
        players[player_name][1].append(position)  # hard coded position

    def get_current_results(self, player):  # player object
        results = dict()
        position = 0
        global questions

        for question in questions:
            results[position] = question + player.answers[position]
            position += 1

        return results

    def check_answer(self, player, question_correct_answer, player_answer):
        if player_answer == question_correct_answer:
            player.score += 1
            return True
        return False
