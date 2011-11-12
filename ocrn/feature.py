import Image as im
import numpy as np

class feature:
	#Return a 10X10 array from a monochrome BMP Image
	@staticmethod
	def getImageArray(imagepath):
		try:
			image = im.open(imagepath)
			imagearray=np.asarray(image.crop(image.getbbox()).resize((10,10))).astype(float)
			return imagearray
		except IOError:
			print "File Not Found"
			return np.zeros((10,10))
	
	# Normalizes a 2D array cell.
	@staticmethod
	def normalizeArrayCell( array, x, y):
		for c in range(1,5):
			for i in range(x-c,x+c+1):
				for j in range(y-c, y+c+1):
					if i<=9 and i>=0 and j<=9 and j>=0:
						if array[i,j] < array[x,y] and array[i,j] < array[x,y]-0.2*c:
							array[i,j]=array[x,y]-0.2*c
	
	# Returns a Normalized 2D Array from an Input Array. 
	# normalizeArrayCell is called for all non zero cells
	@staticmethod
	def getNormalizedArray( imagearray):
		nonzerocells = np.transpose(imagearray.nonzero())
		for i in range (0, nonzerocells.shape[0]):
			feature.normalizeArrayCell(imagearray, nonzerocells[i][0],nonzerocells[i][1])
		return imagearray
	
	# Returns Normalized 2D array from an Image
	@staticmethod
	def getNormalizedImageArray( imagepath):
		return feature.getNormalizedArray(feature.getImageArray(imagepath))
	
	# Returns Feature Vector of an Image
	@staticmethod
	def getImageFeatureVector( imagepath):
		array = feature.getNormalizedImageArray(imagepath)
		vector = np.resize(array,(1,100))
		return vector[0]


