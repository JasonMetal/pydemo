
from urllib import request

from bs4 import BeautifulSoup
def get_html(url,num_retries = 2):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
    items = []
    for page in range(1, 2489):
        try:
            response = request.Request(url=url%page, headers=headers)
            html = request.urlopen(response).read().decode('utf-8')
            soup = BeautifulSoup(html, 'html.parser')
            trs = soup.find_all('tr')
            for i in range(1, len(trs)):
                try:
                    tds = trs[i].find_all("td")
                    tds0,tds6,tds7 = '','',''
                    if len(tds) == 10:
                        if tds[0].img: tds0 = tds[0].img["alt"]
                        if tds[6].div:tds6 = tds[6].div["title"]
                        if tds[7].div:tds7 = tds[7].div["title"]
                        item = (tds0,tds[1].get_text(),tds[2].get_text(),
                                 tds[3].get_text().strip(),tds[4].get_text(),
                                 tds[5].get_text(),tds6,tds7,tds[8].get_text(),
                                 tds[9].get_text())
                        items.append(item)
                except TypeError as e:
                    print('get_html_td TypeError:' + e.__str__())
                    continue
            print(url % page)
        except request.URLError as e:
            print('get_html Error:'+e.reason)
            html = None
            if num_retries>0:
                if hasattr(e,'code') and 500<=e.code<600:
                    # recursively retry 5xx HTTP errors
                    return get_html(url,num_retries-1)
        if page%50==0 or page==2488:
            print(item)





if __name__=='__main__':
    url = 'http://www.xicidaili.com/nn/%s'
    get_html(url)
