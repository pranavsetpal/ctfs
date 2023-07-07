import hashlib
import re

guess = 'input'

hashes = [
 'd.0.....f5...5.6.7.1.30.6c.d9..0',
 '1b.8.1.c........09.30.....64aa9.',
 'c.d.1.53..66.4.43bd.......59...8',
 '.d.d.076........eae.3.6.85.a2...']

guesses = []
for i in range(len(hashes)):
    guess = input()

    if re.match('^[a-z]+$', guess):
        re.match('^' + hashes[i].replace('.', '[0-9a-f]') + '$', hashlib.md5(guess.encode()).hexdigest())
        guesses.append(guess)

print('Flag: ', guesses, '{',''.join(guesses), '}')
