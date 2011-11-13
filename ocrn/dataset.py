from pybrain.datasets import SupervisedDataSet
import numpy as np
import feature as ft
import fileinput

class dataset:
	# Initialize the dataset with input and label size
	def __init__(self, inputsize, labelsize):
		self.inputsize = inputsize
		self.labelsize = labelsize
		self.DS = SupervisedDataSet(self.inputsize, self.labelsize)
	
	# Adds data to existing training dataset
	def addTrainingData(self,inputdata, labeldata):
		try:
			if inputdata.size == self.inputsize and labeldata.size == self.labelsize:
				self.DS.appendLinked(inputdata, labeldata)
				return 1
		except AttributeError:
			print "Input error."
			return 0
	
	def getTrainingDataset(self):
		return self.DS
	
	def generateDataSet(self):
		for line in fileinput.input(['data/inputdata']):
			x = line.split(':')
			self.addTrainingData(ft.feature.getImageFeatureVector(x[0]),np.array([int(x[1])]))
		return 1
