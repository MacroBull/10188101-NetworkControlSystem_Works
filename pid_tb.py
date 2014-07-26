# -*- coding: utf-8 -*-


from pid_tb_ui import *
import numpy as np
from macrobull.misc import exclusiveSplit

from pid import CPIDController

pltLen = 60

class MainForm(Ui_Form):
	def setupUi(self, Form):
		super(MainForm, self).setupUi(Form)

		closeShort = QtGui.QShortcut(Form)
		closeShort.setKey("Esc")
		closeShort.activated.connect(Form.destroy)

#		self.horizontalSlider.releaseMouse.connect(d)
		self.horizontalSlider.sliderReleased.connect(self.updatePlot)
		self.kdoublenuminput.valueChanged.connect(self.updatePlot)

		self.inp = np.zeros(pltLen)
		self.oup = np.zeros(pltLen)
		self.cop = np.zeros(pltLen)
		self.sp = self.mplwidget.figure.add_subplot(111)#, title="PID demo")

		self.pid = CPIDController()
		self.updatePID()
		self.updateBlock = False

		self.input_Kp.valueChanged.connect(self.updatePID)
		self.input_Ki.valueChanged.connect(self.updatePID)
		self.input_Kd.valueChanged.connect(self.updatePID)

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


	def updatePID(self):
		self.pid.setPID(self.input_Kp.value(), self.input_Ki.value(), self.input_Kd.value())
		print self.pid.Kp, self.pid.Ki, self.pid.Kd

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
		if not self.updateBlock:
			if self.c_bypass.checkState():
				out = self.systemSim(value, self.inp)
			else:
#				out = (self.pid.regulate(value - self.oup[-self.kdoublenuminput_2.value()]))
				cout = self.pid.regulate(value - self.oup[-self.kdoublenuminput_2.value()])
				out = self.systemSim(cout, self.cop)
				print "input={}, \terror={}, \tPID output={}, \toutput={}".format(value, value - self.oup[-self.kdoublenuminput_2.value()], cout, out)
				self.cop = np.concatenate([self.cop[1:],[cout]])

			self.inp = np.concatenate([self.inp[1:], [value]])
			self.oup = np.concatenate([self.oup[1:], [out]])
			self.sp.plot(self.inp, label = "input")
			self.sp.hold(True)
			self.sp.plot(self.oup, label = "output")
			self.sp.legend(loc="best")
			self.mplwidget.draw()
			self.sp.hold(False)

			self.updateBlock = tToBlock



if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	Form = QtGui.QWidget()
	ui = MainForm()
	ui.setupUi(Form)
	Form.show()
	sys.exit(app.exec_())

