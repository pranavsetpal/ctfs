from hashlib import md5

hashes = [
 'd.0.....f5...5.6.7.1.30.6c.d9..0',
 '1b.8.1.c........09.30.....64aa9.',
 'c.d.1.53..66.4.43bd.......59...8',
 '.d.d.076........eae.3.6.85.a2...'
]
guesses = ['']*len(hashes)

vals = [chr(i) for i in range(ord('a'), ord('z')+1)]

for i in vals:
    for j in vals:
        for k in vals:
            for l in vals:
                for m in vals:
                    guess = (i+j+k+l+m)
                    hashed = md5(guess.encode()).hexdigest()

                    for n in range(len(hashes)):
                        for o in range(len(hashes[n])):
                            if hashes[n][o] != '.' and hashes[n][o] != hashed[o]:
                                break
                        else:
                            guesses[n] = guess

print(guesses)
