# -*- coding: utf-8 -*
from ast import If
import requests
import json
import random
import time



def get_api():
    response_api_joke = requests.get("https://api.vvhan.com/api/joke")
    msg_joke = response_api_joke.text
    response_api_poem = requests.get("https://v1.jinrishici.com/all")
    msg_pome = response_api_poem.text
    parse_json = json.loads(msg_pome)
    final_data_poem = parse_json["content"]
    msg = ""

    flag = random.randint(0,1);
    if flag == 0:
        msg = final_data_poem
    else :
        msg = msg_joke


    return msg

def random_context():
    random_list = [
        "大家好啊",
        "这个项目好像融资了不少",
        "lfg",
        "想要升级",
        "马上升级"
    ]




def chat(chanel_list,authorization_list):
    for authorization in authorization_list:
        header = {
            "Authorization": authorization,
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
        }
        for chanel_id in chanel_list:
            msg = {
                "content": get_api(),
                "nonce": "82329451214{}33232234".format(random.randrange(0, 1000)),
                "tts": False,
            }
            url = "https://discord.com/api/v9/channels/{}/messages".format(chanel_id)
            try:
                res = requests.post(url=url, headers=header, data=json.dumps(msg))
                print(res.content)
            except:
                pass
            continue
        time.sleep(random.randrange(1, 3))



if __name__ == "__main__":
    chanel_list = ["channel_id"]
    authorization_list = ["user_Owen_Authorization"]
    while True:
        try:
            chat(chanel_list,authorization_list)
            sleeptime = random.randrange(59, 60)
            time.sleep(sleeptime)
        except:
            break