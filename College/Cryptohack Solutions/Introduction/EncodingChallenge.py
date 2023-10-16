from pwn import * # pip install pwntools
import json
from Crypto.Util.number import long_to_bytes
import codecs

r = remote('socket.cryptohack.org', 13377, level = 'debug')
for counter in range(100):
    answer = ""

    def json_recv():
        line = r.recvline()
        return json.loads(line.decode())

    def json_send(hsh):
        request = json.dumps(hsh).encode()
        r.sendline(request)


    received = json_recv()

    print("Received type: ")
    print(received["type"])
    print("Received encoded value: ")
    print(received["encoded"])

    if received["type"] == "hex" or received["type"] == "bigint":
        answer=str(long_to_bytes(int(received["encoded"], 16)))[2:-1]
    elif received["type"] == "base64":
        answer=base64.b64decode(received["encoded"].encode()).decode()
    elif received["type"] == "rot13":
        answer=codecs.encode(received["encoded"], 'rot_13')
    elif received["type"] == "utf-8":
        for c in received["encoded"]:
            answer += chr(c)

    print(answer)
    to_send = {
        "decoded": answer, "changeme": 12
    }
    json_send(to_send)

print(json_recv())