from utilities import *
from preprocessing import preprocessingImage as ppi
from preprocessing import selectingPointRepresentation as spr
from scipy import misc, ndimage
import os, glob, cPickle
import numpy as np
 
def main(loaded_images):
	ppi().rgbToGrayscaleConversion(loaded_images)
	ppi().grayscaleToBinaryConversion(loaded_images)
	pass
	
if __name__ == '__main__':
	main(loadFromPickle("binaryT1eroded"))
	main(loadFromPickle("grayscaledT1"))