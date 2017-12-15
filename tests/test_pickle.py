import os, sys, pickle

os.chdir('../')

def create_if_none():
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

def update(key, val):
    create_if_none()
    pickle_file = open('sensitives.pickle', 'rb')
    data = pickle.load(pickle_file)
    if key != 'DEBUG':
        data[key] = val
    else:
        data[key] = bool(int(val))
    with open('sensitives.pickle', 'wb') as f:
        pickle.dump(data, f)
    print('Update complete')
    print('Current IP_ADDRESS: ' + data['IP_ADDRESS'])
    print('Current {} status: '.format(key) + str(data[key]))

if sys.argv[1] == 'IP_ADDRESS':
    create_if_none()
    update('IP_ADDRESS', sys.argv[2])

elif sys.argv[1] == 'DEBUG':
    create_if_none()
    update('DEBUG', sys.argv[2])

elif sys.argv[1] == 'APP_STATUS':
    create_if_none()
    update('APP_STATUS', sys.argv[2])

else:
    create_if_none()
    pickle_file = open('sensitives.pickle', 'rb')
    data = pickle.load(pickle_file)
    print('Current IP_ADDRESS: ' + data['IP_ADDRESS'])
    print('Current DEBUG status: ' + str(data['DEBUG']))
