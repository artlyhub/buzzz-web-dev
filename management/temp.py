import pickle
import os

with open('../sensitives.pickle', 'rb') as f:
	data = pickle.load(f)
	print(data)

f.close()
print(data['IP_ADDRESS'])

# data['IP_ADDRESS'] = '45.32.249.71'
# # data['IP_ADDRESS'] = '45.32.63.193'
# data['DEBUG'] = False
# pickle.dump(data, open("../sensitives.pickle", "wb"))


