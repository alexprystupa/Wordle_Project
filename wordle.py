#!/usr/bin/env python3
# wordle.py

from termcolor import colored
import os

def clear_board():
    os.system('clear')

wordle_word = input('Wordle of the day: ')

while len(wordle_word) != 5:
    print('Please input a 5 letter word')
    wordle_word = input('Wordle of the day: ')
    #print('Try again')

# Printing the board
row1 = ['_'] * 5
row2 = ['_'] * 5
row3 = ['_'] * 5
row4 = ['_'] * 5
row5 = ['_'] * 5
row6 = ['_'] * 5
rows = [row1, row2, row3, row4, row5, row6]

def print_board():
    for row in rows:
        print(*row)


print_board()
# Guessing the word
list_of_guess_one = []
test = input('First guess: ')
for i in test:
    list_of_guess_one.append(i)
rows[0] = list_of_guess_one

clear_board()
print_board()

def take_guess():
    list_of_guess = []
    guess = input('Take a guess: ')
    for letter in guess:
        list_of_guess.append(letter)

    return list_of_guess
