
import os

testing_script_dir = './management/test_today_info.py'
enc = 'utf-8'
command = 'echo exec(open("{}", encoding="{}").read()) | python manage.py shell'.format(testing_script_dir, enc)
os.system(command)
