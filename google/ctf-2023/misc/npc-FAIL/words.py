import re

with open("./USACONST.TXT", encoding="ISO8859") as f:
  text = f.read().lower()
raw_words = set(re.sub('[^a-z]', ' ', text.lower()).split())


from pairs import pairs

words = set(raw_words)

for word in raw_words:
  possible_word = False

  for char in pairs:
    for pair in pairs[char]:

      loc = word.find(pair)
      if loc != -1:
        continue

      if loc+2 < len(word):
        for inv_pair in pairs:
          inv_pair = inv_pair[::-1]
          if word[loc+1: loc+3] in inv_pair:
            possible_word = True
      else:
        possible_word = True

    if possible_word:
      break

  if not possible_word:
    words.remove(word)

print(len(words))
print(f"possible words: {words}")
