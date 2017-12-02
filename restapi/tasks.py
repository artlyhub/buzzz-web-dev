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



@task(name="kos_file_down")
def down():
	driver = webdriver.Firefox()
	driver.get('http://kind.krx.co.kr/corpgeneral/corpList.do?method=loadInitPage')
	time.sleep(4)
	btn = driver.find_element_by_id(btn_id)
    btn.click()
    driver.execute_script('fnSearchWithoutIndex();') #검색 버튼 
    time.sleep(3)
    driver.execute_script('fnDownload();')
    time.sleep(4)
    pyautogui.press('down')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(3)
    driver.execute_script('fnDownload();')
    time.sleep(4)
    pyautogui.press('enter')



    
