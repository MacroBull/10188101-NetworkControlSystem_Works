# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pid_tb_ui.ui'
#
# Created by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	def _fromUtf8(s):
		return s

try:
	_encoding = QtGui.QApplication.UnicodeUTF8
	def _translate(context, text, disambig):
		return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
	def _translate(context, text, disambig):
		return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
	def setupUi(self, Form):
		Form.setObjectName(_fromUtf8("Form"))
		Form.resize(648, 480)
		self.verticalLayout = QtGui.QVBoxLayout(Form)
		self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
		self.horizontalLayout_2 = QtGui.QHBoxLayout()
		self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
		self.mplwidget = MatplotlibWidget(Form)
		self.mplwidget.setObjectName(_fromUtf8("mplwidget"))
		self.horizontalLayout_2.addWidget(self.mplwidget)
		self.groupBox = QtGui.QGroupBox(Form)
		self.groupBox.setStyleSheet(_fromUtf8("QGroupBox { \n"
"     border: 2px solid gray; \n"
"     border-radius: 3px; \n"
" } \n"
"\n"
"QGroupBox::title {\n"
"	color:rgb(255,255,255);\n"
"}"))
		self.groupBox.setObjectName(_fromUtf8("groupBox"))
		self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
		self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
		self.horizontalLayout_3 = QtGui.QHBoxLayout()
		self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
		self.input_Kp = KDoubleNumInput(self.groupBox)
		self.input_Kp.setProperty("value", 0.2)
		self.input_Kp.setMinimum(-10.0)
		self.input_Kp.setMaximum(10.0)
		self.input_Kp.setObjectName(_fromUtf8("input_Kp"))
		self.horizontalLayout_3.addWidget(self.input_Kp)
		self.verticalLayout_2.addLayout(self.horizontalLayout_3)
		self.horizontalLayout_4 = QtGui.QHBoxLayout()
		self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
		self.input_Ki = KDoubleNumInput(self.groupBox)
		self.input_Ki.setProperty("value", 0.3)
		self.input_Ki.setMinimum(-10.0)
		self.input_Ki.setMaximum(10.0)
		self.input_Ki.setObjectName(_fromUtf8("input_Ki"))
		self.horizontalLayout_4.addWidget(self.input_Ki)
		self.verticalLayout_2.addLayout(self.horizontalLayout_4)
		self.horizontalLayout_5 = QtGui.QHBoxLayout()
		self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
		self.input_Kd = KDoubleNumInput(self.groupBox)
		self.input_Kd.setProperty("value", 0.1)
		self.input_Kd.setMinimum(-10.0)
		self.input_Kd.setMaximum(10.0)
		self.input_Kd.setObjectName(_fromUtf8("input_Kd"))
		self.horizontalLayout_5.addWidget(self.input_Kd)
		self.verticalLayout_2.addLayout(self.horizontalLayout_5)
		self.c_bypass = QtGui.QCheckBox(self.groupBox)
		self.c_bypass.setChecked(False)
		self.c_bypass.setObjectName(_fromUtf8("c_bypass"))
		self.verticalLayout_2.addWidget(self.c_bypass)
		self.horizontalLayout_2.addWidget(self.groupBox)
		self.verticalLayout.addLayout(self.horizontalLayout_2)
		self.horizontalLayout = QtGui.QHBoxLayout()
		self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
		self.horizontalSlider = QtGui.QSlider(Form)
		self.horizontalSlider.setMinimum(-100)
		self.horizontalSlider.setMaximum(100)
		self.horizontalSlider.setSingleStep(1)
		self.horizontalSlider.setPageStep(10)
		self.horizontalSlider.setTracking(True)
		self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
		self.horizontalSlider.setTickPosition(QtGui.QSlider.NoTicks)
		self.horizontalSlider.setTickInterval(20)
		self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
		self.horizontalLayout.addWidget(self.horizontalSlider)
		self.kdoublenuminput = KDoubleNumInput(Form)
		self.kdoublenuminput.setMinimum(-100.0)
		self.kdoublenuminput.setMaximum(100.0)
		self.kdoublenuminput.setSingleStep(1.0)
		self.kdoublenuminput.setDecimals(0)
		self.kdoublenuminput.setObjectName(_fromUtf8("kdoublenuminput"))
		self.horizontalLayout.addWidget(self.kdoublenuminput)
		self.horizontalLayout.setStretch(0, 1)
		self.verticalLayout.addLayout(self.horizontalLayout)
		self.horizontalLayout_6 = QtGui.QHBoxLayout()
		self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
		self.label_3 = QtGui.QLabel(Form)
		self.label_3.setObjectName(_fromUtf8("label_3"))
		self.horizontalLayout_6.addWidget(self.label_3)
		self.e_polyA = QtGui.QLineEdit(Form)
		self.e_polyA.setObjectName(_fromUtf8("e_polyA"))
		self.horizontalLayout_6.addWidget(self.e_polyA)
		self.label_4 = QtGui.QLabel(Form)
		self.label_4.setObjectName(_fromUtf8("label_4"))
		self.horizontalLayout_6.addWidget(self.label_4)
		self.e_polyB = QtGui.QLineEdit(Form)
		self.e_polyB.setObjectName(_fromUtf8("e_polyB"))
		self.horizontalLayout_6.addWidget(self.e_polyB)
		self.label_2 = QtGui.QLabel(Form)
		self.label_2.setObjectName(_fromUtf8("label_2"))
		self.horizontalLayout_6.addWidget(self.label_2)
		self.kdoublenuminput_2 = KDoubleNumInput(Form)
		self.kdoublenuminput_2.setProperty("value", 5.0)
		self.kdoublenuminput_2.setMinimum(1.0)
		self.kdoublenuminput_2.setMaximum(30.0)
		self.kdoublenuminput_2.setSingleStep(1.0)
		self.kdoublenuminput_2.setDecimals(0)
		self.kdoublenuminput_2.setObjectName(_fromUtf8("kdoublenuminput_2"))
		self.horizontalLayout_6.addWidget(self.kdoublenuminput_2)
		self.verticalLayout.addLayout(self.horizontalLayout_6)
		self.horizontalLayout_8 = QtGui.QHBoxLayout()
		self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
		self.label = QtGui.QLabel(Form)
		self.label.setObjectName(_fromUtf8("label"))
		self.horizontalLayout_8.addWidget(self.label)
		self.l_exp = QtGui.QLabel(Form)
		self.l_exp.setText(_fromUtf8(""))
		self.l_exp.setObjectName(_fromUtf8("l_exp"))
		self.horizontalLayout_8.addWidget(self.l_exp)
		self.horizontalLayout_8.setStretch(1, 1)
		self.verticalLayout.addLayout(self.horizontalLayout_8)

		self.retranslateUi(Form)
		QtCore.QMetaObject.connectSlotsByName(Form)

	def retranslateUi(self, Form):
		Form.setWindowTitle(_translate("Form", "PID demo", None))
		self.groupBox.setTitle(_translate("Form", "PID params", None))
		self.input_Kp.setLabel(_translate("Form", "Kp", None))
		self.input_Ki.setLabel(_translate("Form", "Ki", None))
		self.input_Kd.setLabel(_translate("Form", "Kd", None))
		self.c_bypass.setText(_translate("Form", "Bypass", None))
		self.kdoublenuminput.setLabel(_translate("Form", "Input", None))
		self.label_3.setText(_translate("Form", "a=", None))
		self.e_polyA.setText(_translate("Form", "1,0", None))
		self.label_4.setText(_translate("Form", "b=", None))
		self.e_polyB.setText(_translate("Form", "1,1", None))
		self.label_2.setText(_translate("Form", "T=", None))
		self.label.setText(_translate("Form", "Target system:", None))

from matplotlibwidget import MatplotlibWidget
from PyKDE4.kdeui import KDoubleNumInput
