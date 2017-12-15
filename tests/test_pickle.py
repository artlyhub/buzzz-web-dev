import os, sys, pickle

os.chdir('../')

if not os.path.exists('sensitives.pickle'):
    with open('sensitives.pickle', 'wb') as f:
        empty_data = {'SECRET_KEY': '',
                      'IP_ADDRESS': '',
                      'DB_NAME': '',
                      'DB_USER': '',
                      'DB_PW': '',
                      'DEBUG': '',
                      'APP_STATUS': ''}
        pickle.dump(empty_data, f)
        print('Created empty sensitives.pickle file')

pickle_file = open('sensitives.pickle', 'rb')
data = pickle.load(pickle_file)
print('Current IP_ADDRESS: ' + data['IP_ADDRESS'])
print('Current DEBUG status: ' + str(data['DEBUG']))

if sys.argv[1] == 'ip':
    data['IP_ADDRESS'] = sys.argv[2]
    with open('sensitives.pickle', 'wb') as f:
        pickle.dump(data, f)
    print('Update complete')
elif sys.argv[1] == 'debug':
    data['DEBUG'] = bool(sys.argv[2])
    with open('sensitives.pickle', 'wb') as f:
        pickle.dump(data, f)
    print('Update complete')
elif sys.argv[1] == 'app_status':
    data['APP_STATUS'] = sys.argv[2]
    with open('sensitives.pickle', 'wb') as f:
        pickle.dump(data, f)
    print('Update complete')
