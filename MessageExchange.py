import json;
import requests;
import time
import ResponseAnalysis

URL = "https://api.telegram.org/bot{}/".format("787801184:AAHsCYcYAVpaJSf2PbxyVlQBBTqNkrve2Wo")


def get_url(url):
    return requests.get(url).content.decode("utf8")


def get_json_from_url(url):
    return json.loads(get_url(url))


def get_updates():
    return get_json_from_url(URL + "getUpdates")


def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)


def send_message(text, chat_id):
    get_url(URL + "sendMessage?text={}&chat_id={}".format(text, chat_id))

def launchME(trig):

    last_textchat = (None, None)
    while True:
        text, chat = get_last_chat_id_and_text(get_updates())
        if (text, chat) != last_textchat:
            send_message(ResponseAnalysis.launchRA(text), chat)
            last_textchat = (text, chat)
            time.sleep(0.1)
        if text == "End" or text == "end":
                return (1)
