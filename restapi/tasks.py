from __future__ import absolute_import, unicode_literals

from datetime import datetime
from selenium import webdriver
import pyautogui
import os
from bs4 import BeautifulSoup
import requests
import sqlite3
import time
import simplejson as json
from celery.decorators import task

from restapi.models import Ticker, OHLCV



@task(name="scrape_naver_ohlcv")
def hi():
	print('hi hi')
