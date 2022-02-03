#!/usr/bin/env python3
# wordle.py
'''
This script was made to mimic the popular worlde game
that was just aquired by the NY Times.
'''
import sys
import os
from termcolor import colored

def clear_board():
    '''Function to clear board'''
    os.system('clear')

def make_wordle_word():
    '''Let the user define a worlde to guess'''

    wordle_word = input('Wordle of the day: ')
    while len(wordle_word) != 5:
        print('Please input a 5 letter word')
        wordle_word = input('Wordle of the day: ')

    return wordle_word

def wordle_check_word(wordle_word):
    '''
    Takes in user defined worlde word and outputs the colorized
    green version so we can check player guess against it
    '''
    green_wordle = []

    for letter in wordle_word:
        green_wordle.append(colored(letter, 'green'))

    return green_wordle

def print_board(rows):
    '''Prints the board'''
    for row in rows:
        print(*row)

def take_guess():
    '''Takes in the user guess'''
    list_of_guess = []
    guess = input('Take a guess: ')
    for letter in guess:
        list_of_guess.append(letter)

    return list_of_guess

def return_colored_word(word, guess):
    '''
    Takes in the worlde word and user guess to return
    the colorized version of it to be printed
    '''
    correct_letter = []
    incorrect_letter = []
    not_in_word = []

    for i, letter in enumerate(guess):
        if guess[i] == word[i]:
            correct_letter.append(letter)
        elif letter in word:
            incorrect_letter.append(letter)
        else:
            not_in_word.append(letter)

    # THIS VERSION FINALLY WORKS!
    colored_guess = []
    for i, letter in enumerate(guess):
        if letter in correct_letter and guess[i] == word[i]:
            colored_guess.append(colored(letter, 'green'))
        elif letter in incorrect_letter and letter in correct_letter:
            colored_guess.append(colored(letter, 'red'))
        elif letter in incorrect_letter:
            colored_guess.append(colored(letter, 'yellow'))
        else:
            colored_guess.append(colored(letter, 'red'))

    return colored_guess

def main():
    '''
    Making the game play for wordle
    '''

    # Making beginning board
    row1 = ['_'] * 5
    row2 = ['_'] * 5
    row3 = ['_'] * 5
    row4 = ['_'] * 5
    row5 = ['_'] * 5
    row6 = ['_'] * 5
    wordle_rows = [row1, row2, row3, row4, row5, row6]

    wordle_word = make_wordle_word()
    print_board(wordle_rows)

    for i in range(0, 6):
        wordle_rows[i] = return_colored_word(wordle_word, take_guess())
        clear_board()
        print_board(wordle_rows)

        for word in wordle_rows:
            if word == wordle_check_word(wordle_word):
            #if ''.join(word) == wordle_word:
                print('Congrats, you have solved the wordle!')
                sys.exit(0)

    if wordle_rows[5] != row6 and wordle_rows[5] != wordle_check_word(wordle_word):
        print('Sorry the correct word was: ')
        print(*wordle_check_word(wordle_word))

            #if wordle_rows[5] != wordle_check_word(wordle_word):
                #print('Sorry!')



if __name__ == '__main__':
    main()
