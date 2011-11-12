from pybrain.datasets import SupervisedDataSet
import numpy as np
import feature as fr

class dataset:
	def __init__(self, inputsize, labelsize):
		self.inputsize = inputsize
		self.labelsize = labelsize
		self.DS = SupervisedDataSet(self.inputsize, self.labelsize)
	
	def addData(self,inputdata, labeldata):
		try:
			if inputdata.size == self.inputsize and labeldata.size == self.labelsize:
				self.DS.appendLinked(inputdata, labeldata)
				return 1
		except AttributeError:
			print "Input error."
			return 0
