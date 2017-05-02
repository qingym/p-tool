# coding:utf8

__author__ = 'taojing'

# coding:utf8
# https://gist.github.com/evandrix/3694955



from ghost import Ghost
import time
import httplib
import random
import hashlib
import json
import requests
import re
import shutil

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


def f_html_to_text(strr):
    return re.sub(r'</?\w+[^>]*>', '', strr).strip('\n').strip()


def f_https_download(url):
    # rest for a bit
    time.sleep(random.randint(10, 30))
    try:
        conn = httplib.HTTPSConnection("www.yelp.com")
        conn.request("GET", url)
        response = conn.getresponse()
        print url, response.status, response.reason
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


def f_https_download_image(image_url, address):
    print image_url, address
    try:
        r = requests.get(image_url, stream=True)
        if r.status_code == 200:
            with open(address, 'wb') as f:
                for chunk in r.iter_content(1024):
                    f.write(chunk)
    except Exception, e:
        r = requests.get(image_url, stream=True)
        if r.status_code == 200:
            with open(address, 'wb') as f:
                for chunk in r.iter_content(1024):
                    f.write(chunk)


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
        for content_url in list_url[0:100]:
            try:
                self.content_analyser(content_url)
            except Exception, e:
                print content_url, repr(e)

    def content_analyser(self, content_url):
        response = f_https_download(content_url)

        result = ContentResult()
        result.url = content_url
        # 716
        response = response[response.find('<span itemprop="streetAddress">') + len('<span itemprop="streetAddress">'):]
        result.address = f_html_to_text(f_html_to_text(response[0:response.find('</address>')]))
        # 719
        response = response[response.find('<span itemprop="telephone">') + len('<span itemprop="telephone">'):]
        result.tele = f_html_to_text(response[0:response.find('</span>')])
        # 1078
        response = response[response.find('<h1 class="biz-page-title embossed-text-white shortenough">') + len(
            '<h1 class="biz-page-title embossed-text-white shortenough">'):]
        result.title = f_html_to_text(response[0:response.find('</h1>')].strip("\n"))
        # 1144
        response = response[
                   response.find('<span class="category-str-list">') + len('<span class="category-str-list">'):]
        result.type = f_html_to_text((response[0:response.find('</span>')]))
        # 1557
        response = response[
                   response.find('<div class="showcase-photo-box">') + len('<div class="showcase-photo-box">'):]
        response = response[response.find('src="') + len('src="'):]
        image_url = response[0:response.find('"')]
        md5_address = hashlib.md5(content_url).hexdigest() + '.jpg'
        result.imageList.append(image_url)
        result.imageList.append(md5_address)
        f_https_download_image(image_url, 'ca/' + md5_address)
        # 9039
        response = response[
                   response.find('<table class="table table-simple hours-table">') + len(
                       '<table class="table table-simple hours-table">'):]
        result.hours = f_html_to_text((response[0:response.find('</tbody>')])).replace('\n', "").replace('Closed now',
                                                                                                         "")

        line = json.dumps(result.__dict__)
        f_line_prepender(line)
        return result


class ContentResult():
    def __init__(self):
        self.url = None
        self.title = None
        self.type = None
        self.address = None
        self.tele = None
        self.imageList = []
        self.hours = ''


def f_content_url():
    list_url = []
    for line in open("ca.content_page_link_list"):
        print line
        if line.startswith("/"):
            list_url.append(line)

    print "length", len(list_url)
    return list_url


def f_line_prepender(line):
    f_line_prepender_name('ca.result', line)


def f_line_prepender_name(file_name, line):
    with open(file_name, 'r+') as f:
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

