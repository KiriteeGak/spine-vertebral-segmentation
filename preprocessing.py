import numpy as np
from PIL import Image, ImageChops

class preprocessingImage(object):
	def __init__(self, image_nd_array):
		self.image_nd_array = image_nd_array

	def trimBlackBoxes(self, image_array):
		bg = Image.new(image_array.mode, image_array.size, image_array.getpixel((0,0)))
		diff = ImageChops.difference(image_array, bg)
		diff = ImageChops.add(diff, diff, 2.0, -100)
		bbox = diff.getbbox()
		if bbox:
			return image_array.crop(bbox)

	def removeBlackBoxes(self, image_nd_array):
		return [self._trimBlackBoxes(each_array) for each_array in image_nd_array]

	def rgbToGrayscaleConversion(self, image_nd_array):
		imagesInGrayScale = []
		for i, each_array in enumerate(image_nd_array):
			grayscaled_image = []
			for pixel in each_array:
				for row in pixel:
					grayscaled_image.append([self.weightedAverageGrayscaleConv(pixel) for pixel in row])
			imagesInGrayScale.append(grayscaled_image)
		return imagesInGrayScale

	def weightedAverageGrayscaleConv(self, pixel):
		return np.floor(0.299*pixel[0] + 0.587*pixel[1] + 0.114*pixel[2])

	def padImages(self, image_array):
		imageSize = np.shape(image_array)
		padded_matrix = np.zeros(size[0]+2,size[1]+2)
		padded_matrix[1:size[0],1:size[1]] = image_array
		return padded_matrix
		
	def grayscaleToBinaryConversion(self, image_nd_array):
		binary_converted_images = []
		for image in image_nd_array:
			size = np.shape(image)
			im = self._padImages(image)
			binary_image = np.zeros(size)
			for i in range(1,size[0]+1):
				for j in range(1,size[1]+1):
					list_of_pixels = [im[i-1,j-1],im[i-1,j],im[i-1,j+1],im[i,j-1],im[i,j+1],im[i+1,j-1],im[i+1,j],im[i+1,j+1]]
					binary_image[i,j] = np.median(np.sort(list_of_pixels))
			binary_converted_images.append(binary_image)
		return binary_converted_images

	def mainCallerProcessor(self, image_nd_array):
		pass

class selectingPointRepresentation(object):
	def __init__(self, image_nd_array):
		self.image_nd_array = image_nd_array

	def weightingTheImage(self, image_nd_array):
		pass

	def bestRowSelection(self, listOfRows):
		pass
