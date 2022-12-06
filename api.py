
import requests
import json
import random
import time



def get_api():
    # response_api_joke = requests.get("https://api.vvhan.com/api/joke")
    response_api_poem = requests.get("https://v1.jinrishici.com/all")
    # msg_joke = response_api_joke.text
    msg_pome = response_api_poem.text
    parse_json = json.loads(msg_pome)
    final_data_poem = parse_json["content"]
    print(final_data_poem)



if __name__ == "__main__":
    while True:
        try:
            get_api()
            sleeptime = random.randrange(2, 3)
            time.sleep(sleeptime)
        except:
            break