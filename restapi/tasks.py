from __future__ import absolute_import, unicode_literals

from celery.decorators import task

@task(name="scrape_naver_ohlcv")
def hi():
	return 'hi'

@task(name="test")
def test():
	return 'hi'
