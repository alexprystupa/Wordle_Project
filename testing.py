#!/usr/bin/env python3
# testing.py
from termcolor import colored

word = 'fail'
guess = 'fall'

list_of_word = []
for letter in word:
    list_of_word.append(letter)

list_of_guess = []
for letter in guess:
    list_of_guess.append(letter)

print(list_of_word)
print(list_of_guess)

correct_placement = []
incorrect_placement = []

for i, letter in enumerate(list_of_word):
    if list_of_word[i] == list_of_guess[i]:
        correct_placement.append(letter)

    elif letter in list_of_guess:
        incorrect_placement.append(letter)

    else:
        pass

#print(correct_placement, incorrect_placement)
#print(colored_letters)

colored_guess = []
for letter in guess:
    if letter in correct_placement:
        colored_guess.append(colored(letter, 'green'))
    elif letter in incorrect_placement:
        colored_guess.append(colored(letter, 'yellow'))
    else:
        colored_guess.append(letter)

#print(*colored_guess)
print(correct_placement)
print(incorrect_placement)

