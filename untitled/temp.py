import urllib2
import re
import requests
from metar import Metar
import unicodedata
import json
import memcache
import redis

temp = redis.Redis(host='localhost', port=6379, db=0)
temp.set('foo', 'bar')
print temp.get('foo')

#client = memcache.Client([('127.0.0.1', 11211)])
#data = {"key1": "value1",
 #       "key2": "value2"}
#client.set_multi(data, time=0, key_prefix="pfx_")
#print client.get("pfx_key1")

r = requests.get('http://tgftp.nws.noaa.gov/data/observations/metar/stations/KSGS.TXT');
#print r.text;

s = r.text
#print type(s)


lis = s.splitlines()
#print lis

metar_str= str(lis[1])
obs = Metar.Metar(metar_str)
#print obs.string()


lis = obs.string().splitlines()
#print lis

js = json.dumps(lis)
#print js

print type(js)


