'''
This code was the research presented in my masters thesis
The main idea behind this rewriting is to not make someone build something from scratch and 
if this is found useful and additions to make this better are always welcome

Contributors : Kiritee.GAK

Loading >> Preprocessing
Finding the vertebrae and eliminating FP
Finding orientation of vertebrae in space for predicting next missing vertebrae
contributors, if any, can use the same casing in naming for proper flow 
function naming in camelcasing and variable with underscore

dumps:
> N-D Array dumps for actual images/Grayscaled/Binary are present in dumps folder
'''

from utilities import *
from preprocessing import preprocessingImage as ppi
from preprocessing import selectingPointRepresentation as spr
from scipy import misc, ndimage
import os, glob, cPickle
import numpy as np
 
def loading_images(path):
	return [ndimage.imread(path+"/"+filename, mode="RGB") for root, dirnames, filenames in os.walk(path) for filename in filenames]

def point_representation_vertebra():
	pass

def region_growing(image, point, thershold):
	pass

def main(loaded_images):
	pass
	
if __name__ == '__main__':
	main(loadFromPickle("binaryT1eroded"))