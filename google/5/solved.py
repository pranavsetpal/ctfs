flag= ""
# Read bytes from secret file
f = open("secret.enc", "rb")
secret = list(f.read())
f.close()

# Reverse encodeSecret() function for secret.enc
key = [predictor.getrandbits(8) for i in range(len(secret))]
for a,b in zip(key,secret):
    flag += (chr(a^b))

# Output the message
print(flag)

