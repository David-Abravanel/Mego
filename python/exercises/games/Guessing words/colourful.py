import os
import pyautogui
import random as rnd 
from colorama import Style, Fore, Back, init
# from bidi.algorithm import get_display
init(autoreset=True)
colors = [Fore.GREEN,Fore.BLUE,Fore.LIGHTYELLOW_EX,Fore.MAGENTA,Fore.CYAN,Fore.BLACK]


def regestrtion() -> tuple:

    numOfPlayers = get_valid_number(
        input(Fore.MAGENTA+" >> Registration:\n"+Fore.YELLOW+"Enter the number of the players: "+Style.RESET_ALL))
    numOfWords = get_valid_number(
        input(Fore.YELLOW+"Enter the number of the words you want to play: "+Style.RESET_ALL))
    nameOfThePlayers = [
        colors[num]+input(colors[num]+f"\n player {num + 1} enter your name: ")+Style.RESET_ALL for num in range(numOfPlayers)]

    return nameOfThePlayers, numOfPlayers, numOfWords


def get_valid_number(num:str) -> int:
    while True:
        if(not num.isnumeric()):
            num = input('\nInvalid input:\n\n Enter a number  : ')
        else:
            return int(num)


def extracting_words(num_word: int) -> tuple:
    with open('words.txt', 'r+', encoding='utf-8') as file:
        content = file.read()
        dictionary_words = content.split(',')

        # Pulls a number of words randomly from the dictionary
        random_words = rnd.sample(dictionary_words, num_word)

    english_words, hebrew_words = [], []
    for i in range(num_word):
        dec = random_words[i].split(':')
        english_words.append(dec[0].lower())
        hebrew_words.append(dec[1].lower())

    return english_words, hebrew_words


def Bonus(score: list, Names: list, english_words: str, hebrew_words: str) -> list:
    switch_language()

    print(Fore.MAGENTA+'Bonus:\nwrite the word in hebrew.\n',len(hebrew_words.split()),Fore.MAGENTA+" Words ", len(hebrew_words), Fore.MAGENTA+" Letters\n")
    for i in range(len(Names)):
        if input(f'Players {Names[i]}, translate this word in hebrew? ') == hebrew_words:
            score[i] += len(hebrew_words)

    switch_language()
    return score


# Do to meny staff...
def Display(name: list, score: list, word: list, this_word: int, num_of_words: int,letters_found) -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.MAGENTA+'You have guessed '+Style.RESET_ALL+f'{this_word}'+Fore.MAGENTA+' words out of '+Style.RESET_ALL+f'{num_of_words}'+Fore.MAGENTA+' words\n'+Style.RESET_ALL)
    print(">> Player scores: ")
    # can do with zip
    for i in range(len(name)):
        print(f":: {name[i]} = {score[i]}")
    print()

    print(Fore.GREEN+f"{letters_found}","Letters out of",Fore.GREEN+f"{len(word)}","have been found: ", end="")
    for j in range(len(word)):
        if(word[j] == '* '):
            print(Fore.RED+word[j], end="")
        else:
            print(Fore.GREEN+word[j], end="")
    print('\n')


# Do to meny staff...
def get_letter_from_user(player: str, word: list) -> str:

    while True:
        letter = input(f'Player {player}, guess a letter: ')

        if not letter.isalpha():
            print('\nInvalid input:\n >> Enter a letter\n')

        elif len(letter) > 1:
            print('\nInvalid input:\nYou can only enter one letter: \n')

        elif letter+" " in word:
            print('\nThis letter has already been found:\n >> Try again: \n')

        else:
            return letter.lower()


def cheak_leter_in_word(letter: str, haide_word: str, display_word: list,player: int) -> tuple:
    status = False
    corect_gesses = 0

    for i in range(len(haide_word)):
        if letter == haide_word[i]:
            display_word[i] = f"{haide_word[i]} "
            corect_gesses += 1
            status = True

    return display_word, status, corect_gesses


def switch_language():
    pyautogui.keyDown('alt')
    pyautogui.press('shift')
    pyautogui.keyUp('alt')


# Do to meny staff...
def main_game() -> None:
    players_names, num_of_players, num_of_words = regestrtion()
    players_score = [0] * num_of_players
    english_words, hebrew_words = extracting_words(num_of_words)

    for i in range(num_of_words):
        word = ['* '] * len(english_words[i])

        gesses_letters = 0
        Display(players_names, players_score, word, i, num_of_words,gesses_letters)

        player_tourn = 0
        while '* ' in word:
            letter = get_letter_from_user(players_names[player_tourn], word)
            word, is_in, gesses_found = cheak_leter_in_word(
                letter, english_words[i], word,player_tourn)

            if is_in == True:
                gesses_letters += gesses_found
                players_score[player_tourn] += gesses_found
                # print(f'Player {players_names[player_tourn]} you have successfully guessed a letter ')

            Display(players_names, players_score, word, i, num_of_words,gesses_letters)
            player_tourn = (player_tourn + 1) % num_of_players
        
        players_score = Bonus(players_score, players_names, english_words[i], hebrew_words[i])

    Display(players_names, players_score, word, i+1, num_of_words,gesses_letters)
    print(players_names[players_score.index(max(players_score))],'is the winer\n')


main_game()