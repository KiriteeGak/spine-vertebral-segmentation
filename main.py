from utilities import *
from preprocessing import preprocessingImage as ppi
from preprocessing import selectingPointRepresentation as spr
from scipy import misc, ndimage
import os, glob, cPickle
import numpy as np
from matplotlib import pyplot as plt

def main():
	# images = ppi().rgbToGrayscaleConversion(loaded_images)
	# dumpAsPickle("trimmedGrayscaledT1",[ppi().trimBlackBoxes(image) for image in loaded_images])
	sample = ndimage.imread("resources/t1 images/IMG-0007-00007.jpg", mode="RGB")
	trimGrayscale = ppi().trimBlackBoxes(ppi().rgbToGrayscaleConversion([sample])[0])
	# plt.imshow(trimGrayscale)
	# plt.show()
	# exit()
	weighted = spr().weightingTheImage(trimGrayscale)
	for i,each in enumerate(weighted):
		if i == 55:
			plt.plot(each)
			plt.show()
	
if __name__ == '__main__':
	main()
	# main(loadFromPickle("binaryT1eroded"))
	# main(loadFromPickle("grayscaledT1"))
