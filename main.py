import os
import random
import string
from time import sleep
import requests
import threading


COLORS = {
    "red": "\u001b[31m",
    "cyan": "\u001b[36m",
    "white": "\u001b[37m",
    "magenta": "\u001b[35m",
    "yellow": "\u001b[33m"
}

def ProxyFile():


    proxylist = open('proxies.txt', 'r').read().split('\n')

    randomip = proxylist[random.randint(0, len(proxylist)-1)]

    return {'https': randomip}


def GetUser():
    os.system('cls')
    ASCII()
    user = input(ColorText("[[yellow]]Type the Curious Cat user: "))

    print(ColorText("[[magenta]]User successfully set!"))
    sleep(1)
    os.system('cls')
    return user

def GetMessage():
    os.system('cls')
    ASCII()
    message = input(ColorText('[[yellow]]Type the message that you want to send: '))

    print(ColorText("[[magenta]]Message successfully set!"))
    sleep(1)
    os.system('cls')
    return message


def RandomString():
    random_string = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])
    return random_string


def SendQuestions(ccUser, message, proxy):
    url = 'https://curiouscat.qa/api/v2/post/create'


    while True:
        try:
            requests.post(url, proxies=proxy, allow_redirects=False, data={
                    "to": ccUser,
                     "anon": "true",
                    "question": message
            }, timeout=5)

            print(ColorText('[[yellow]]Message sent:'), message)
        except:
            continue

def ColorText(text):
    for color in COLORS:
        text = text.replace("[[" + color + "]]", COLORS[color])
    return text


def ASCII():
    os.system('cls')

    logo = open('curious_cat_logo.txt', 'r')
    ascii = "".join(logo.readlines())
    print(ColorText(ascii))


ccUser = GetUser()
message = GetMessage()

while 1:
    try:
        proxy = ProxyFile()
        threading.Thread(target=SendQuestions, args=(ccUser, message, proxy)).start()

    except:
        continue



