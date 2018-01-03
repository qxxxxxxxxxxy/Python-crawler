'''
Created on 2018年1月3日

@author: ll
'''
import re
import requests

if __name__ == '__main__':
    i = 0
    list = []
    resa = requests.get('https://pages.tmall.com/wow/act/15879/phonebazaareins?spm=875.7931836/B.2016006.d6.62bcc3492o50Zb&trackInfo=20160815100101;18109337003;134202;531459913477;3;134202_531459913477;1007.14152.68669.100200300000000;980fd196-8761-4267-8995-ca936fcdda70;2;0;10000001&item_id=531459913477&pvid=980fd196-8761-4267-8995-ca936fcdda70&pos=3&activity_id=134202&acm=07055.1003.1.2430099&scm=1003.1.20160815.OTHER_0_2754397').text
    urllist = re.findall(r'//img.+\.jpg', resa)
    for img in urllist:
        a = 'http:' + img
        list.append(a)
        print(a)
    for url in list:
        f = open(str(i) + '.jpg', 'wb')
        req = requests.get(url).content
        f.write(req)
        f.close()
        i += 1
