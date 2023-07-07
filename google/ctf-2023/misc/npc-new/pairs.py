chars = {
  1051081353: 'a',
  66849241: 'a',
  53342583: 'n',
  213493562: 'd',
  4385267: 'i',
  261138725: 'o',
  51574206: 't',
  565468867: 'e',
  647082638: 'r',
  177014844: 'd',
  894978618: 'e',
  948544779: 'n',
  572570465: 'n',
  582531406: 'r',
  264939475: 'a',
  415170621: 's',
  532012257: 't',
  151901859: 'v',
  346347468: 'g',
  148496047: 'g',
  125615053: 's',
  723039811: 'e',
  962878065: 'i',
  112993293: 'w',
  748275487: 'n',
  120330115: 's',
  76544105: 'c',
  186790608: 'h'
}


pairs = [(53342583, 565468867),(582531406, 76544105),(125615053, 120330115),(264939475, 572570465),(53342583, 565468867),(532012257, 264939475),(346347468, 532012257),(125615053, 582531406),(177014844, 120330115),(264939475, 962878065),(647082638, 1051081353),(346347468, 112993293),(120330115, 151901859),(647082638, 125615053),(532012257, 66849241),(582531406, 894978618),(582531406, 572570465),(125615053, 532012257),(948544779, 261138725),(748275487, 894978618),(112993293, 177014844),(532012257, 4385267),(415170621, 962878065),(723039811, 962878065),(120330115, 151901859),(51574206, 76544105),(415170621, 532012257),(53342583, 120330115),(723039811, 582531406),(186790608, 112993293),(148496047, 582531406),(4385267, 125615053),(151901859, 962878065),(582531406, 894978618),(76544105, 748275487),(261138725, 186790608),(948544779, 346347468),(565468867, 213493562),(213493562, 261138725),(565468867, 894978618),(572570465, 264939475),(415170621, 151901859),(582531406, 962878065),(112993293, 346347468),(66849241, 1051081353),(894978618, 264939475),(647082638, 66849241),(894978618, 148496047),(213493562, 748275487),(572570465, 120330115),(565468867, 264939475),(148496047, 948544779),(186790608, 76544105),(177014844, 647082638),(125615053, 186790608),(112993293, 76544105),(582531406, 415170621),(151901859, 177014844),(346347468, 565468867),(148496047, 151901859),(723039811, 415170621),(1051081353, 415170621),(261138725, 76544105),(894978618, 723039811),(66849241, 112993293),(264939475, 112993293),(346347468, 748275487),(647082638, 948544779),(962878065, 647082638),(948544779, 962878065),(723039811, 120330115),(572570465, 51574206),(565468867, 151901859),(213493562, 76544105),(1051081353, 213493562),(962878065, 151901859),(112993293, 948544779),(186790608, 948544779),(346347468, 4385267),(565468867, 66849241),(1051081353, 177014844),(962878065, 148496047),(748275487, 264939475),(4385267, 565468867),(565468867, 1051081353),(51574206, 76544105),(532012257, 213493562),(532012257, 894978618),(723039811, 415170621),(264939475, 51574206),(572570465, 723039811),(894978618, 532012257),(66849241, 186790608),(213493562, 261138725),(415170621, 261138725),(125615053, 177014844),(186790608, 53342583),(565468867, 120330115),(51574206, 120330115),(186790608, 748275487),(213493562, 1051081353),(76544105, 53342583),(148496047, 565468867)]

pairs.append([pair[::-1] for pair in pairs])

def find_paths(char, pairs, depth, max_depth):
  if depth == max_depth: return [-1]

  next_chars = [pair[1] for pair in pairs if pair[0] == char] 
  pairs = [pair for pair in pairs if char not in pair]

  child_paths = []
  for next_char in next_chars:
    child_paths.extend(find_paths(next_char, pairs, depth+1, max_depth))
  if len(next_chars) == 0: child_paths.append([])

  paths = [[char, *path] for path in child_paths]
  return paths


# char = 1
# pairs = [(1,3), (2,3), (5,1), (4,5), (4,2)]
# pairs.extend([pair[::-1] for pair in pairs])

char = list(chars.keys())[0]
pairs = pairs
print(find_paths(char, pairs, 0, 28))

# char = 5
# paths = [[1,2,4,3], [3,2,4,1]]
# paths = [[char, *path] for path in paths]
# print(paths)











# char_paths = []
#
# def follow_path(char, chars, pairs):
#   print(char, chars, pairs)
#   path = {}
#   possible_paths = [pair[1] for pair in pairs if char in pair]
#
#   if len(possible_paths) != 0:
#     pairs = [pair for pair in pairs if pair not in possible_paths]
#     chars.remove(char)
#     for char in chars:
#       path[char] = follow_path(char, chars, pairs)
#       return path
#
#   return {}
#
#
# char = 1
# chars = [1,2,3,4,5]
#
# print(chars.index(char))
#
# pairs = [(1,2), (3,2), (4,2), (5,1), (1,4)]
#
# print(follow_path(char, chars, pairs))



# follow_path(char, pairs, pairs_inv):
#   possible_paths = [pair[1] for pair in pairs if char == pair[0]]
#   possible_paths_inv = [pair[1] for pair in pairs_inv if char == pair[0]]
#   if len(possible_paths) != 0 and len(possible_paths_inv) != 0:
#     pairs = [pair for pair in pairs if pair not in possible_paths]
#     pairs_inv = [pair for pair in pairs_inv if pair not in possible_paths]
#     for path in possible_paths:
#       follow_path(path, pairs, pairs_inv)
#     for path in possible_paths_inv:
#       follow_path(path, pairs, pairs_inv)
#   for pair in pairs:
#     if char in pair:
#       recurse = True
#
# create_char_paths(chars, pairs, pairs_inv):
#   pairs, pairs_inv = list(pairs), list(pairs_inv)
#   
#   paths = {}
#   for char in chars:
#     paths[char] = {}
#
#     for pair in pairs:
#       if pair[0] == char:
#         paths[char][pair[1]] = {}
#
#
#     paths.extend([[pair] for pair in pairs if pair[0] == char])
#     paths.extend([[pair] for pair in pairs_inv if pair[0] == char])
#
#     for i in range(len(paths)):
#       pair.remove(path[i][-1])
