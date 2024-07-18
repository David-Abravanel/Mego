import json
import random
import pathlib
from player import Player
from question import Question
import os

def registration() -> tuple[int, list[Player]]:
    num_of_players = get_valid_number(
        '\nWelcome to trivia game:\n\nFirst: How many players are you? ')
    num_of_questions = get_valid_number(
        '\nSecond: How many questions would you like to play? ')
    
    return num_of_questions, num_of_players


def get_questions(num_of_chosen_questions):
    current_path_file = pathlib.Path(__file__)
    questions_path = current_path_file.parent / "questions_file.json"
    list_of_dic_questions = json.loads(questions_path.read_text())
    random.shuffle(list_of_dic_questions)

    return list_of_dic_questions[:num_of_chosen_questions]


def get_valid_number(message: str) -> int:
    while True:
        number = input(message)
        if not number.isnumeric() or int(number) < 1:
            number = print(
                '\nError -> Not a Number: lets try again')
        else:
            return int(number)


def print_score(players: list[Player]) -> None:
    os.system('cls')
    print('The players\' points:\n')
    for player in players:
        print(" ● ", player)


def get_number_between_1_4(player: Player) -> int:
    while True:
        num_chose = get_valid_number(f'{player.get_name()} choose a number between 1 and 4: ')

        if int(num_chose) > 4 or int(num_chose) < 1:
            print("\n  >>>  Invalid input:\n ")
        else:
            return int(num_chose)


def print_the_winner(players:list[Player]):
    print_score(players)
    max_score = max(player.get_score() for player in players)
    winner = [player for player in players if player.get_score() == max_score]
    if len(winner) > 1:
        for win in winner:
            print(win.get_name(),sep="and ",end=" ")
        print(" you are the winners!\n")
    else:
        print(f"\n{winner[0].get_name()} you are the winner!\n")


def trivia_game() -> None:
    num_of_questions, num_of_players = registration()
    list_of_dic_questions = get_questions(num_of_questions)
    players = [Player(input(f'\nPlayer {i+1}, type your name: ')) for i in range(num_of_players)]
    questions = [Question(question) for question in list_of_dic_questions]

    question = questions.pop()
    player_turn = 0
    player = players[player_turn]

    while True:
        print_score(players)
        print(question)

        num_chose = get_number_between_1_4(player)
        if not question.is_correct(num_chose):
            player = players[(player_turn+1) % num_of_players]
        else:
            player.add_score()
            input(f'\n{player.get_name()}, you answered correctly!\n\n>>> press any key to continue...')

            if questions == []:
                break
            question = questions.pop()

    print_the_winner(players)


if __name__ == "__main__":
    trivia_game()