import re

import requests
from bs4 import BeautifulSoup
import urllib.request as DFU
import os


url = input('Enter URl: ')
data = requests.get(url)
string = data.text
print(string)


match = re.findall(r'video_url\W\W\W([-\W\w]+)\W\W\Wvideo_view_count', string)
print(match)

extraction = ".mp4"

if len(match) == 0:
    match = re.findall(r'display_url\W\W\W([-\W\w]+)\W\W\Wdisplay_resources', string)
    print(match)
    extraction = ".jpg"

res = match[0]
print(res)

page = BeautifulSoup(string, "html.parser")
title = page.find("title")
title = title.get_text()

title = re.sub(r"\W+", "_", title)
title = "download" + title
print("\n" + title)

if res != "":
    try:
        file_name = title
        DFU.urlretrieve(res, file_name+extraction)
        os.system("tree download")

    except Exception as e:
        print(e)
else:
    print("404 Not Found")
