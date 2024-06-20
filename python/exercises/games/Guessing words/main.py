import os
import random as rnd
# from colorama import Style, Fore, Back, init
# from bidi.algorithm import get_display
# init(autoreset=True)


def Regestrtion() -> tuple:

    numOfPlayers = GetValidNumbers(
        input(" >> Registration:\nEnter the number of the players: "))
    numOfWords = GetValidNumbers(
        input("Enter the number of the words you want to play: "))
    nameOfThePlayers = [
        input(f" player {num + 1} enter your name: ") for num in range(numOfPlayers)]

    return nameOfThePlayers, numOfPlayers, numOfWords


def GetValidNumbers(num:str):
    while True:
        if(not num.isnumeric()):
            num = input('\nInvalid input:\n Enter a number\n\n   : ')
        else:
            return int(num)


def ExtractingWords(numword: int) -> tuple:
    with open('words.txt', 'r+', encoding='utf-8') as file:
        content = file.read()
        dicwords = content.split(',')
        randomWords = rnd.sample(dicwords, numword)

    english, hebrew = [], []
    for i in range(numword):
        dec = randomWords[i].split(':')
        english.append(dec[0].lower())
        hebrew.append(dec[1].lower())

    return english, hebrew


def bonus(score: list, Names: list, english: str, hebrew: str) -> list:
    print('Bonus:\nTry to write the word in Hebrew.\n',len(hebrew.split())," Words ", len(hebrew), " Letters\n")
    for i in range(len(Names)):
        if input(f'Player {Names[i]}, what is the translation of the word {english}? ') == hebrew:
            score[i] += len(hebrew)

    return score


def Display(PlayNam: list, PlayScr: list, word: list, Numword: int, numTotalWords: int) -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'You have guessed {Numword} words out of {numTotalWords} words\n')
    print(" >> The players' scores: ")
    for i in range(len(PlayNam)):
        print(f":: {PlayNam[i]} = {PlayScr[i]}")
    print()

    print(f"Letters that have been found in word {Numword + 1}: ", end="")
    for j in range(len(word)):
        print(word[j], end="")
    print('\n')


def GetValidLetter(player: str, word: list) -> str:
    while True:
        letter = input(f'Player {player}, guess a letter: ')
        if not letter.isalpha():
            print('\nInvalid input:\n >> Enter a letter\n')
        elif len(letter) > 1:
            print('\nInvalid input:\nYou can only enter one letter: \n')
        elif f"{letter} " in word:
            print('\nThis letter has already been found:\n >> Try again: \n')
        else:
            return letter.lower()


def CheakLeterInWord(letter: str, wordHaide: str, wordDisplay: list) -> tuple:
    status = False
    corectGesses = 0

    for i in range(len(wordHaide)):
        if letter == wordHaide[i]:
            wordDisplay[i] = f"{wordHaide[i]} "
            corectGesses += 1
            status = True

    return wordDisplay, status, corectGesses


def TheMainGame() -> None:
    PlayersNames, numPlay, namTotalWords = Regestrtion()
    PlayersScore = [0] * numPlay
    words, hebrew_words = ExtractingWords(namTotalWords)

    for i in range(namTotalWords):
        word = ['* '] * len(words[i])

        Display(PlayersNames, PlayersScore, word, i, namTotalWords)

        playerTourn = 0
        while '* ' in word:
            letter = GetValidLetter(PlayersNames[playerTourn], word)
            word, status, gessesFound = CheakLeterInWord(
                letter, words[i], word)

            if status:
                PlayersScore[playerTourn] += gessesFound
                # print(f'Player {PlayersNames[playerTourn]} you have successfully guessed a letter ')

            Display(PlayersNames, PlayersScore, word, i, namTotalWords)
            playerTourn = (playerTourn + 1) % numPlay
        
        PlayersScore = bonus(PlayersScore, PlayersNames, words[i - 1], hebrew_words[i - 1])

    print('The winer is ', PlayersNames[PlayersScore.index(max(PlayersScore))])


TheMainGame()
