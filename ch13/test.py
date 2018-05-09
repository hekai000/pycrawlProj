# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader.processors import TakeFirst
proc = TakeFirst()
print proc(['', 'one', 'two', 'three'])
from scrapy.loader.processors import Join
proc = Join()
print proc(['', 'one', 'two', 'three'])
proc = Join('<br>')
print proc(['', 'one', 'two', 'three'])
from scrapy.loader.processors import Compose
proc = Compose(lambda v:v[0], str.upper, stop_on_none=False)
print proc([ 'one', 'two', 'three'])
from scrapy.loader.processors import MapCompose
def filter_world(x):
    return None if x=='world' else x

proc = MapCompose(filter_world,unicode.upper)
print proc([u'hello', u'world', u'this', u'is', u'scrapy'])

from scrapy.loader.processors import SelectJmes,Compose,MapCompose
proc = SelectJmes("foo")
print proc({'foo':'bar'})
print proc({'foo': {'bar':'baz'}})