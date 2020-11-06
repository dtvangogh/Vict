#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup
import numpy
import getpass
import io
import re
import os.path, sys, stat
import requests
from bs4 import BeautifulSoup
import sys
import os
import selenium
from sys import argv
from array import array
from selenium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException

words_array = []
missed_words_array = []
quotation = '\''
comma_space = ', '
count = 0
text_file = argv[3]
with open(text_file) as file:
    for line in file:
        line = line[:-1]
        words_array.append(line)
viet_to_english = []
viet_to_english = words_array
driver = webdriver.Chrome()
language = argv[1]
plist_file = argv[2]

##add language urls here

if argv[1] == 'vietnamese':
    url = 'https://translate.google.com/#view=home&op=translate&sl=en&tl=vi'
if argv[1] == 'spanish':
    url = 'https://translate.google.com/#view=home&op=translate&sl=en&tl=es'
if argv[1] == 'russian':
    url = 'https://translate.google.com/#view=home&op=translate&sl=en&tl=ru'
if argv[1] == 'french':
    url = 'https://translate.google.com/#view=home&op=translate&sl=en&tl=fr'
if argv[1] == 'italian':
    url = 'https://translate.google.com/#view=home&op=translate&sl=en&tl=it'
if argv[1] == 'chinese':
    url = 'https://translate.google.com/#view=home&op=translate&sl=en&tl=zh-CN'
if argv[1] == 'korean':
    url = 'https://translate.google.com/#view=home&op=translate&sl=en&tl=ko'
if argv[1] == 'japanese':
    url = 'https://translate.google.com/#view=home&op=translate&sl=en&tl=ja'
if argv[1] == 'vietnamese-english':
    url = 'https://translate.google.com/#view=home&op=translate&sl=vi&tl=en'


with open(plist_file, "a") as f:
    f.write('<array>\n')
driver.get(url)
sleep(3)
    
for item in viet_to_english:
    try:
        send_item = item + ' '
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div/div/div[1]/textarea")\
                .send_keys(send_item)
        sleep(3)
        basic_translation = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]').text
        basic_translation = basic_translation[:-2]
        print(item)
        try:
            full_translation = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div[2]/div[3]/div[3]/div[1]/div[1]/div/div[2]').text
## remove 'frequency' bar and newline character from translation
            full_translation = full_translation.replace('Frequency', '')
            full_translation = full_translation.replace('\n\n', '\n')
            translation = basic_translation + '\n' + full_translation
            print(translation)
        except NoSuchElementException:
            missed_words_array.append(item)
        shortcut = item
        shortcut = shortcut.replace(' ', '.')
        extra_shortcut = shortcut + '?g'
        shortcut = shortcut + 'gg'
        
        with open(plist_file, "a") as f:
            f.write("<dict>\n<key>shortcut</key>\n<string>{}</string>\n<key>phrase</key>\n<string>{}</string>\n</dict>".format(shortcut, basic_translation))
            f.write("<dict>\n<key>shortcut</key>\n<string>{}</string>\n<key>phrase</key>\n<string>{}</string>\n</dict>".format(extra_shortcut, translation))
        count += 1
        print("{} words translated so far".format(count))
        print('---------------------------------------------------------------')
    except NoSuchElementException:
        missed_words_array.append(item)
    print('words missed')
    print(missed_words_array)
    print('---------------------------------------------------------------')
##clear input block
    driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div/div/div[1]/textarea")\
            .clear()

with open(plist_file, "a") as f:
    f.write('</array>\n')

        
        
