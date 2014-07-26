# -*- coding: utf-8 -*-


from tcp_client_ui import *
from threading import Thread

import time, socket

class sio(Thread):
	def setup(self, sock):
		self.sock = sock

	def run(self):
		self.running = True
		while self.running:
			try:
				r = self.sock.recv(1024)
				print "r=", r
			except BaseException:
				time.sleep(0.2)
			else:
				if r:
					self.dataReceived(r)
		self.sock.close()
		print "socket closed"

	def dataReceived(self, s):
		print "received", s



class MainForm(Ui_Form, QtCore.QObject):

	receivedSig = QtCore.pyqtSignal(str)

	def setupUi(self, Form):
		super(MainForm, self).setupUi(Form)

		self.form = Form
		self.b_connect.clicked.connect(self.connect)
		self.b_disconnect.clicked.connect(self.disconnect)
		self.b_close.clicked.connect(self.close)

		self.receivedSig.connect(self.received)


		sendShort = QtGui.QShortcut(Form)
		sendShort.setKey("Ctrl+Return")
		sendShort.activated.connect(self.send)


		self.sio = None


	def connect(self):
		try:
			host, port = str(self.e_target.text()).split(':')
			port = int(port)
			print "connect to", host, port
		except ValueError:
			QtGui.QMessageBox.about(None, "Error", "Server address format error.")
		else:
			self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.sock.settimeout(2)
			try:
				self.sock.connect((host, port))
				self.sio = sio()
				self.sio.setup(self.sock)
				self.sio.dataReceived = self.receivedSig.emit
				self.sio.start()
				self.messages = ""
				self.plainTextEdit.setEnabled(True)
				print "Sio started"
			except BaseException, e:
				QtGui.QMessageBox.about(None, "Error", e.args[1])



	def close(self):
		if self.sio:
			self.sio.running = False
			self.sio.join()
		self.form.destroy()

	def send(self):
		content = self.plainTextEdit.toPlainText()
		if content:
			if self.checkBox.isChecked():
				self.messages += content
				if self.checkBox_2.isChecked():
					self.textBrowser.setHtml(self.messages)
				else:
					self.textBrowser.setPlainText(self.messages)
			self.sock.send(content)

	def received(self, s):
		self.messages += s
		if self.checkBox_2.isChecked():
			self.textBrowser.setHtml(self.messages)
		else:
			self.textBrowser.setPlainText(self.messages)

	def disconnect(self):
		self.sio.running = False
		self.sio.join()
		self.sock.close()
		self.plainTextEdit.setEnabled(False)
		print "Sio closed"

if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	Form = QtGui.QWidget()
	ui = MainForm()
	ui.setupUi(Form)
	Form.show()
	sys.exit(app.exec_())

