import os

testing_script_dir = './algo_test/ohlcv_scraper.py'
command = 'echo exec(open("{}").read()) | python manage.py shell'.format(testing_script_dir)
os.system(command)
