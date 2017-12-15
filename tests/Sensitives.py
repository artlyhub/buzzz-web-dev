## @Ver     0.8v
## @Author  Phillip Park
## @Date    2017/12/12
## @Details 장고 서버를 실행하기 위한 sensitives.pickle 파일 핸들링

import pickle


class Sensitives:
    def __init__(self):
        self.sensitives = {'SECRET_KEY': '',
                           'IP_ADDRESS': '',
                           'DB_NAME': '',
                           'DB_USER': '',
                           'DB_PW': '',
                           'DEBUG': '',
                           'APP_STATUS': ''}
        self.data = None

    def setup(self):
        self.sensitives['SECRET_KEY'] = input('SECRET_KEY: ')
        self.sensitives['IP_ADDRESS'] = input('IP_ADDRESS: ')
        self.sensitives['DB_NAME'] = input('DB_NAME: ')
        self.sensitives['DB_USER'] = input('DB_USER: ')
        self.sensitives['DB_PW'] = input('DB_PW: ')
        self.sensitives['DEBUG'] = bool(input('DEBUG (True/False): '))
        self.sensitives['APP_STATUS'] = input('APP_STATUS (dev/prod): ')

    def open(self):
        pickle_file = open('sensitives.pickle', 'rb')
        self.data = pickle.load(pickle_file)
        print('Data loaded')

    def check(self):
        if self.data == None:
            self.open_file()
        for key, val in self.data.items():
            print(key + ': ' + val)

    def set(self, key, val):
        if key == 'DEBUG':
            self.data[key] = bool(val)
        else:
            self.data[key] = str(val)
        print('Successfully set ' + key + ' as ' + str(val))

    def save(self):
        pickle_file = open('sensitives.pickle', 'wb')
        pickle.dump(self.data, pickle_file)
        print('Data saved')
