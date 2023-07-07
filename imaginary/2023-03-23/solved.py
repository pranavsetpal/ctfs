from hashlib import sha512

passhash = "b411eb3d2d71ee1a70c92bbb5fdcb2460949c9739e518f8b0b4d2e73a00a9795054c955669137f2e17ea4800ee20efed38e94a8ba19f05c1af19e044f26952e7"

salt = b'very_secure_salt'

for n in range(10**8):
    password = f"{n:07}" # fill 0s
    if sha512(salt + password.encode()).hexdigest() == passhash:
        print(f"Here it is! Password={password}")
        break
else:
    print("No password D:")
