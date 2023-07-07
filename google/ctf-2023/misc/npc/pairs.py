chars = set("aandioterdennrastvggseiwnsch")

raw_pairs = set(["ne", "nc", "ss", "an", "ne", "ta", "gt", "sn", "ds", "ai", "ra", "gw", "sv", "rs", "ta", "ne", "nn", "st", "no", "ne", "wd", "ti", "si", "ei", "sv", "tc", "st", "ns", "en", "hw", "gn", "is", "vi", "ne", "cn", "oh", "ng", "ed", "do", "ee", "na", "sv", "ni", "wg", "aa", "ea", "ra", "eg", "dn", "ns", "ea", "gn", "hc", "dr", "sh", "wc", "ns", "vd", "ge", "gv", "es", "as", "oc", "ee", "aw", "aw", "gn", "rn", "ir", "ni", "es", "nt", "ev", "dc", "ad", "iv", "wn", "hn", "gi", "ea", "ad", "ig", "na", "ie", "ea", "tc", "td", "te", "es", "at", "ne", "et", "ah", "do", "so", "sd", "hn", "es", "ts", "hn", "da", "cn", "ge"])

pairs = set(raw_pairs)

for pair in raw_pairs:
  pairs.add(pair[::-1])

# print(len(pairs)) -- 108




# unique_pairs = set()
#
# for pair in raw_pairs:
#   if pair[::-1] not in unique_pairs:
#     unique_pairs.add(pair)

# print(len(unique_pairs)) -- 56

# pairs = {}
# for char in chars:
#   pairs[char] = []
#
#   for pair in unique_pairs:
#     if char in pair:
#       pair = list(pair)
#       pair.remove(char)
#       pairs[char].append(pair[0]+char)

# print(pairs)
