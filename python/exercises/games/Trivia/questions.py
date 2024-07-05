import pathlib
import json
import random


class Question:
    def __init__(self, dic):
        # The function _read() returns all the question parts
        self.__the_question, \
            self.__answer1, \
            self.__answer2, \
            self.__answer3, \
            self.__answer4, \
            self.__the_answer = self._read(dic)

    def _read(self, dic: dict[str:str,]) -> dict[str:int]:
        return dic['Question'], \
            dic['Answer1'], \
            dic['Answer2'], \
            dic['Answer3'], \
            dic['Answer4'], \
            dic['Accurate']

    def is_correct(self, the_player_choice):
        return the_player_choice == self.__the_answer

    def __repr__(self) -> str:
        return f"\nThe question is ::: {self.__the_question}\n\n\
    1. {self.__answer1}.\n\
    2. {self.__answer2}.\n\
    3. {self.__answer3}.\n\
    4. {self.__answer4}.\n"


class Questions:
    # stand by: list_dic: list[dict]
    def __init__(self, num_of_questions):
        self._questions = self._get_questions(num_of_questions)
        self._num_of_questions = len(self._questions)
        self._questions_asked = 0

    def _get_questions(self, num_of_chosen_questions):
        current_path_file = pathlib.Path(__file__)
        questions_path = current_path_file.parent / "questions_file.json"
        list_of_dic_questions = json.loads(questions_path.read_text())
        random.shuffle(list_of_dic_questions)
        
        return [Question(question) for question in list_of_dic_questions[:num_of_chosen_questions]]

    def pop(self):
        self._questions_asked += 1
        return self._questions.pop()
    
    def is_empty(self):
        return self._num_of_questions == self._questions_asked
