# -*- coding: utf-8 -*-
"""
Created on Sat Jul 19 19:12:33 2014
Project	:SNCS?
Version	:0.0.1
@author	:macrobull

"""


class CPIDController():

	def __init__(self):
		self.u = 0.
		self.reset()

	def setPID(self, Kp, Ki, Kd):
		self.Kp, self.Ki, self.Kd = Kp, Ki, Kd

	def reset(self):
		self.ts = 0.05
		self.pError, self.iError, self.dError = 0., 0., 0.

	def regulate(self, e):
		self.dError = e - self.pError
		self.iError += e
		self.pError = e
		u = self.Kp * self.pError + self.Ki * self.iError + self.Kd * self.dError
		return u if abs(u)<70 else 70 if (u>0) else -70


if __name__ == "__main__":
	ctlr = CPIDController()
	ctlr.setPID(1,1e-3, 10)
	inp = [0] + [1] * 20

	out = []
	for i in inp:
		out.append(ctlr.regulate(i))

	from pylab import *
	plot(inp)
	plot(out)
	show()

