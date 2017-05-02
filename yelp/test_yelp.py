__author__ = 'Administrator'

import unittest
import os
import json

from yelp import *


class MyTestCase(unittest.TestCase):
    def test_YelpContentPage(self):
        aa = YelpContentPage()
        url = '/biz/liholiho-yacht-club-san-francisco-2'
        result = aa.content_analyser(url)
        print json.dumps(result.__dict__)
        assert os.path.isfile('ca/' + result.imageList[1])


    def test_download_image(self):
        save_file = 'ca/ls.jpg'
        f_https_download_image('https://s3-media3.fl.yelpcdn.com/bphoto/Xb-iaTWxqLd8TD4TUbybqw/ls.jpg', save_file)
        assert os.path.isfile(save_file)

    def test_f_html_to_text(self):
        str = "<img /><a>srcd</a>hello</br><br/>"
        str = f_html_to_text(str)
        print str
        assert str.find('srcd') == 0


if __name__ == '__main__':
    unittest.main()
