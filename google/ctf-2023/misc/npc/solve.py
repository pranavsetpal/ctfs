from itertools import combinations
from words import word_list

chars = list("aandioterdennrastvggseiwnsch")
password_char_count = {char: chars.count(char) for char in chars}

def req_words(words, fn):
  words = list(words) # Working with copy

  length = 0
  len_words = [len(word) for word in words]

  n_words = 0
  while length < 28:
    length += len_words.pop(fn(len_words))
    n_words += 1
  n_words -= 1

  return n_words

min_req_words = req_words(word_list, max)
max_req_words = req_words(word_list, min)

print(min_req_words)
print(max_req_words)

# possible_combinations = []
combs = 0

for i in range(min_req_words, max_req_words+1):
  for words in combinations(word_list, i):
    combination = ''.join(words)
    if len(combination) == 28:
      word_char_count = {char: chars.count(char) for char in combination}
      if password_char_count == word_char_count:
        # possible_combinations.append(words)
        combs += 1
    print(combs)

print("Possible Combs:", combs)

# with open("combinations.txt", 'w') as f:
#   f.write(str(possible_combinations))
