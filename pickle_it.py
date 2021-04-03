import pickle	#import the pickle module

data = [1,2,3,4,5,6,77,8,86,6]	#The data to be pickled

def pickle_the_data(data):
	with open('pickledfile.pickle','wb+') as fil:
		pickle.dump(data,fil)

def unpickle_the_data(filename):
	with open(filename + '.pickle' , 'rb+') as fil:
		p = pickle.load(fil)
	return(p)

# print(unpickle_the_data('pickledfile'))
