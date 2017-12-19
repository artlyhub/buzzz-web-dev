## @Ver     0.8v
## @Author  Phillip Park
## @Date    2017/12/17
## @Details tools에 있는 모듈들을 합쳐주는 기능

import os, sys, glob

start_path = os.getcwd()
proj_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "buzzz.settings")
sys.path.append(proj_path)
os.chdir(proj_path)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

### scripts ###
from tools.Benchmark import Benchmark
from tools.Cleaner import Cleaner
from tools.Data import Data
from tools.Processor import Processor
from tools.Sensitives import Sensitives
import tools.KRX as KRX

if sys.argv[1] == 'cleanmigrations':
    c = Cleaner(start_path)
    c.clean_migrations()
    db = start_path + '/db.sqlite3'
    if os.path.exists(db):
        os.remove(db)
        print('Removed database')

elif sys.argv[1] == 'sensitives':
    s = Sensitives(start_path)
    if sys.argv[2] == 'setup':
        s.setup()
    elif sys.argv[2] == 'check':
        s.check()
    elif sys.argv[2] == 'set':
        s.set(sys.argv[3], sys.argv[4])
        s.save()

elif sys.argv[1] == 'bm':
    b = Benchmark(start_path)
    df, exists = b.get()
    recent_date = list(df.ix[len(df)-1])[0].replace('-', '')
    if exists:
        print('Recent update: ' + recent_date)
    else:
        print('Downloaded data to: ' + recent_date)

elif sys.argv[1] == 'data':
    d = Data(start_path)
    if sys.argv[2] == 'send':
        if sys.argv[3] == 'ticker':
            d.send_ticker()
        elif sys.argv[3] == 'bm':
            d.send_bm()
        elif sys.argv[3] == 'ohlcv':
            d.send_ohlcv()

elif sys.argv[1] == 'krx':
    KRX.main(start_path)

elif sys.argv[1] == 'process':
    p = Processor()
    p.get_data_local()
    p.set_return_portfolio()
    p.bm_data()
    p.save_mom_volt_cor_vol()
