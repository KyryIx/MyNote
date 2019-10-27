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

HOST = '192.168.1.100'
PORT = [39681, 34249][0] # AS DUAS PORTAS FUNCIONAM

tcp = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
tcp.bind( ( HOST, PORT ) )
#tcp.bind( ( HOST, PORT ) )
tcp.listen( 1 )
app = QtWidgets.QApplication([])
while True:
	con, cliente = tcp.accept()
	#print( 'Conectado por', cliente )
	while True:
		msg = con.recv( 1024 )
		if not msg:
			break
		#print( cliente, msg )
		#print( msg )
		values = getValues( msg )
		widget = MyNote()
		widget.resize( int(values['Width']), int(values['Height']) )
		widget.setTitle( values['From'] + '/' + values['SentBy'] + ' - ' + values['SZTITLE'] )
		widget.setContent( font='Arial', text=values['Text'], color=[255,0,0] )
		widget.show()
		app.exec_()
		#sys.exit(app.exec_())
	#print( 'Finalizando conexao do cliente', cliente )
	con.close()

#msg = b'Everton, chega aiEnd of TCPIP text#\r\nFrom=Milton#\r\nSentBy=MTD-Milton#\r\nStayOnTop=Yes#\r\nHasBorder=Yes#\r\nBkColor=16711680#\r\nFoColor=16777215#\r\nTiBkColor=255#\r\nTiFoColor=16777215#\r\nX=1#\r\nY=1#\r\nWidth=500#\r\nHeight=150#\r\nSponsored=Yes#\r\nLFHEIGHT=-18#\r\nLFWIDTH=0#\r\nLFESCAPEME=0#\r\nLFORIENTAT=0#\r\nLFWEIGHT=400#\r\nLFITALIC=00#\r\nLFUNDERLIN=0#\r\nLFSTRIKEOU=0#\r\nLFCHARSET=0#\r\nLFOUTPRECI=3#\r\nLFCLIPPREC=2#\r\nLFQUALITY=1#\r\nLFPITCHAND=22#\r\nLFFACENAME=Times New Roman#\r\nLFHEIGHTTI=-13#\r\nLFWIDTHTI=0#\r\nLFESCAPETI=0#\r\nLFORIENTTI=0#\r\nLFWEIGHTTI=700#\r\nLFITALICTI=0#\r\nLFUNDERLTI=1#\r\nLFSTRIKETI=0#\r\nLFCHARSETI=0#\r\nLFOUTPRETI=3#\r\nLFCLIPPRTI=2#\r\nLFQUALITTI=1#\r\nLFPITCHTI=12#\r\nLFFACENATI=Calibri#\r\nSZTITLE=Estamos em teste ;)#\r\nALARMTIME=2019,10,27,1,50#\r\nRECURRINGALARMTYPE=5#\r\nRECURRINGALARMVALUE=10#\r\nROLLUP=#\r\n'
#

#values = getValues( msg )
#app = QtWidgets.QApplication([])
#widget = MyNote()
#widget.resize( int(values['Width']), int(values['Height']) )
#widget.setTitle( values['From'] + '/' + values['SentBy'] + ' - ' + values['SZTITLE'] )
#widget.setContent( font='Arial', text=values['Text'], color=[255,0,0] )
#widget.show()
#sys.exit(app.exec_())

#
## funciona!
#text = msg.decode( "utf-8" )
#array = text.splitlines()
#
#content = array[0][:-18]
#array   = array[1:]
#values  = {}
##print( "Conteudo:", content )
##print( array )
#
#
#for value in array:
#	txt = value[:-1]
#	tmp = txt.split( '=' )
#	values[tmp[0]] = tmp[1]
#	#print( tmp )
##print( values )
#
#
#
#
#class MyNote( QtWidgets.QWidget ):
#	def __init__(self):
#		super().__init__()
#		super().setWindowTitle( values['From'] + '/' + values['SentBy'] + ' - ' + values['SZTITLE'] )
#		
#		self.layout = QtWidgets.QVBoxLayout()
#		self.setLayout(self.layout)
#		
#		self.text = QtWidgets.QTextEdit()
#		self.text.setCurrentFont( QtGui.QFont( values['LFFACENAME'] ) )
#		fontColor = int(values['FoColor'])
#		fontColor_r = 255
#		fontColor_g = 50
#		fontColor_b = 50
#		self.text.setTextColor( QtGui.QColor(fontColor_r,fontColor_g,fontColor_b) )
#		self.text.setText( content )
#		self.layout.addWidget(self.text)
#
#if __name__ == "__main__":
#	app = QtWidgets.QApplication([])
#	
#	widget = MyNote()
#	widget.resize( int(values['Width']), int(values['Height']) )
#	widget.show()
#	
#	sys.exit(app.exec_())