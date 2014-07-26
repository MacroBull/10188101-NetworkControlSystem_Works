# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tcp_client_ui.ui'
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
		Form.resize(662, 528)
		self.verticalLayout = QtGui.QVBoxLayout(Form)
		self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
		self.horizontalLayout = QtGui.QHBoxLayout()
		self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
		self.verticalLayout_3 = QtGui.QVBoxLayout()
		self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
		self.horizontalLayout_6 = QtGui.QHBoxLayout()
		self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
		self.l_target = QtGui.QLabel(Form)
		self.l_target.setObjectName(_fromUtf8("l_target"))
		self.horizontalLayout_6.addWidget(self.l_target)
		self.e_target = QtGui.QLineEdit(Form)
		self.e_target.setObjectName(_fromUtf8("e_target"))
		self.horizontalLayout_6.addWidget(self.e_target)
		self.verticalLayout_3.addLayout(self.horizontalLayout_6)
		self.verticalLayout_7 = QtGui.QVBoxLayout()
		self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
		self.b_connect = QtGui.QPushButton(Form)
		self.b_connect.setObjectName(_fromUtf8("b_connect"))
		self.verticalLayout_7.addWidget(self.b_connect)
		self.b_disconnect = QtGui.QPushButton(Form)
		self.b_disconnect.setObjectName(_fromUtf8("b_disconnect"))
		self.verticalLayout_7.addWidget(self.b_disconnect)
		self.checkBox = QtGui.QCheckBox(Form)
		self.checkBox.setChecked(True)
		self.checkBox.setObjectName(_fromUtf8("checkBox"))
		self.verticalLayout_7.addWidget(self.checkBox)
		self.checkBox_2 = QtGui.QCheckBox(Form)
		self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
		self.verticalLayout_7.addWidget(self.checkBox_2)
		self.b_close = QtGui.QPushButton(Form)
		self.b_close.setObjectName(_fromUtf8("b_close"))
		self.verticalLayout_7.addWidget(self.b_close)
		self.verticalLayout_3.addLayout(self.verticalLayout_7)
		self.horizontalLayout.addLayout(self.verticalLayout_3)
		self.verticalLayout_2 = QtGui.QVBoxLayout()
		self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
		self.textBrowser = QtGui.QTextBrowser(Form)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(1)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
		self.textBrowser.setSizePolicy(sizePolicy)
		self.textBrowser.setAcceptRichText(False)
		self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
		self.verticalLayout_2.addWidget(self.textBrowser)
		self.plainTextEdit = QtGui.QPlainTextEdit(Form)
		self.plainTextEdit.setEnabled(False)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
		self.plainTextEdit.setSizePolicy(sizePolicy)
		self.plainTextEdit.setMinimumSize(QtCore.QSize(0, 150))
		self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
		self.verticalLayout_2.addWidget(self.plainTextEdit)
		self.verticalLayout_2.setStretch(0, 1)
		self.horizontalLayout.addLayout(self.verticalLayout_2)
		self.horizontalLayout.setStretch(1, 1)
		self.verticalLayout.addLayout(self.horizontalLayout)

		self.retranslateUi(Form)
		QtCore.QMetaObject.connectSlotsByName(Form)

	def retranslateUi(self, Form):
		Form.setWindowTitle(_translate("Form", "TCP Client", None))
		self.l_target.setText(_translate("Form", "Server", None))
		self.e_target.setText(_translate("Form", "localhost:8888", None))
		self.b_connect.setText(_translate("Form", "Connect", None))
		self.b_disconnect.setText(_translate("Form", "Disconnect", None))
		self.checkBox.setText(_translate("Form", "Local Echo", None))
		self.checkBox_2.setText(_translate("Form", "Html", None))
		self.b_close.setText(_translate("Form", "Close", None))
		self.plainTextEdit.setPlainText(_translate("Form", "Ctrl+Return to send.", None))

