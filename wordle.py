#!/usr/bin/env python3
# wordle.py
import sys

from termcolor import colored
import os

def clear_board():
    os.system('clear')

def make_wordle_word():
    wordle_word = input('Wordle of the day: ')
    while len(wordle_word) != 5:
        print('Please input a 5 letter word')
        wordle_word = input('Wordle of the day: ')

    return wordle_word

def print_board(rows):
    for row in rows:
        print(*row)

def take_guess():
    list_of_guess = []
    guess = input('Take a guess: ')
    for letter in guess:
        list_of_guess.append(letter)

    return list_of_guess

def main():

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

    for i in range(0,6):
        wordle_rows[i] = take_guess()
        clear_board()
        print_board(wordle_rows)

        for word in wordle_rows:
            if ''.join(word) == wordle_word:
                print('Congrats, you have solved the wordle!')
                sys.exit(0)



if __name__ == '__main__':
    main()











