# coding:utf8
import sys
import re
import urllib2
import urllib
import requests
import cookielib
import time

## 这段代码是用于解决中文报错的问题
reload(sys)
sys.setdefaultencoding("utf8")
#####################################################

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)

first_url = 'http://www.adidas.com.cn/productlist/?sport_gender=40&product_style=215'
opener.addheaders = [
    ('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'),
    ('Accept', 'text/html, application/xhtml+xml, image/jxr, */*'),
    ('Accept-Language', 'en-US, en; q=0.8, zh-Hans-CN; q=0.5, zh-Hans; q=0.3'),
    ('Accept-Encoding', 'gzip, deflate'),
    ('Connection', 'Keep-Alive'),
    ('DNT', '1'),
    ('Host', 'www.adidas.com.cn'),
]

# resp = opener.open(first_url)

url = 'http://www.adidas.com.cn/checkout/cart/add'

values = {
    'isajax': 'yes',
    'product': '344904',
    'qty': '1',
    'release2': 'yes',
    'super_attribute[185]': '70',
    # 'token': 'ec21ec19de83a86263e0652350e85ced'
}
# print len(values)
data = urllib.urlencode(values, "utf8")
# print data
# print len(data)
# exit(0)

current_time=time.time()
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:42.0) Gecko/20100101 Firefox/42.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US, en; q=0.8, zh-Hans-CN; q=0.5, zh-Hans; q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Cache-Control': 'no-cache',
    'Connection': 'Keep-Alive',
    'Content-Length': '68',
    'Pragma': 'no-cache',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Host': 'www.adidas.com.cn',
    'Referer': 'http://www.adidas.com.cn/productlist/?cat=718&sport_gender=39',
    'X-Requested-With': 'XMLHttpRequest',
    'Cookie': 'ak_bmsc=7002973902B2F0843B48442542C68B277AE00A3E0406000030E207597CC1FA78~plndkDcw79fhXb35KuP7MGbdRaQNLTl7r3Gc+KAI2Bve/kj0I7kSWWOcNBOAQaPdWUv890ojSxd1UXWCkLLioTtFziszFC5LGd4CwzpjI3dlIC3QEUVrKXRGJ2x2EI7b9GRS/ce25r0j4Uf0yfimhEexZixw8JHhg7pR0EjURnmRTgpmXlLjXZeGyJ0PeSZ3nZCE+SyyL+No9KR2Jj9S6YuJcdyipPq6XxJ3QKdmzZVi2vGUE5vqzJsre9n+0sMfGJ; bm_mi=17DAB946A0DE62CADE28714F05C24CD1~uaCX7qwzAF/wxMe9Rj8XkKRa4F4ocjeKc7f6lf9YhDITOOmCn6XsmGBffrk12EiI4TdKkIvscdvrRrpnxU8tgh7/dSq1c8QARNCeXMBTFn5Y3193khfOKaVsoXey3SNT4LGHi86MqI/ytBKxGduQZO3lslpo35BxiDXohDq3iGdbDO4uIyGN8SviOkbOvUlTPDU9KJ0vJoWfJbGz5Eshx4bIUR9ckI3oWvcy6UgoM4HyJAeL/HvfKPp2fJEh6Qbye5kGjaLIYNlgquxciAfcOg==; frontend=8qddmtn8q7n72vg87f002agkc1; bm_sv=A015D3A95D1520063CB40DB85C170D26~nUtkGVXsj+49FwDOLbkidKHbveVwBKes8TXPY1VIC0A9f5RuabguTiKM2plfXV1cbLu7MrYR7Fi+7uHsojIg45f2VhvvW296wS27c0Oh5jmYBoqVPrRs57cfxXrEhEioshYYsScSZukni0gBSoSspK+CyI6FZRr+tZ/GRlwvNR0=; utag_main=v_id:015bc6cb9a33007aeebe627df6000404c001900900bd0$_sn:1$_ss:0$_st:1493690751563$ses_id:1493688883764%3Bexp-session$_pn:3%3Bexp-session; AMCV_7ADA401053CCF9130A490D4C%40AdobeOrg=-227196251%7CMCIDTS%7C17289%7CMCMID%7C18320438211673661159041391135778024329%7CMCAID%7CNONE%7CMCOPTOUT-1493696088s%7CNONE%7CMCAAMLH-1494293688%7C11%7CMCAAMB-1494293688%7Chmk_Lq6TPIBMW925SPhw3Q; _ga=GA1.3.1147519457.1493688885; AMCVS_7ADA401053CCF9130A490D4C%40AdobeOrg=1; s_pers=%20s_vnum%3D1496246400193%2526vn%253D1%7C1496246400193%3B%20pn%3D1%7C1496280900791%3B%20c4%3DPLP%257CG_%25E7%2594%25B7%25E5%25AD%2590%257CPR_SUMMER%7C1493690753619%3B%20s_invisit%3Dtrue%7C1493690753619%3B; s_cc=true; __v3_c_sesslist_11403=epgv7einzy_dc8; __v3_c_pv_11403=3; __v3_c_session_11403=1493688895570942; __v3_c_today_11403=1; __v3_c_review_11403=0; __v3_c_last_11403=1493688913803; __v3_c_visitor=1493688895570942; __v3_c_session_at_11403=1493688951876; s_sq=ag-adi-cn-prod%3D%2526pid%253DPLP%25257CG_%2525E7%252594%2525B7%2525E5%2525AD%252590%25257CPR_SUMMER%2526pidt%253D1%2526oid%253Dfunctiononclick%252528event%252529%25257Bga%252528%252527send%252527%25252C%252527event%252527%25252C%252527cart%252527%25252C%252527add%252527%25252C%252527list%252527%25252C1099%252529%25253B%25257D%2526oidt%253D2%2526ot%253DSUBMIT; Hm_lvt_c29ad6ea0a27499743676357b8867377=1493688897; Hm_lpvt_c29ad6ea0a27499743676357b8867377=1493688901; Hm_lvt_690ef42ff30759b60f6c189b11f82369=1493688897; Hm_lpvt_690ef42ff30759b60f6c189b11f82369=1493688901; _gat=1'
}

req = urllib2.Request(url, data, headers)

response = urllib2.urlopen(req, timeout=10)
# print response
result = response.read()
print result
# print result.decode('utf8')



