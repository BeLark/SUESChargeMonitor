import requests
from lxml import etree
import time
import re
import os

ntime = "NOW: " + time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
print(ntime)

url = "https://epay.sues.edu.cn/epay/wxpage/wanxiao/eleresult?sysid=xxxx&roomid=xxxx&areaid=xxxx&buildid=xxxx"      #抓包获取电费页面
content = requests.get(url).content
html = etree.HTML(content)
html_xpath = html.xpath('/html/body/div[3]/div[1]/div[2]/text()')
title1 = str(html_xpath)
title1 = title1[2:-2]
title1 = re.sub(r'[\r\n\s]', '', title1)
title1 = title1[4:-4]
elec = float(title1[0:-1])
title1 = '剩余电费: ' + title1
print(title1)       #屏幕打印获取更新时间

title = title1

if elec < 15.0 :
    burl = "http://www.pushplus.plus/send?token=xxxxx&title=电费通知&content=" + title + '\n' + ntime + "&topic=xxxx"      #采用pushplus+群发消息接口
    sendb = requests.get(burl).json()
    print(sendb)
else :
    print("电费足够，不推送")