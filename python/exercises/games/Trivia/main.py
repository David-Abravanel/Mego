from questions import Questions
from players import *
import os


def print_score(players: list[Player]):
    os.system('cls')
    print('The players\' points:\n')
    for ply in players:
        print(" ● ",ply)


def get_number_between_1_4(player: Player):
    while True:
        num_chose = input(f'{player.get_name()} choose a number between 1 and 4: ')

        if not num_chose.isnumeric() or int(num_chose) > 4 or int(num_chose) < 1:
            print("\n  >>>  Invalid input:\n ")
        else:
            return int(num_chose)


def trivia_game():
    players = Players()
    questions = Questions(players.num_of_questions)
    question = questions.pop()
    player = players.get_next()

    while True:
        print_score(players.get_players())
        print(question)

        num_chose = get_number_between_1_4(player)
        if not question.is_correct(num_chose):
            player = players.get_next()
        else:
            player.add_score()
            input(f'\n{player.get_name()}, you answered correctly!\n\n>>> press any key to continue...')

            if questions.is_empty():
                break
            question = questions.pop()

    max_score = 0
    print_score(players.get_players())
    players_list = players.get_players()
    winner = None

    for player in players_list:
        if player.get_score() > max_score:
            max_score = player.get_score()
            winner = player.get_name()

    if winner:
        print(f"\n{winner} you are the winner!\n")


if __name__ == "__main__":
    trivia_game()
