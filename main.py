# This code was the research presented in my masters thesis
# The main idea behind sharing this is to not make someone build something from scratch
# Contributors : Kiritee.GAK

# Loading images from the folder.
# Preprocessing the images for evaluation
# Finding the vertebrae and eliminating FP
# Finding orientation of vertebrae in space for predicting next missing vertebrae
# contributors, if any, can use the same casing in naming for proper flow 
# function name in lower case and starting with an '_'(underscore) and variablew with merged word with caping in between

from preprocessing import preprocessingImage as ppi
from preprocessing import selectingPointRepresentation as spr
import os, glob, cPickle
import numpy as np
from scipy import misc, ndimage 

def loading_images(path):
	return [ndimage.imread(path+"/"+filename, mode="RGB") for root, dirnames, filenames in os.walk(path) for filename in filenames]

def dumpAsPickle(filename, toDump):
	with open("dumps/"+filename+".pkl", 'wb') as fid:
			cPickle.dump(toDump, fid)

def loadFromPickle(filename):
	with open("dumps/"+filename+".pkl", 'r') as fid:
		return cPickle.load(fid)

def point_representation_vertebra():
	pass

def region_growing(image, point, thershold):
	pass

def main(path):
	ppi(path).rgbToGrayscaleConversion(loadedImages)

if __name__ == '__main__':
	images_loaded = loadFromPickle("t1ImagesRaw")
	main(images_loaded)
	