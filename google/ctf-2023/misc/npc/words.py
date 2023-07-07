import re

with open('USACONST.TXT', 'r', encoding='ISO8859') as f:
  text = f.read()
raw_word_list = list(re.sub('[^a-z]', ' ', text.lower()).split())

unique_word_list = []
[unique_word_list.append(word) for word in raw_word_list if word not in unique_word_list]


from pairs import pairs

possible_word_list = []
for word in unique_word_list:
  if len(word) == 1:
    possible_word_list.append(word)
    continue

  if len(word) == 2:
    if word in pairs:
      possible_word_list.append(word)
      continue

  possible_word = True
  for c1,c2 in zip(word, word[1:]):
    if (c1+c2) not in pairs:
      possible_word = False
      break
  if possible_word:
    possible_word_list.append(word)

word_list = []
for w1 in possible_word_list:
  start_pair = False
  for w2 in possible_word_list:
    if (w1[0]+w2[-1]) in pairs:
      start_pair = True
      break

  end_pair = False
  for w2 in possible_word_list:
    if (w1[-1]+w2[0]) in pairs:
      end_pair = True
      break

  if start_pair and end_pair:
    word_list.append(w1)


char_count = {}
chars = list("aandioterdennrastvggseiwnsch")
for char in chars:
  char_count[char] = chars.count(char)

for word in word_list:
  if char in word:
    if word.count(char) > char_count[char]:
      word_list.remove(word)
print(len(word_list))


print(word_list)
