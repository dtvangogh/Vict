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
with open('Viet11K.txt') as file:
    for line in file:
        index_of_space = line.find(' ')
        line = line[:index_of_space]
        if line not in words_array:
            with open("remove_duplicates_Viet11K.txt", "a") as f:
                f.write('{}\n'.format(line))
                words_array.append(line)
