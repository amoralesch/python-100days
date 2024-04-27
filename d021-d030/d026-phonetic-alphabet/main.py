# NATO Phonetic Alphabet

# Take a string, and produce an array of words denoting the NATO
# phonetic alphabet.
#
# Learn about list (and dict) comprehension.

import pandas

DATA = pandas.read_csv('nato_phonetic_alphabet.csv')

alphabet = {row.letter:row.code for (index, row) in DATA.iterrows()}
word = input('Enter a word: ').upper()
codes = [alphabet[letter] for letter in word]
print(codes)
