import os, sys

testing_script_dir = './tools/{}.py'.format(sys.argv[1])

enc = 'utf-8'
command = 'echo exec(open("{}", encoding="{}").read()) | python manage.py shell'.format(testing_script_dir, enc)
os.system(command)
