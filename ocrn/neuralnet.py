from pybrain.tools.shortcuts import buildNetwork
import dataset

class neuralnet:
	def __init__(self, *args):
		if len(args) >=2 :
			self.nnet = buildNetwork(*args)
			self.inputlayer = args[0]
			self.outputlayer = args[len(args)-1]
			self.nnet.sortModules()
			
			print self.nnet
		else:
			print "Number of layers must be more than two\n"

