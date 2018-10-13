#! /usr/bin/env python3
# coding: utf-8

import requests
#import time
import re
#import random
#import math
#import os
#import pickle
#from bs4 import BeautifulSoup

'''url_search_base = 'http://songsearch.kugou.com/song_search_v2?callback=jQuery112406335936274624496_1539417511214&keyword='

keyword = '一百万个可能'

response = requests.get(url_search_base+keyword)
print (response.status_code)
print(response.headers)
print('----------------')

songname = re.findall('"SongName":"(.*?)"',response.text)
index = 0
for song in songname:
	print ('[%d]:%s' %(index,song))
	index+=1
#print(response.text)'''

url_test = 'http://fs.w.kugou.com/201810131617/ab71285a7be0cbc925202997726efad8/G137/M02/03/15/yQ0DAFuaCCGAQmMwADsktht-moM154.mp3'

with open('test_song.mp3','wb') as f:
	f.write(requests.get(url_test).content)
print ("downloaded")





