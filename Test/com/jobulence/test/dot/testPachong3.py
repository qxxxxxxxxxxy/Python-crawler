'''
Created on 2018年1月3日

@author: ll
'''
import requests
import bs4
if __name__ == '__main__':
    resa = requests.get('https://pages.tmall.com/wow/act/15879/phonebazaareins?spm=875.7931836/B.2016006.d6.62bcc3492o50Zb&trackInfo=20160815100101;18109337003;134202;531459913477;3;134202_531459913477;1007.14152.68669.100200300000000;980fd196-8761-4267-8995-ca936fcdda70;2;0;10000001&item_id=531459913477&pvid=980fd196-8761-4267-8995-ca936fcdda70&pos=3&activity_id=134202&acm=07055.1003.1.2430099&scm=1003.1.20160815.OTHER_0_2754397').text
    soup = bs4.BeautifulSoup(resa,'html.parser',from_encoding='utf-8')
    links = soup.findAll('a')
    for link in links:
        print(link.name,link['href'],link.get_text())