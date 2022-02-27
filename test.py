# -*- coding:UTF-8 -*-
from urllib2 import Request
from urllib2 import build_opener
from urllib2 import ProxyHandler
from urllib2 import HTTPCookieProcessor
from urllib2 import URLError
import cookielib


def down_html(url):
    req = Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36')
    my_proxy = ProxyHandler({'http': 'http://127.0.0.1:10810','https': 'https://127.0.0.1:10810'})
    cookie_file = 'config/cookie.txt'
    #cj_receive = cookielib.CookieJar()
    cookie = cookielib.MozillaCookieJar(cookie_file)
    my_cookie_handler = HTTPCookieProcessor(cookie)
    opener = build_opener(my_proxy,my_cookie_handler)
    response = opener.open(req)
    cookie.save(ignore_expires=True,ignore_discard=True)
    for item in cookie:
        print 'Name = '+item.name
        print 'Value = '+item.value
    print '------'
    print response.read()


if __name__ == '__main__':
    down_html('https://www.pixiv.net/')