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
quotation = '\''
comma_space = ', '
f = open('test_array', "w")
with open('Viet1K.txt') as file:
    for line in file:
##:[:-1] removes the \n(newline) character
        line = line[:-1]
        words_array.append(line)
viet_to_english = []
viet_to_english = words_array
##opens one window
driver = webdriver.Chrome()
driver.get("https://t.vdict.com/")
##change to viet-eng
driver.find_element_by_xpath("/html/body/div[1]/form/div[1]/div/select")\
    .click()
driver.find_element_by_xpath("/html/body/div[1]/form/div[1]/div/select/option[2]")\
    .click()
for item in viet_to_english:
    driver.find_element_by_xpath("/html/body/div[1]/form/div[3]/div[1]/div[1]/input")\
            .clear()
##type word 
    driver.find_element_by_xpath("/html/body/div[1]/form/div[3]/div[1]/div[1]/input")\
            .send_keys(item)
##submit
    driver.find_element_by_xpath("/html/body/div[1]/form/div[3]/div[1]/div[2]/a")\
        .click()
    sleep(2)
    try:
        one_word_translation = driver.find_element_by_xpath('/html/body/div[1]/form/div[3]/div[1]/div[4]/div/ul[1]/li/b').text
    except NoSuchElementException:
        one_word_translation = 'Word not found'
    print("Simple translation: ", one_word_translation)
    try:
        full_translation = driver.find_element_by_xpath('/html/body/div[1]/form/div[3]/div[1]/div[4]/div').text
    except NoSuchElementException:
        full_translation = 'Word not found'
    dictionary = item + ':' + full_translation
    print(full_translation)
    print('---------------------------------------------------------------')
    shortcut = item + ',,'
    extra_shortcut = item + ',?'
    with open("vdict_viet_to_english.plist", "a") as f:
        f.write("<dict>\n<key>shortcut</key>\n<string>{}</string>\n<key>phrase</key>\n<string>{}</string>\n</dict>".format(shortcut, one_word_translation))
        f.write("<dict>\n<key>shortcut</key>\n<string>{}</string>\n<key>phrase</key>\n<string>{}</string>\n</dict>".format(extra_shortcut, full_translation))
