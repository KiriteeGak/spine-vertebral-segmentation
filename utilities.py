import cPickle
import numpy as np

def dumpAsPickle(filename, toDump):
	with open("dumps/"+filename+".pkl", 'wb') as fid:
			cPickle.dump(toDump, fid)

def loadFromPickle(filename):
	with open("dumps/"+filename+".pkl", 'r') as fid:
		return cPickle.load(fid)

def padImages(image_array):
	size = np.shape(image_array)
	padded_matrix = np.zeros((size[0]+2,size[1]+2))
	padded_matrix[1:size[0]+1,1:size[1]+1] = np.array(image_array)
	return padded_matrix

def loadingImageFiles(path):
	return [ndimage.imread(path+"/"+filename, mode="RGB") for root, dirnames, filenames in os.walk(path) for filename in filenames]