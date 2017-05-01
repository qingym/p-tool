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
    'product': '345602',
    'qty': '1',
    'release2': 'yes',
    'super_attribute[185]': '53',
    # 'token': 'ec21ec19de83a86263e0652350e85ced'
}
# print len(values)
data = urllib.urlencode(values, "utf8")
# print data
# print len(data)
# exit(0)

current_time=time.time()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Accept': '*/*',
    'Accept-Language': 'en-US, en; q=0.8, zh-Hans-CN; q=0.5, zh-Hans; q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Cache-Control': 'no-cache',
    'Connection': 'Keep-Alive',
    'Content-Length': '68',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Host': 'www.adidas.com.cn',
    'Referer': 'http://www.adidas.com.cn/productlist/?sport_gender=40&product_style=215',
    'X-Requested-With': 'XMLHttpRequest',
    # 'Cookie': 'bm_mi=7ECE0473C9F814EB13D2B38B46F4D83D~QKm0NFqnGXAH05t/L987yTkGaa/vHHJl6PSlDYVRs93WNCDhLscd4KI334JIGMcUQIRKMZAF72XCPRBM37lOeNJDFbT6ooT71uHdfGqoyZwwPb3LPXoCt5q/aeHYG53GwMo8o+CQi+TdZnpzllchbsVuszZW1Lw51mK8KzfbHTtu/OPaLNHzrvZUiTuVcnx4XgukswsTzU9WvUZQCBWsOdIBwYb12pxi21ORKa03Lk77/obYrxgq2RoEdbvUgGiJl/FTEQa1ykHfLFJz9l+E/Q==; __v3_c_pv_11403=6; __v3_c_session_11403=1493627339429491; AMCVS_7ADA401053CCF9130A490D4C%40AdobeOrg=1; __v3_c_session_at_11403=1493629172402; s_cc=true; bm_sv=F7A7D49AE8BD3CAA040E9BFDDC30A125~MqNJNWLKrLpkR4371VVpxGhuGLhuHz0g+fAv9MOC3RgciWU6LQDuaWnOgN1YY9VsnLEQCFLot+VvwJUosOhPeAeM+vM4tYgXummU2WVNckzUMzZPGkJNVHeuJOIGrglzsdHy4CTUeT56vErGaz2Gs5hF08BBYTdw4bMwEEWdJos=; s_sq=ag-adi-cn-prod%3D%2526pid%253DPLP%25257CG_%2525E7%252594%2525B7%2525E5%2525AD%252590%25257CPR_%2525E4%2525B8%25258B%2525E8%2525A3%252585%2526pidt%253D1%2526oid%253Dfunctiononclick%252528event%252529%25257Bga%252528%252527send%252527%25252C%252527event%252527%25252C%252527cart%252527%25252C%252527add%252527%25252C%252527list%252527%25252C269%252529%25253B%25257D%2526oidt%253D2%2526ot%253DSUBMIT%2526oi%253D1228; ak_bmsc=0CE52E61CC5F4DD46EF392166E127A473D93A52D79180000BEF106593E257221~plmJQHnz9Hpix6TeQiAXWkt8AsNKtvRA2s+fqR87LCVCt0I8+0ycq1PRRB9prQdpZAdzJEDys3wouanlvW0j5irmO0/vBGT4pgzigJalMHO0ik+h5/2AmMlOdU3QOIdlMyjE9YlWbn+ifAAMxE/nZNMrOSQXHJS2v6LLHHnNsTIEonDjBUc/U1nEq95rCPBW6oeMZxVM+/PiCFCZEtoMq9njLvU7GBg0pWF5hUX7mFUuBHqU+R1GZOYtxtr/tT2GyO; utag_main=v_id:015bc31f2a9d0016e062dce1995e020a1001909900bd0$_sn:1$_ss:0$_st:1493630971970$ses_id:1493627251359%3Bexp-session$_pn:7%3Bexp-session; AMCV_7ADA401053CCF9130A490D4C%40AdobeOrg=-227196251%7CMCIDTS%7C17288%7CMCMID%7C48385709600184338290871727469643275109%7CMCAAMLH-1494232051%7C11%7CMCAAMB-1494232051%7CcIBAx_aQzFEHcPoEv0GwcQ%7CMCOPTOUT-1493634451s%7CNONE%7CMCAID%7CNONE; __v3_c_sesslist_11403=epg2xdkx9v_dc7; __v3_c_today_11403=1; __v3_c_review_11403=0; __v3_c_last_11403=1493629248240; __v3_c_visitor=1493627339429491; s_pers=%20s_vnum%3D1496246400920%2526vn%253D1%7C1496246400920%3B%20pn%3D4%7C1496221161126%3B%20c4%3DPLP%257CG_%25E7%2594%25B7%25E5%25AD%2590%257CPR_%25E4%25B8%258B%25E8%25A3%2585%7C1493630975229%3B%20s_invisit%3Dtrue%7C1493630975233%3B; _ga=GA1.3.699113916.1493627282; _gat=1; Hm_lpvt_c29ad6ea0a27499743676357b8867377=1493629161; Hm_lpvt_690ef42ff30759b60f6c189b11f82369=1493629161; frontend=pmj21s1qf1hmpjml4tjnofioj3; Hm_lvt_c29ad6ea0a27499743676357b8867377=1493627281; Hm_lvt_690ef42ff30759b60f6c189b11f82369=1493627281'
    'Cookie': 'bm_mi=7ECE0473C9F814EB13D2B38B46F4D83D~QKm0NFqnGXAH05t/L987yTkGaa/vHHJl6PSlDYVRs93WNCDhLscd4KI334JIGMcUQIRKMZAF72XCPRBM37lOeNJDFbT6ooT71uHdfGqoyZwwPb3LPXoCt5q/aeHYG53GwMo8o+CQi+TdZnpzllchbsVuszZW1Lw51mK8KzfbHTtu/OPaLNHzrvZUiTuVcnx4XgukswsTzU9WvUZQCBWsOdIBwYb12pxi21ORKa03Lk77/obYrxgq2RoEdbvUgGiJl/FTEQa1ykHfLFJz9l+E/Q==; __v3_c_pv_11403=13; __v3_c_session_11403=1493627339429491; AMCVS_7ADA401053CCF9130A490D4C%40AdobeOrg=1; __v3_c_session_at_11403=1493631842076; s_cc=true; bm_sv=F7A7D49AE8BD3CAA040E9BFDDC30A125~MqNJNWLKrLpkR4371VVpxGhuGLhuHz0g+fAv9MOC3RgciWU6LQDuaWnOgN1YY9VsnLEQCFLot+VvwJUosOhPeAeM+vM4tYgXummU2WVNckxF+Iaj8eriB2Yk6ene7BaO0hcckNW59r5gioI7x0cHZsxesyttloxYtlaPniQ2k1w=; s_sq=ag-adi-cn-prod%3D%2526pid%253DPLP%25257CG_%2525E5%2525A5%2525B3%2525E5%2525AD%252590%2526pidt%253D1%2526oid%253Dfunctiononclick%252528event%252529%25257Bga%252528%252527send%252527%25252C%252527event%252527%25252C%252527cart%252527%25252C%252527add%252527%25252C%252527list%252527%25252C1099%252529%25253B%25257D%2526oidt%253D2%2526ot%253DSUBMIT%2526oi%253D1544; ak_bmsc=0CE52E61CC5F4DD46EF392166E127A473D93A52D79180000BEF106593E257221~plmJQHnz9Hpix6TeQiAXWkt8AsNKtvRA2s+fqR87LCVCt0I8+0ycq1PRRB9prQdpZAdzJEDys3wouanlvW0j5irmO0/vBGT4pgzigJalMHO0ik+h5/2AmMlOdU3QOIdlMyjE9YlWbn+ifAAMxE/nZNMrOSQXHJS2v6LLHHnNsTIEonDjBUc/U1nEq95rCPBW6oeMZxVM+/PiCFCZEtoMq9njLvU7GBg0pWF5hUX7mFUuBHqU+R1GZOYtxtr/tT2GyO; utag_main=v_id:015bc31f2a9d0016e062dce1995e020a1001909900bd0$_sn:1$_ss:0$_st:1493633640740$ses_id:1493627251359%3Bexp-session$_pn:17%3Bexp-session; AMCV_7ADA401053CCF9130A490D4C%40AdobeOrg=-227196251%7CMCIDTS%7C17288%7CMCMID%7C48385709600184338290871727469643275109%7CMCAAMLH-1494232051%7C11%7CMCAAMB-1494232051%7CcIBAx_aQzFEHcPoEv0GwcQ%7CMCOPTOUT-1493634451s%7CNONE%7CMCAID%7CNONE; __v3_c_sesslist_11403=epg2xdkx9v_dc7; __v3_c_today_11403=1; __v3_c_review_11403=0; __v3_c_last_11403=1493631859656; __v3_c_visitor=1493627339429491; s_pers=%20s_vnum%3D1496246400920%2526vn%253D1%7C1496246400920%3B%20pn%3D6%7C1496223772621%3B%20c4%3DPLP%257CG_%25E5%25A5%25B3%25E5%25AD%2590%7C1493633648110%3B%20s_invisit%3Dtrue%7C1493633648113%3B; _ga=GA1.3.699113916.1493627282; _gat=1; Hm_lpvt_c29ad6ea0a27499743676357b8867377=1493631773; Hm_lpvt_690ef42ff30759b60f6c189b11f82369=1493631773; Hm_lvt_c29ad6ea0a27499743676357b8867377='+str(current_time)+'; Hm_lvt_690ef42ff30759b60f6c189b11f82369='+str(current_time)+'; frontend=pmj21s1qf1hmpjml4tjnofioj3'
}

req = urllib2.Request(url, data, headers)

response = urllib2.urlopen(req, timeout=10)
# print response
result = response.read()
print result.decode('utf8')



