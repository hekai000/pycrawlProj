# -*- coding: utf-8 -*-
import redis

r = redis.Redis(host='127.0.0.1', port=6379)
r.set('name', 'qiye')
print r.get('name')

pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
r = redis.Redis(connection_pool=pool)
r.set('name', 'hekai')
print r.get('name')

# r.set('name', 'hekai',ex=3)
# print r.get('name')
# import time
# time.sleep(4)
# print r.get('name')

r.setnx('name', 'hah')
print r.get('name')

# r.setex('name', 'qiye', 5)
# time.sleep(6)
# print r.get('name')

r.psetex('name', 5000,'qiye')
print r.get('name')

r.mset(age=20, country='china')
print r.mget('age','country')

print r.getset('name','hello')

r.set('name',u'qiye安全博客')
print r.getrange('name',4,9)

r.setrange('name', 1, 'python')
print r.get('name')

from binascii import hexlify
r.set('name','qiye')
print bin(int(hexlify('qiye'), 16))
r.setbit('name',2,0)
print r.get('name')
print bin(int(hexlify(r.get('name')),16))

print r.getbit('name', 2)
print r.strlen('name')
r.append('name','python')
print r.get('name')