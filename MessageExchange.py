import json
import requests
import time
import ResponseAnalysis

URL = "https://api.telegram.org/bot{}/".format("787801184:AAHsCYcYAVpaJSf2PbxyVlQBBTqNkrve2Wo")


def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def echo_all(updates,trig):
    for update in updates["result"]:
        try:
            text = update["message"]["text"]
            chat = update["message"]["chat"]["id"]
            name = update["message"]["chat"]["first_name"]


            if trig == 8 :
                send_message(ResponseAnalysis.launchRA(text, name, trig), chat)
                return (4)

            if text == "END" or text == "End" or text == "end":
                send_message(ResponseAnalysis.launchRA(text, name, trig), chat)
                return (4)

            send_message(ResponseAnalysis.launchRA(text,name,trig), chat)
            return 1

        except Exception as e:
            print(e)


def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)


def get_updates(offset=None):
    url = URL + "getUpdates?timeout=100"
    if offset:
        url += "&offset={}".format(offset)
    js = get_json_from_url(url)
    return js


def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)


def send_message(text, chat_id):
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)


def launchME(trig):

    last_update_id = None

    while trig:
        updates = get_updates(last_update_id)
        if trig == 4 :
            return (0)
        if len(updates["result"]) > 0:
            last_update_id = get_last_update_id(updates) + 1
            trig = echo_all(updates,trig)
        time.sleep(0.5)