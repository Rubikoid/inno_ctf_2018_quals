import requests
from nclib import Netcat
import json
langs={
    "spanish":"es",
    "german":"de",
    "french":"fr",
    "italian":"it",
    "russian":"ru"
}
URL = r"https://translate.yandex.net/api/v1.5/tr.json/translate?key=<YOUR KEY>&text={text}&lang={lang}&format=plain"
nc = Netcat(("tcp.innoctf.hackforces.com",5061))
while True:
    while True:
        s = nc.recv_line().decode().split()
        print("< ",s)
        if(s[0] == 'Translate'):
            break
    lang, word = s[2], s[-1][1:-1]
    lang =  langs[lang]
    url = URL.format(text=word,lang=lang)
    resp = json.loads(requests.get(url).text)
    print("> ", resp['text'][0])
    nc.send_line(resp['text'][0].encode())
