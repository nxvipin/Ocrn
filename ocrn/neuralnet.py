from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer

class neuralnet:
	def __init__(self, *args):
		if len(args) >=2 :
			self.nnet = buildNetwork(*args)
			self.inputdimension = args[0]
			self.outputdimension = args[len(args)-1]
			self.nnet.sortModules()
			
			print self.nnet
		else:
			print "Number of layers must be more than two\n"

	def loadTrainingData(self, trainingdataset):
		if trainingdataset.getDimension('input') == self.inputdimension and \
			trainingdataset.getDimension('target') == self.outputdimension:
				self.trainer = BackpropTrainer(self.nnet, trainingdataset)
				return 1
		else:
			print "Dataset & Network size mismatch"
			return 0

	def teach(self, repeat):
		for i in range (1, repeat+1):
			print self.trainer.train()

