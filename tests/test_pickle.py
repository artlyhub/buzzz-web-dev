import sys, pickle

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
    data['DEBUG'] = sys.argv[2]
    with open('sensitives.pickle', 'wb') as f:
        pickle.dump(data, f)
    print('Update complete')
