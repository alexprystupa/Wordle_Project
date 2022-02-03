from termcolor import colored

#word = 'fail'
#guess = 'fale'

'''
if index and letter match append to correct list.
else if index does not match but the letter appears in the word append to incorrect list
else append to not in word list
'''

#correct_letter = []
#incorrect_letter = []
#not_in_word = []
#for i, letter in enumerate(guess):
    #if guess[i] == word[i]:
        #correct_letter.append(letter)
    #elif letter in word:
        #incorrect_letter.append(letter)
    #else:
        #not_in_word.append(letter)

#print(f'Correct Letter: {correct_letter}')
#print(f'Incorrect Letter: {incorrect_letter}')
#print(f'Not in word: {not_in_word}')

# THIS VERSION FINALLY WORKS!
#colored_guess = []
#for i, letter in enumerate(guess):
    #if letter in correct_letter and guess[i] == word[i]:
        #colored_guess.append(colored(letter, 'green'))
    #elif letter in incorrect_letter and letter in correct_letter:
        #colored_guess.append(colored(letter, 'red'))
    #elif letter in incorrect_letter:
        #colored_guess.append(colored(letter, 'yellow'))
    #else:
       # colored_guess.append(colored(letter, 'red'))

#print(*colored_guess)

def return_colored_word(word, guess):
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

    print(*colored_guess)

if __name__ == '__main__':
    return_colored_word('knoll', 'knoll')