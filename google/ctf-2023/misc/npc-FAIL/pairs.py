characters = "andiotersvgwc"

raw_pairs = set([
('c', 'n'), ('h', 'n'), ('n', 's'), ('n', 'e'), ('e', 'd'), ('e', 'e'), ('e', 'a'), ('g', 'e'), ('e', 'v'), ('e', 'a'), ('i', 'e'), ('e', 'a'), ('e', 's'), ('g', 'e'), ('r', 'c'), ('s', 's'), ('a', 'n'), ('t', 'a'), ('g', 't'), ('s', 'r'), ('d', 's'), ('a', 'i'), ('r', 'a'), ('g', 'w'), ('s', 'v'), ('r', 's'), ('t', 'a'), ('r', 'e'), ('r', 'n'), ('s', 't'), ('n', 'o'), ('n', 'e'), ('w', 'd'), ('t', 'i'), ('s', 'i'), ('e', 'i'), ('s', 'v'), ('t', 'c'), ('s', 't'), ('e', 'r'), ('h', 'w'), ('g', 'r'), ('i', 's'), ('v', 'i'), ('r', 'e'), ('c', 'n'), ('o', 'h'), ('n', 'g'), ('d', 'o'), ('n', 'a'), ('s', 'v'), ('r', 'i'), ('w', 'g'), ('a', 'a'), ('e', 'a'), ('r', 'a'), ('e', 'g'), ('d', 'n'), ('n', 's'), ('g', 'n'), ('h', 'c'), ('d', 'r'), ('s', 'h'), ('w', 'c'), ('r', 's'), ('v', 'd'), ('g', 'v'), ('e', 's'), ('a', 's'), ('o', 'c'), ('e', 'e'), ('a', 'w'), ('a', 'w'), ('g', 'n'), ('r', 'n'), ('i', 'r'), ('n', 'i'), ('e', 's'), ('n', 't'), ('d', 'c'), ('a', 'd'), ('i', 'v'), ('w', 'n'), ('h', 'n'), ('g', 'i'), ('a', 'd'), ('i', 'g'), ('n', 'a'), ('t', 'c'), ('t', 'd'), ('t', 'e'), ('e', 's'), ('a', 't'), ('n', 'e'), ('e', 't'), ('a', 'h'), ('d', 'o'), ('s', 'o'), ('s', 'd'), ('t', 's'), ('h', 'n'), ('d', 'a')
])


pairs = {char: set() for char in characters}

for char in characters:
    for pair in raw_pairs:
        if char in pair:
            pair = list(pair)
            pair.remove(char)
            pairs[char].add(pair[0]+char)

# print(pairs)
