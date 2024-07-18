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
