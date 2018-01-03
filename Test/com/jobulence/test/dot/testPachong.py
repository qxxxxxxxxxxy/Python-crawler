'''
Created on 2017年12月28日

@author: ll
'''
import requests
import re
url = 'http://www.xiaohuar.com/hua/'
response = requests.get(url)
html = response.text
img_urls=re.findall(r'/d/file/\d+/\w+\.jpg',html)

for img_url in img_urls:
    img_response = requests.get('http://www.xiaohuar.com%s' % img_url)
    img_data = img_response.content
    beauty = img_url.split('/')[-1]
    with open(beauty,'wb')as f:
        f.write(img_data)
