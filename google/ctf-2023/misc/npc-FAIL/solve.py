from itertools import combinations

from words import words

i = 0
for pass_words in combinations(words, 4):
  i+=1
  # print(pass_words)
  # break

print(i)
