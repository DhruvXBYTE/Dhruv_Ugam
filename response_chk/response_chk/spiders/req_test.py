import requests



re=requests.get('https://search.rakuten.co.jp/search/mall/skin+care/')

print(re.status_code)

with open('Rakuten.html','w',encoding='utf-8')as f:
    f.write(re.text)