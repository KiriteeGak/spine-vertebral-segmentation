from utilities import *
from preprocessing import preprocessingImage as ppi
from preprocessing import selectingPointRepresentation as spr
from scipy import misc, ndimage
import os, glob, cPickle
import numpy as np
from matplotlib import pyplot as plt

# Clustering kmeans
# 

def main():
	# images = ppi().rgbToGrayscaleConversion(loaded_images)
	# dumpAsPickle("trimmedGrayscaledT1",[ppi().trimBlackBoxes(image) for image in loaded_images])
	# sample = ndimage.imread("resources/t1 images/IMG-0007-00007.jpg", mode="RGB")
	# trimGrayscale = ppi().trimBlackBoxes(ppi().rgbToGrayscaleConversion([sample])[0])
	# plt.imshow(trimGrayscale)
	# plt.show()
	weighted = spr()._weightingTheImage(trimGrayscale)


	
if __name__ == '__main__':
	main()