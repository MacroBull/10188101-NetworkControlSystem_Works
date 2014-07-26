# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bpnc_tb_ui.ui'
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
		self.verticalLayout_3 = QtGui.QVBoxLayout()
		self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
		spacerItem = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Minimum)
		self.verticalLayout_3.addItem(spacerItem)
		self.i_depth = KIntNumInput(self.groupBox)
		self.i_depth.setProperty("value", 3)
		self.i_depth.setMinimum(3)
		self.i_depth.setMaximum(6)
		self.i_depth.setObjectName(_fromUtf8("i_depth"))
		self.verticalLayout_3.addWidget(self.i_depth)
		self.i_inpLen = KIntNumInput(self.groupBox)
		self.i_inpLen.setProperty("value", 2)
		self.i_inpLen.setMinimum(0)
		self.i_inpLen.setMaximum(10)
		self.i_inpLen.setObjectName(_fromUtf8("i_inpLen"))
		self.verticalLayout_3.addWidget(self.i_inpLen)
		self.i_outLen = KIntNumInput(self.groupBox)
		self.i_outLen.setProperty("value", 0)
		self.i_outLen.setMinimum(0)
		self.i_outLen.setMaximum(10)
		self.i_outLen.setObjectName(_fromUtf8("i_outLen"))
		self.verticalLayout_3.addWidget(self.i_outLen)
		self.b_init = QtGui.QPushButton(self.groupBox)
		self.b_init.setObjectName(_fromUtf8("b_init"))
		self.verticalLayout_3.addWidget(self.b_init)
		spacerItem1 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Minimum)
		self.verticalLayout_3.addItem(spacerItem1)
		self.i_epochs = KIntNumInput(self.groupBox)
		self.i_epochs.setProperty("value", 500)
		self.i_epochs.setMinimum(10)
		self.i_epochs.setMaximum(10000)
		self.i_epochs.setSingleStep(10)
		self.i_epochs.setObjectName(_fromUtf8("i_epochs"))
		self.verticalLayout_3.addWidget(self.i_epochs)
		self.b_train = QtGui.QPushButton(self.groupBox)
		self.b_train.setObjectName(_fromUtf8("b_train"))
		self.verticalLayout_3.addWidget(self.b_train)
		spacerItem2 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Minimum)
		self.verticalLayout_3.addItem(spacerItem2)
		self.c_train = QtGui.QCheckBox(self.groupBox)
		self.c_train.setChecked(True)
		self.c_train.setObjectName(_fromUtf8("c_train"))
		self.verticalLayout_3.addWidget(self.c_train)
		self.verticalLayout_3.setStretch(4, 1)
		self.verticalLayout_3.setStretch(7, 1)
		self.verticalLayout_2.addLayout(self.verticalLayout_3)
		self.horizontalLayout_2.addWidget(self.groupBox)
		self.verticalLayout.addLayout(self.horizontalLayout_2)
		self.horizontalLayout = QtGui.QHBoxLayout()
		self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
		self.horizontalSlider = QtGui.QSlider(Form)
		self.horizontalSlider.setAutoFillBackground(False)
		self.horizontalSlider.setMinimum(-100)
		self.horizontalSlider.setMaximum(100)
		self.horizontalSlider.setSingleStep(1)
		self.horizontalSlider.setPageStep(10)
		self.horizontalSlider.setSliderPosition(0)
		self.horizontalSlider.setTracking(True)
		self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
		self.horizontalSlider.setInvertedAppearance(False)
		self.horizontalSlider.setInvertedControls(False)
		self.horizontalSlider.setTickPosition(QtGui.QSlider.TicksAbove)
		self.horizontalSlider.setTickInterval(10)
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
		self.kdoublenuminput_2.setProperty("value", 1.0)
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
		self.l_stat = QtGui.QLabel(Form)
		self.l_stat.setObjectName(_fromUtf8("l_stat"))
		self.horizontalLayout_8.addWidget(self.l_stat)
		self.horizontalLayout_8.setStretch(1, 1)
		self.verticalLayout.addLayout(self.horizontalLayout_8)

		self.retranslateUi(Form)
		QtCore.QMetaObject.connectSlotsByName(Form)

	def retranslateUi(self, Form):
		Form.setWindowTitle(_translate("Form", "BP Neural Network Controller demo", None))
		self.groupBox.setTitle(_translate("Form", "Neural network params", None))
		self.i_depth.setLabel(_translate("Form", "Network depth", None))
		self.i_inpLen.setLabel(_translate("Form", "Including inputs", None))
		self.i_outLen.setLabel(_translate("Form", "Including outputs", None))
		self.b_init.setText(_translate("Form", "Initial network", None))
		self.i_epochs.setLabel(_translate("Form", "Trainning epochs", None))
		self.b_train.setText(_translate("Form", "Train", None))
		self.c_train.setText(_translate("Form", "Current as dataset", None))
		self.kdoublenuminput.setLabel(_translate("Form", "Input", None))
		self.label_3.setText(_translate("Form", "a=", None))
		self.e_polyA.setText(_translate("Form", "1,0", None))
		self.label_4.setText(_translate("Form", "b=", None))
		self.e_polyB.setText(_translate("Form", "1,1", None))
		self.label_2.setText(_translate("Form", "T=", None))
		self.label.setText(_translate("Form", "Target system:", None))
		self.l_stat.setText(_translate("Form", "Please train first.", None))

from matplotlibwidget import MatplotlibWidget
from PyKDE4.kdeui import KIntNumInput, KDoubleNumInput
