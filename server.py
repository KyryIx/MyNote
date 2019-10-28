# https://wiki.python.org.br/SocketBasico
# https://docs.python.org/2/library/socket.html
# https://docs.python.org/3/library/socket.html#socket.socket
# https://docs.python.org/3/library/socket.html#constants
# https://docs.python.org/3/library/socket.html#socket.socket.bind
# https://docs.python.org/3/library/socket.html#socket.socket.listen
# https://docs.python.org/3/library/socket.html#socket.socket.accept
# https://docs.python.org/3/library/socket.html#socket.socket.recv
# https://docs.python.org/3/library/socket.html#socket.close
# https://docs.python.org/3/library/stdtypes.html#bytes.decode
# https://docs.python.org/3/library/string.html
# https://docs.python.org/3/library/stdtypes.html#str.splitlines
# https://docs.python.org/3/library/stdtypes.html#str.split
# https://docs.python.org/3.8/tutorial/datastructures.html#dictionaries
# https://doc.qt.io/qtforpython/PySide2/QtWidgets/
# https://doc.qt.io/qtforpython/PySide2/QtWidgets/QApplication.html
# https://doc.qt.io/qtforpython/PySide2/QtWidgets/QWidget.html
# https://doc.qt.io/qtforpython/PySide2/QtWidgets/QWidget.html#PySide2.QtWidgets.PySide2.QtWidgets.QWidget.setWindowTitle
# https://doc.qt.io/qtforpython/PySide2/QtWidgets/QTextEdit.html

import socket
import sys
from PySide2 import QtCore, QtWidgets, QtGui

def getValues( msg ):
	text = msg.decode( "utf-8" )
	array = text.splitlines()
	values  = {}
	values['Text'] = array[0][:-18]
	array   = array[1:]
	for value in array:
		txt = value[:-1]
		tmp = txt.split( '=' )
		values[tmp[0]] = tmp[1]
	return values

class MyNote( QtWidgets.QWidget ):
	def __init__(self):
		super().__init__()
		self.layout = QtWidgets.QVBoxLayout()
		self.text   = QtWidgets.QTextEdit()
		self.setLayout(self.layout)
		self.layout.addWidget(self.text)
	
	def setTitle(self, title):
		super().setWindowTitle( title )
	
	def setContent(self, font='Arial', text='', color=[255,0,0]):
		self.text.setCurrentFont( QtGui.QFont( font ) )
		self.text.setTextColor( QtGui.QColor(color[0], color[1], color[2]) )
		self.text.setText( text )

def myApp():
	app    = QtWidgets.QApplication([])
	widget = MyNote()
	values = getValues( msg )
	widget.resize( int(values['Width']), int(values['Height']) )
	widget.setTitle( values['From'] + '/' + values['SentBy'] + ' - ' + values['SZTITLE'] )
	widget.setContent( font='Arial', text=values['Text'], color=[255,0,0] )
	widget.show()
	app.exec_()
	#sys.exit(app.exec_())

HOST = '192.168.1.103'
PORT = [39681, 34249][0]

tcp = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
tcp.bind( ( HOST, PORT ) )
tcp.listen( 1 )
while True:
	con, cliente = tcp.accept()
	#print( 'Conectado por', cliente )
	while True:
		msg = con.recv( 1024 )
		if not msg:
			break
		#print( cliente, msg )
		myApp()
	#print( 'Finalizando conexao do cliente', cliente )
	con.close()