# -*- coding: utf-8 -*-
"""
Created on Sat May 18 19:13:00 2019

@author: Damar Adi
"""

import bs4 as bs
import urllib.request
import csv

main_source = urllib.request.urlopen("https://www.azlyrics.com/a/arcticmonkeys.html").read()
soup = bs.BeautifulSoup(main_source, 'lxml')
songs = soup.find(id="listAlbum")

titles = []
lyrics = []
for s in songs.find_all('a', href=True):
    source = urllib.request.urlopen(f"https://www.azlyrics.com/{s['href'][2:]}").read()
    soup = bs.BeautifulSoup(source, 'lxml')
    title = soup.find("div",class_="ringtone").find_next_sibling()
    titles.append(title.get_text())
    lyric = soup.find("div",class_="ringtone").find_next_sibling("div")
    lyrics.append(lyric.get_text().strip())
    print(title.get_text())
    
with open('lyrics_with_titles.tsv','a', encoding='utf8', newline='') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(zip(titles,lyrics))
