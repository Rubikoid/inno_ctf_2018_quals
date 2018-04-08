# TCP-реверсер


**Category:** ppc, tcp, words
**Points:** 100
**Description:**

> Привет! Вот задание на сегодня - написать программу, способную "переворачивать" слова, полученные от нашего сервера. Например, мы прислали "olleh", в ответ нужно прислать "hello". Это несложно. Всего 100 итераций и флаг твой!
> nc tcp.innoctf.hackforces.com 5090
> P.S. время на ответ ограничено - всего 3 секунды!

## WriteUp 

Дается сервис, который просит развернуть строку и отправить её обратно. 100 успешных посылок - флаг.

Важно аккуратно обработать символы `\r`, `\n`, и фразы `Good job!` и `progress!`

Собственно, скрипт:

```python
import socket
import time
import datetime

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('tcp.innoctf.hackforces.com',5090))
while True:
#if True==True:
    data = s.recv(1024).decode('utf-8')
    data = data.replace('\r', '').replace('\n','').replace('Good job!', '').replace('progress!','')
    print(data)

    print(data[::-1])
    #e = input(':')
    s.send(bytes(data[::-1]+"\n", 'UTF-8'))

    time.sleep(0.25)
s.close()
```