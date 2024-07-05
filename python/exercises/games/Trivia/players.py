import random

class Player:
    def __init__(self, name) -> None:
        # logic - error: if the name isn't a letter
        self._name = name[0].upper() + name[1:]
        self._score = 0

    def add_score(self):
        self._score += 1

    def get_name(self):
        return self._name

    def get_score(self):
        return self._score

    def __repr__(self) -> str:
        return f'{self._name} has {self._score} points'


class Players:

    def __init__(self) -> None:
        self.num_of_questions, \
        self._players = self._registration()
        random.shuffle(self._players)
        self._num_of_players = len(self._players)
        self._current_player = 0


    def _registration(self):
        num_of_players = self._get_valid_number(
            '\nWelcome to trivia game:\n\nFirst: How many players are you? ')
        num_of_questions = self._get_valid_number(
            '\nSecond: How many questions would you like to play? ')
        return num_of_questions, [Player(input(f'\nPlayer {i+1}, type your name: ')) for i in range(num_of_players)]


    def get_next(self):
        self._current_player = (self._current_player + 1) % self._num_of_players
        return self._players[self._current_player]

    def get_players(self):
        return self._players

    def _get_valid_number(self, message: str) -> int:
        number = input(message)
        while True:
            if not number.isnumeric() or int(number) < 1:
                number = input(
                    '\nError -> Not a Number:\n For the number of players,\n you must type a number greater than 0:')
            else:
                return int(number)
