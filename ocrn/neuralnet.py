from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer

class neuralnet:
	def __init__(self, *args):
		if len(args) >=2 :
			self.nnet = buildNetwork(*args)
			self.inputdimension = args[0]
			self.outputdimension = args[len(args)-1]
			self.nnet.sortModules()
		else:
			print "Number of layers must be greater than or equal to two\n"

	# Loads the training data into neural network before training.
	def loadTrainingData(self, trainingdataset):
		if trainingdataset.getDimension('input') == self.inputdimension and \
			trainingdataset.getDimension('target') == self.outputdimension:
				self.trainer = BackpropTrainer(self.nnet, trainingdataset)
				return 1
		else:
			print "Dataset-Network size mismatch\n"
			return 0

	# Train the neural network 'n' times with loaded training data.
	def teach(self, n):
		for i in range (1, n+1):
			print str(i) + " : " + str(self.trainer.train())

	# Activate the Neural Network with test data. Returns calculated output.
	def activate(self, testdata):
		if testdata.size == self.inputdimension:
			x = self.nnet.activate(testdata)
			return int(round(x[0],0))
		else:
			print "Test data error\n"
			return 0


