from sys import argv

chars = [f"chr({ord(char)})" for char in argv[1]]
s = '+'.join(chars)
print(s)
