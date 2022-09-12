# -*- coding: utf-8 -*
import requests
import json
import random
import time



def get_api():
    response_api = requests.get("https://api.vvhan.com/api/joke")
    msg = response_api.text
    return msg





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
    chanel_list = ["902180067130630174"]
    authorization_list = ["ODYwNDkwMTc3NTk5MjQyMjYw.G5fE2D.i6VluWny2Ks3pdWNqDwZ4FQdfhCUhtYE_GURoA"]
    while True:
        try:
            chat(chanel_list,authorization_list)
            sleeptime = random.randrange(59, 60)
            time.sleep(sleeptime)
        except:
            break