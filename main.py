# -*- coding: utf-8 -*
import requests
import json
import random
import time


def get_context():
    context_list = [
        "好羡慕",
        "马上10级",
        "感觉全是机器人",
        "水",
        "冲",
        "肝",
        "干就完了兄弟们",
        "好累",
         "gogogo",
        "\U0001F607",
        "\U0001F642",
       "\U0001F601"
        
    ]
    text = random.choice(context_list)
    return text


def chat(chanel_list,authorization_list):
    for authorization in authorization_list:
        header = {
            "Authorization": authorization,
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
        }
        for chanel_id in chanel_list:
            msg = {
                "content": get_context(),
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
            sleeptime = random.randrange(40, 50)
            time.sleep(sleeptime)
        except:
            break