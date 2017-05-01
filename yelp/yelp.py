# coding:utf8

__author__ = 'taojing'

# coding:utf8
# https://gist.github.com/evandrix/3694955


# from PyQt4.QtCore import *
from ghost import Ghost
import time
import urllib2
import httplib
import random

ghost = Ghost()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate,br',
    'Connection': 'Keep-Alive',
    'Host': 'www.yelp.com',
    'upgrade-insecure-requests': '1',

}

# with ghost.start() as session:
# page, extra_resources = session.open("https://www.yelp.com/search?cflt=restaurants&find_loc=San+Francisco%2C+CA",
# headers=headers)
#
# assert page.http_status == 200
# print type(page.content)
# print unicode(page.content)

def f_https_download(url):
    try:
        conn = httplib.HTTPSConnection("www.yelp.com")
        conn.request("GET", url)
        response = conn.getresponse()
        print response.status, response.reason
        data = response.read()
        return data
    except Exception, e:
        conn = httplib.HTTPSConnection("www.yelp.com")
        conn.request("GET", url)
        response = conn.getresponse()
        print response.status, response.reason
        data = response.read()
        return data


class YelpLinkPage:
    def __init__(self):
        pass

    def city_main(self):
        url = '/search?cflt=restaurants&find_loc=San+Francisco%2C+CA'
        f_link_page_analyser(f_https_download(url))

        for link_page_url in f_list_url():
            try:
                time.sleep(random.randint(10, 30))
                f_link_page_analyser(f_https_download(link_page_url))
            except Exception, e:
                print link_page_url, repr(e)


def f_list_url():
    url = '/search?cflt=restaurants&find_loc=San+Francisco%2C+CA'
    list_url = []
    for i in range(1, 100):
        list_url.append(url + "&start=" + str(i * 10))

    return list_url


def f_link_page_analyser(page_content):
    link_html = page_content.split("<span class=\"indexed-biz-name\">")
    for link_area in link_html[1:]:
        link_area = link_area[link_area.find('href="')+6:]
        print link_area[0:link_area.find('"')]


if __name__ == '__main__':
    sta = time.time()
    a = YelpLinkPage()
    a.city_main()
    print "end", time.time() - sta
# https://www.yelp.com/search?cflt=restaurants&find_loc=San+Francisco%2C+CA&start=10
