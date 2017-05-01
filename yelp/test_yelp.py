__author__ = 'Administrator'

import unittest
from yelp import  *


class MyTestCase(unittest.TestCase):
    def test_something(self):
        aa = YelpContentPage()
        aa.content_analyser(f_https_download("/biz/turners-kitchen-san-francisco"))
        assert True


if __name__ == '__main__':
    unittest.main()
