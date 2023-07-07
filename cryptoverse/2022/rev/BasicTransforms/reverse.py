from base64 import b64decode

cat = b64decode("QUlgNGoxT2A2empxMQ==").decode()[::-1]
cat = ''.join([chr(ord(c)-1) for c in cat])
print(cat)
