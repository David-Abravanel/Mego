class Question:
    def __init__(self, dic:dict):
        # The function _read() returns all the question parts
        self._the_question, \
            self._answer1, \
            self._answer2, \
            self._answer3, \
            self._answer4, \
            self._the_correct_answer = self._read(dic)

    def _read(self, dic: dict[str:str,]) -> dict[str:int]:
        return dic['Question'], \
            dic['Answer1'], \
            dic['Answer2'], \
            dic['Answer3'], \
            dic['Answer4'], \
            dic['Accurate']

    def is_correct(self, the_player_choice):
        return the_player_choice == self._the_correct_answer

    def __repr__(self) -> str:
        return f"\nThe question is ::: {self._the_question}\n\n\
    1. {self._answer1}.\n\
    2. {self._answer2}.\n\
    3. {self._answer3}.\n\
    4. {self._answer4}.\n"
