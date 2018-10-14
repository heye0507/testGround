#! /usr/bin/env python3
# coding: utf-8

import requests
import re
import sys


url_search_base = 'http://songsearch.kugou.com/song_search_v2?callback=jQuery112406335936274624496_1539417511214&keyword='
hash_url = 'http://www.kugou.com/yy/index.php?r=play/getdata&hash='




keyword = input("歌曲名: ")

response = requests.get(url_search_base+keyword)

print('----------------')

songname = re.findall('"FileName":"(.*?)"',response.text)
index = 0
for song in songname:
	print ('[%d]:%s' %(index,song))
	index+=1

files = re.findall(r'"FileHash":"(.*?)"',response.text)

num = int(input("请输入序号: "))


hash_response = requests.get(hash_url+files[num])

play_url = re.findall(r'"play_url":"(.*?)"',hash_response.text)
download_url = re.sub(r'\\',r'',play_url[0])


music = requests.get(download_url, stream=True)
total_size = music.headers['Content-Length']
chunk_size=1024
rate = chunk_size / int(total_size) * 100
counter = 1

with open(songname[0]+'.mp3','wb') as f:
	for chunk in music.iter_content(chunk_size=chunk_size):
		if chunk:
			f.write(chunk)
			print ('%d%%' %int(rate*counter),end = '\r')
			counter+=1

print('\ndone') 


