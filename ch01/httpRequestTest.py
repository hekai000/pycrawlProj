# -*- coding: utf-8 -*-

import urllib2
import urllib
import cookielib
# method 1
def urlopenTest1():
    response = urllib2.urlopen("http://www.baidu.com")
    html = response.read()
    print html

# method 2
def urlopenTest2():
    req = urllib2.Request("http://www.zhihu.com")
    response = urllib2.urlopen(req)
    html = response.read()
    print html


def urlopenTest3():
    url = "http://10.1.30.251/home/"
    postdata = {'username': "admin1", "passwd": "qwer1234"}
    data = urllib.urlencode(postdata)
    user_agent = "Mozilla/5.0 (Windows NT 6.1; W…) Gecko/20100101 Firefox/59.0"
    referer = "http://10.1.30.251/devadm/accounts/login/"
    headers = {'User-Agent': user_agent, 'Referer': referer}
    req = urllib2.Request(url, data, headers)
    response = urllib2.urlopen(req)
    html = response.read()
    with open("c:\\1.html","w+") as f:
        f.write(html)
    #print html

def urlopenTest4():
    url = "http://10.1.30.251/home/"
    postdata = {'username': "admin1", "passwd": "qwer1234"}
    data = urllib.urlencode(postdata)
    user_agent = "Mozilla/5.0 (Windows NT 6.1; W…) Gecko/20100101 Firefox/59.0"
    referer = "http://10.1.30.251/devadm/accounts/login/"
    req = urllib2.Request(url)
    req.add_header(user_agent)
    req.add_header(referer)
    req.add_data(data)
    response = urllib2.urlopen(req)
    html = response.read()
    with open("c:\\1.html","w+") as f:
        f.write(html)
    #print html


def cookieTest():
    cookie = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    response = opener.open("http://www.zhihu.com")
    for item in cookie:
        print item.name + ":" + item.value

def cookieTest2():
    opener = urllib2.build_opener()
    opener.addheaders.append(('Cookie', 'email=' + "hekaikylin@163.com"))
    req = urllib2.Request("http://www.zhihu.com")
    response = opener.open(req)
    print "header------>", response.headers
    retdata = response.read()
    print "----------------"
    print retdata


def httpProxyTest():
    proxy = urllib2.ProxyHandler({'http': '127.0.0.1:8087'})
    opener = urllib2.build_opener(proxy, )
    response = opener.open("http://www.zhihu.com/")
    print response.read()
if __name__ == "__main__":
    httpProxyTest()