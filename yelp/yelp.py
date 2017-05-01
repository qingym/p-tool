# coding:utf8

__author__ = 'taojing'

# coding:utf8
# https://gist.github.com/evandrix/3694955



from ghost import Ghost
import time
import httplib
import random
import json

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
main_url = 'https://www.yelp.com'


def f_https_download(url):
    # rest for a bit
    # time.sleep(random.randint(10, 30))
    try:
        conn = httplib.HTTPSConnection("www.yelp.com")
        conn.request("GET", url)
        response = conn.getresponse()
        print response.status, response.reason
        if response.status == 503:
            print "is 503"
            print response.read()
            exit(0)
        data = response.read()
    except Exception, e:
        # print repr(e)
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
                f_link_page_analyser(f_https_download(link_page_url))
            except Exception, e:
                print link_page_url, repr(e)


def f_list_url():
    url = '/search?cflt=restaurants&find_loc=San+Francisco%2C+CA'
    list_url = []
    for i in range(1, 100):
        list_url.append(url + "&start=" + str(i * 10))

    return list_url


class YelpContentPage():
    def __init__(self):
        pass

    def process(self):
        list_url = f_content_url()
        # 内容页的url处理
        for content_url in list_url:
            try:
                reponses = f_https_download(content_url)
                self.content_analyser(reponses, content_url)
            except Exception, e:
                print repr(e)

    def content_analyser(self, reponses, content_url):
        result = ContentResult()
        result.url = content_url
        reponses = reponses[reponses.find('<span itemprop="streetAddress">') + len('<span itemprop="streetAddress">'):]
        result.address = reponses[0:reponses.find('</address>')]
        reponses = reponses[reponses.find('<span itemprop="telephone">') + len('<span itemprop="telephone">'):]
        result.tele = reponses[0:reponses.find('</span>')]
        line = json.dumps(result.__dict__)
        f_line_prepender(line)

class ContentResult():
    def __init__(self):
        self.url = None
        self.address = None
        self.tele = None
        self.imageList = []
        self.hours = ''


def f_content_url():
    list_url = []
    for line in open("link_page_url.ca"):
        print line
        if line.startswith("/"):
            list_url.append(line)

    print "length", len(list_url)
    return list_url


def f_line_prepender(line):
    with open("ca.result", 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line.rstrip('\r\n') + '\n' + content)


def f_link_page_analyser(page_content):
    link_html = page_content.split("<span class=\"indexed-biz-name\">")
    for link_area in link_html[1:]:
        link_area = link_area[link_area.find('href="') + 6:]
        print link_area[0:link_area.find('"')]


if __name__ == '__main__':
    sta = time.time() * 1000
    a = YelpContentPage()
    a.process()
    print "end", time.time() * 1000 - sta
# https://www.yelp.com/search?cflt=restaurants&find_loc=San+Francisco%2C+CA&start=10
