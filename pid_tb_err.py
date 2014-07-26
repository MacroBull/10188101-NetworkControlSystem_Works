# -*- coding: utf-8 -*-


from pid_tb_ui import *
import numpy as np
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
		self.sp = self.mplwidget.figure.add_subplot(111)#, title="PID demo")

		self.pid = CPIDController()
		self.updatePID()
		self.updateBlock = False

		self.input_Kp.valueChanged.connect(self.updatePID)
		self.input_Ki.valueChanged.connect(self.updatePID)
		self.input_Kd.valueChanged.connect(self.updatePID)

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
			out = self.pid.regulate(value - self.oup[-self.kdoublenuminput_2.value()])
			self.inp = np.concatenate([self.inp[1:], [value]])
			self.oup = np.concatenate([self.oup[1:], [out]])
			self.sp.plot(self.inp, label = "input")
			self.sp.hold(True)
			self.sp.plot(self.oup, label = "output")
			self.sp.legend(loc="best")
			self.mplwidget.draw()
			self.sp.hold(False)

			self.updateBlock = tToBlock
			print value, out



if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	Form = QtGui.QWidget()
	ui = MainForm()
	ui.setupUi(Form)
	Form.show()
	sys.exit(app.exec_())

