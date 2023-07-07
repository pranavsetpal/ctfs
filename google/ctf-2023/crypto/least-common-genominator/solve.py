from sage.all import ECM
from Crypto.Util.number import isPrime
config_bits = 512

dumps = [ 211286818345627549183608678726370412218029639873054513839005340650674982169404937862395980568550063504804783328450267566224937880641772833325018028629959635 ]


with open("./dump.txt", 'r') as f:
    dumps.extend([int(line[:-1]) for line in f.readlines()])

with open("./public.pem", 'r') as f:
    n = ''.join([line[:-1] for line in f.readlines()[1:-1]])
    n = int(n.encode().hex(), 16)

for i in range(len(dumps)):
    print(f"{i}: {ECM().factor(dumps[i])}")

# prime_arr = []

# for dump in dumps:
#     dump = int(dump)
#     if isPrime(dump) and dump.bit_length() == config_bits:
#         prime_arr.append(dump)
#
# print(prime_arr)
