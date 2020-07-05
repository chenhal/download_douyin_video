import requests
import re
import json
url = input("请输入要下载的抖音视频地址!\n")
userAgent = "Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 XL Build/OPD1.170816.004) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Mobile Safari/537.36"
header = {
    "Referer": "https://v.douyin.com/",
    'User-Agent': userAgent,
}
#获取要下载的视频id
r = requests.get(url, headers=header)
url = r.url
id = url.split("video/")[1].split("/?")[0]
url = "https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids=" + id
r = requests.get(url, headers=header)
video = json.loads(r.content)["item_list"][0]
url = video["video"]["play_addr"]["url_list"][0]
url = url.replace("playwm", "play")
#开始下载
r = requests.get(url, headers=header)
with open(video["desc"] + ".mp4", "wb") as code:
    code.write(r.content)
    print("下载成功")
input("按下回车退出程序")