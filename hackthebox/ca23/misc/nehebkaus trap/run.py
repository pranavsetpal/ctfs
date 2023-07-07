cmd = f"print(__import__('subprocess').check_output({__import__('sys').argv[1:]}))"

def obfuscate(s):
    chars = [f"chr({ord(char)})" for char in s]
    s = '+'.join(chars)
    return s

print(obfuscate(cmd))

