from ocrn import dataset as ds
from ocrn import feature as ft
from ocrn import neuralnet as nt
import numpy as np

print "Ocrn: Optical Character Recognition using Neural Network\nLatest version available at http://github.com/swvist\n"

n = nt.neuralnet(100,80,1)
print "Neural Network Initialized"

d = ds.dataset(100,1)
print "Training Data Set Initialized"

if d.generateDataSet():
	print "Training Data Set Generated"

if n.loadTrainingData(d.getTrainingDataset()):
	print "Training Data Set loaded"

while(True):
	x = raw_input("q: quit \t t: teach \t e: test \nWhat?\t:\t")
	if x == "q":
		break
	elif x == "t":
		t = int(raw_input("How many times?\t:\t"))
		n.teach(t)
	elif x == "e":
		e = raw_input("Enter input file\t:\t")
		x = n.activate(ft.feature.getImageFeatureVector(e))
		print "\nThere is a high probability that the image is '"+str(unichr(x))+"'\n"
	else:
		print "Invalid option\n"
