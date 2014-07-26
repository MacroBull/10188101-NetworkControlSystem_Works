# -*- coding: utf-8 -*-
"""
Created on Sat Jul 26 21:24:52 2014
Project	:Python-Project
Version	:0.0.1
@author	:macrobull

"""


from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure.modules import TanhLayer



class bpNetController(object):
	def __init__(self, *args):
		self.debug = False
		self.setup(*args)

	def setup(self, depth = 4, refLen =5):
		self.inCnt = refLen + 1
		self.net = buildNetwork(self.inCnt, depth, 1, bias=True, hiddenclass=TanhLayer)
		self.ds = SupervisedDataSet(self.inCnt, 1)
		self.trainer = BackpropTrainer(self.net, self.ds)
		self.clear()

	def enableDebug(self):
		self.debug = True

	def sample(self, refs, inp, expectedOut):
		if self.debug: print "added {}".format([refs, inp, expectedOut])
		self.ds.addSample(refs+[inp], expectedOut)

	def train(self, epochs = 100):
		self.trainer.trainEpochs(epochs)

	def clear(self):
		self.ds.clear()

	def act(self, refs, inp):
		return self.net.activate(refs+[inp])

	@property
	def curEpoch(self):
		return self.trainer.epoch


if __name__ == "__main__":
	bpnc = bpNetController(4, 1)
	bpnc.sample([0],0, 0)
	bpnc.sample([1],0, 1)
	bpnc.sample([0],1, 1)
	bpnc.sample([1],1, 0)
	bpnc.train(2000)
	print bpnc.act([0],0), bpnc.act([0],1), bpnc.act([1],0), bpnc.act([1],1)
	print bpnc.curEpoch

