from Crypto.Util.number import *

data = [14169084828739113416, 12950362233651727953, 13081576751296291893, 11189892724250189745, 2366046383900978737, 1749792629103627315, 8575562236709928474]
p = 16200480981168924301 # 0xe0d3ab9e590ba68d

# FLAG = cvctf{ | ...... | ...... | .....}  <-- len=24
FLAG = b'cvctf{' +b'.'*17 + b'}'

u,v,w = getRandomInteger(128), getRandomInteger(256), getRandomInteger(512)

a = bytes_to_long(FLAG[:6]) # 109360125863547
print(hex(a))
