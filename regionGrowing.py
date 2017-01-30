def regionGrowing(image_array, seed_point, threshold = 0.3, iterations = 50):
	default_strength = 1
	size = np.shape(image_array)
	dummy_image = np.zeros(np.shape(image_array))

	for s in seed_point:
		image_array[s[0],s[1]] = 1
	
	for ite in range(0,iterations):
		tdi = np.zeros(size[0]+2,size[1]+2) # tdi - temp dummy image
		for i in range(0, size[0]):
			for j in range(0, size[1]):
				if dummy_image[i,j] != 1:
					tdi = neighborhoodWeighting([i,j], image_array, dummy_image, temp_dummy_image)
		dummy_image = tdi[1:size[0],1:size[1]]
	pass

def strengthCal(dat1, dat2, stre):
	return stre*float(1-(abs(dat1-dat2)/max(dat1,dat2)))

def neighborhoodWeighting(coord, real_image, dummy_image, temp_dummy_image):
	[c1,c2] = coord
	for i in range(-1,2,1):
		for j in range(-1,2,1):
			if not [i,j] == [1,1]:
				temp_dummy_image[i+1+i,j+1+i] = max(dummy_image[c1-1+i,c2-1+j],strengthCal(real_image[c1-1+i,c2-1+j],real_image[c1+i,c2+j],dummy_image[c1+i,c2+j]))
	return temp_dummy_image