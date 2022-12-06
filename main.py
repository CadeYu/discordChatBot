# -*- coding: utf-8 -*
import requests
import json
import random
import time
import textwrap


def get_api():
    last_timestamp = None
   
    # 调用 API 获取新闻数据
    response_api_news = requests.get(
    "https://newsdata.io/api/1/news?apikey=YOU_API_KEY&q=defi",
    verify=False,
)
    msg_news = response_api_news.text
    
    # 解析新闻数据
    news_data = None
    parse_json = json.loads(msg_news)
    if "results" in parse_json and parse_json["results"]:
        # 检查 "results" 字段是否包含有效数据
        news_data = {
            "title": parse_json["results"][0]["title"],
            "content": parse_json["results"][0]["content"],
            "pubDate": parse_json["results"][0]["pubDate"],
        }
        # 检查新闻内容是否为新的
        if last_timestamp is None or news_data["pubDate"] > last_timestamp:
            # 更新最后一次获取新闻的时间戳
            last_timestamp = news_data["pubDate"]
            # 返回新闻数据
            return news_data
    # 如果获取到的新闻数据不是新的，则返回 None
    return None



def chat(chanel_list, authorization_list, news_data):
    for authorization in authorization_list:
        header = {
            "Authorization": authorization,
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
        }
        for chanel_id in chanel_list:
            if news_data is not None:
                # 截取json字段
                lines = textwrap.wrap(news_data["content"], width=400)

                for line in lines:
                    msg = {
                        "title": news_data["title"],
                        "content": line,
                    }
                    msg_json = json.dumps(msg)
                    url ="https://discord.com/api/v9/channels/{}/messages".format(chanel_id)
                    try:
                        res = requests.post(url=url, headers=header, data=msg_json)
                        print(res.content)
                    except:
                        pass
                    continue
                time.sleep(random.randrange(3600,3600*4))


if __name__ == "__main__":
    # Discord 频道列表和授权列表
    chanel_list = ["channel_id"]
    authorization_list = ["authorization_list"]

    while True:
        # 获取新闻数据
        news_data = get_api()

        # 如果新闻数据不为空，则将新闻发送到 Discord 频道
        if news_data is not None:
            chat(chanel_list, authorization_list, news_data)

        # 每隔一小时获取一次新闻数据
        time.sleep(3600)