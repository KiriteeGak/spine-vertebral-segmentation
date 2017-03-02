from PIL import Image, ImageChops
from utilities import *
from regionGrowing import RegionGrowing as rg
import numpy as np
import cv2
from scipy.misc import *
from scipy.ndimage.morphology import *

class preprocessingImage(object):
	def trimBlackBoxes(self, image_array, tol=0):
		trimmed_image = []
		image_array = np.array(map(list, zip(*image_array)))
		size = np.shape(image_array)
		for i in range(0,size[0]):
			if image_array[i].any() > tol:
				trimmed_image.append(image_array[i])
		trimmed_image = map(list, zip(*trimmed_image))
		return trimmed_image

	def rgbToGrayscaleConversion(self, image_nd_array):
		images_grayscale = []
		for i, each_array in enumerate(image_nd_array):
			grayscaled_image = []
			for col in each_array:
				grayscaled_image.append([self.weightedAverageGrayscaleConv(row) for row in col])
			images_grayscale.append(grayscaled_image)
		return images_grayscale

	def weightedAverageGrayscaleConv(self, pixel):
		return int(0.299*pixel[0] + 0.587*pixel[1] + 0.114*pixel[2])
		
	def trimmedToBinary(self, image_array):
		image_array = np.array(map(list, zip(*image_array)))
		bi_image = []
		for col in image_array:
			bi_image.append([1 if pix > np.median(col) else 0 for pix in col])
		bi_image = binary_erosion(np.array(map(list, zip(*bi_image))))
		return bi_image

	def grayscaleToBinaryConversion(self, image_nd_array):
		binary_converted_images = []
		for image in image_nd_array:
			im = self.trimBlackBoxes(image)
			rg().regionGrowing(im,[[1,10],[20,30],[40,80],[100,100],[80,100]])\
			binary_converted_images.append(self.trimmedToBinary(im))
		return binary_converted_images

class selectingPointRepresentation(object):
	def __init__(self, image_nd_array):
		self.image_nd_array = image_nd_array

	def weightingTheImage(self, image_nd_array):
		for row in image_nd_array:
			weighted_row = self.localWeighting(row) + self.rowGlobalWeighting(row)
		pass

	def localWeighting(self, row, neighbors = 10):
		paddedRow = list(np.zeros(neighbors))+row+list(np.zeros(neighbors))
		return [np.mean(np.array(paddedRow[neighbors+i,2*neighbors+i])) for i,val in enumerate(row)]

	def rowGlobalWeighting(self, row):
		slope = 2/len(row)
		return [abs((len(row)/2)-i)*slope for i,pixel in enumerate(row)]
			
	def bestRowSelection(self, listOfRows):
		pass
