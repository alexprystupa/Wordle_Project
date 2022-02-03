from termcolor import colored

word = 'moist'
guess = 'toase'

storage_dict = dict()

list_of_word_letters = []
for word_letter in enumerate(word):
    list_of_word_letters.append(word_letter)

list_of_guess_letters = []
for guess_letter in enumerate(guess):
    list_of_guess_letters.append(guess_letter)

print(list_of_word_letters)
print(list_of_guess_letters)

#for word_tup in list_of_word_letters:
    #for guess_tup in list_of_guess_letters:
        #if word_tup == guess_tup:
            #print('Success')

for i, word_letter in word:
    for j, guess_letter in guess:
        if word_letter[i] == guess_letter[j]:
            print('Success')
