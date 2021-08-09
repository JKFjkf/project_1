import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OSX10_14_2) AppleWebKit/537.36(KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
LocaTion = input('请输入所在地区：')
url = 'https://geoapi.qweather.com/v2/city/lookup?location='+LocaTion+'&key=1b43ddd0d74240d1ad61e29e34ad1aeb&range=cn'
res = requests.get(url,headers=headers,timeout=5)
res = res.text
id = res[46:55]
print(res)
print(id)
url_1 = 'https://devapi.qweather.com/v7/weather/now?location='+id+'&key=1b43ddd0d74240d1ad61e29e34ad1aeb&range=cn'
res_1 = requests.get(url_1,headers=headers,timeout=5)
res_1 = res_1.text
Temp = res_1[135:136]
FeelsLike = res_1[150:151]
print()

