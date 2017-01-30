import cPickle

def dumpAsPickle(filename, toDump):
	with open("dumps/"+filename+".pkl", 'wb') as fid:
			cPickle.dump(toDump, fid)

def loadFromPickle(filename):
	with open("dumps/"+filename+".pkl", 'r') as fid:
		return cPickle.load(fid)