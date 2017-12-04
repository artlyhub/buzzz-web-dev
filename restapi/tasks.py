
from restapi.models import Ticker
from restapi.models import OHLCV
from datetime import datetime
import pandas as pd
from bs4 import BeautifulSoup
import requests
import simplejson as json
from celery.decorators import task


@task(name="scrape_naver_ohlcv")
def get_ohlcv():













