# from stegano import lsb
import requests

# clear_message = lsb.reveal("./potty.png")
# print(clear_message)

r = requests.get('https://potty-training.c.ctf-snyk.io/')
# print(r.text)
