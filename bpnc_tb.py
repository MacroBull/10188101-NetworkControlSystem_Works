# -*- coding: utf-8 -*-


from bpnc_tb_ui import *
import numpy as np
from macrobull.misc import exclusiveSplit

from bp_neural import bpNetController

pltLen = 60

class MainForm(Ui_Form):
	def setupUi(self, Form):
		super(MainForm, self).setupUi(Form)

		closeShort = QtGui.QShortcut(Form)
		closeShort.setKey("Esc")
		closeShort.activated.connect(Form.destroy)

		self.horizontalSlider.sliderReleased.connect(self.updatePlot)
		self.kdoublenuminput.valueChanged.connect(self.updatePlot)
		self.updateBlock = False

#		self.inp = np.zeros(pltLen)
#		self.oup = np.zeros(pltLen)
		self.inp = [0]*pltLen
		self.oup = [0]*pltLen
		self.cop = [0]*pltLen
		self.sp = self.mplwidget.figure.add_subplot(111)#, title="PID demo")

		self.bpnc = bpNetController()
		self.bpnc.enableDebug()

		self.b_init.clicked.connect(self.initialBP)
		self.b_train.clicked.connect(self.train)

		self.initialBP()


		self.e_polyA.editingFinished.connect(self.updateTrans)
		self.e_polyB.editingFinished.connect(self.updateTrans)
		self.updateTrans()


	def updateTrans(self):
		sa = self.e_polyA.text()
		sb = self.e_polyB.text()

		try:
			self.sysA = [float(p) for p in exclusiveSplit(sa)]
			self.sysB = [float(p) for p in exclusiveSplit(sb)]

			if self.sysA[0] == 0: raise ValueError("a[0] == 0")

			poly = str(self.sysA[0])+'y'

			for i,p in enumerate(self.sysA[1:]):
				if p !=0:
					if p>0:
						poly += '+{}y({})'.format(str(p), i+1)
					else:
						poly += '{}y({})'.format(str(p), i+1)

			poly += ' = '

			poly += str(self.sysB[0])+'x'

			for i,p in enumerate(self.sysB[1:]):
				if p !=0:
					if p>0:
						poly += '+{}x({})'.format(str(p), i+1)
					else:
						poly += '{}x({})'.format(str(p), i+1)

		except BaseException:
			self.e_polyA.setText(self.lastPolyA)
			self.e_polyB.setText(self.lastPolyB)
			QtGui.QMessageBox.about(None, "Error", "Invalid target system description")
		else:
			self.l_exp.setText( poly )
			self.lastPolyA = sa
			self.lastPolyB = sb

	def systemSim(self, inp, inps):
		y = self.sysB[0] * inp
		for i,p in enumerate(self.sysB[1:]):
			y += p* inps[-i-1]
		for i,p in enumerate(self.sysA[1:]):
			y -= p* self.oup[-i-1]
		return y / self.sysA[0]


	def updatePlot(self, *args):
		if args:
			value = args[0]
			self.horizontalSlider.setValue(int(round(value)))

		else:
			self.updateBlock = True
			value = self.horizontalSlider.value()
			self.kdoublenuminput.setValue(value)
			self.updateBlock = False

		tToBlock = False
		iLen = int(self.i_inpLen.value())
		oLen = int(self.i_outLen.value())
		delay = int(self.kdoublenuminput_2.value())
#		print -delay - iLen, -delay
		if not self.updateBlock:
			if self.c_train.checkState():
				out = self.systemSim(value, self.inp)
				self.bpnc.sample(self.oup[-delay - oLen:-delay]+self.inp[-delay - iLen:-delay], out, value)
				self.dscnt +=1
				self.l_stat.setText("Added {} samples in total".format(self.dscnt))
				print "input={}, \toutput={}".format(value, out)
			else:
#				out = (self.pid.regulate(value - self.oup[-self.kdoublenuminput_2.value()]))
				cout = self.bpnc.act(self.inp[-delay - oLen:-delay]+self.oup[-delay - iLen:-delay], value)[0]
				out = self.systemSim(cout, self.cop)
				print "input={}, \ttcontroller out={}, \toutput={}".format(value, cout, out)
				self.cop = self.cop[1:]+ [cout]

			self.inp = self.inp[1:]+ [value]
			self.oup = self.oup[1:]+ [out]
			self.sp.plot(self.inp, label = "input")
			self.sp.hold(True)
			self.sp.plot(self.oup, label = "output")
			self.sp.legend(loc="best")
			self.mplwidget.draw()
			self.sp.hold(False)

			self.updateBlock = tToBlock


	def initialBP(self):
		self.bpnc.setup(self.i_depth.value(), self.i_inpLen.value()+self.i_outLen.value())
		self.l_stat.setText("Please train first.")
		self.dscnt = 0

	def train(self):
		try:
			self.bpnc.train(self.i_epochs.value())
		except BaseException,e:
			self.l_stat.setText(e.message)
		else:
			self.l_stat.setText("Trained {} epochs in total".format(self.bpnc.curEpoch))



if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	Form = QtGui.QWidget()
	ui = MainForm()
	ui.setupUi(Form)
	Form.show()
	sys.exit(app.exec_())

