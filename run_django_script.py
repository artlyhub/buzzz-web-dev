
import os

testing_script_dir = './management/OHLCV_KD.py'
enc = 'utf-8'
command = 'echo exec(open("{}", encoding="{}").read()) | python manage.py shell'.format(testing_script_dir, enc)
os.system(command)
