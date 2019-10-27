# https://wiki.python.org.br/SocketBasico
# https://docs.python.org/3/library/socket.html
# https://docs.python.org/3/library/socket.html#socket.socket
# https://docs.python.org/3/library/socket.html#constants
# https://docs.python.org/3/library/socket.html#socket.socket.connect
# https://docs.python.org/3/library/functions.html#func-bytearray
# https://docs.python.org/3/library/stdtypes.html#binaryseq
# https://docs.python.org/3/library/socket.html#socket.socket.send
# https://docs.python.org/3/library/socket.html#socket.close

HOST = '192.168.1.100'
PORT = [39681, 34249][0]

vText                = b"Everton chatinho e legalzinho"
vFrom                = b"Desenvolvedor"
vSentBy              = b"ODYCRUZ-PC"
vStayOnTop           = b"Yes"                   #             (manter note no top): campo vazio (nao) ou Yes (sim)
vHasBorder           = b"Yes"                   #                  (borda no note): campo vazio (nao) ou Yes (sim)
vBkColor             = b"16711680"              #           (cor de fundo do note): R + G * 16^2 + B * 16^4 [255 (vermelho puro) / 65280=255*16^2 (verde puro) / 16711680=255*16^4 (azul puro)]
vFoColor             = b"16777215"              #           (cor da fonte do note): R + G * 16^2 + B * 16^4 [255 (vermelho puro) / 65280=255*16^2 (verde puro) / 16711680=255*16^4 (azul puro)]
vTiBkColor           = b"255"                   #         (cor de fundo do titulo): R + G * 16^2 + B * 16^4 [255 (vermelho puro) / 65280=255*16^2 (verde puro) / 16711680=255*16^4 (azul puro)]
vTiFoColor           = b"16777215"              #         (cor da fonte do titulo): R + G * 16^2 + B * 16^4 [255 (vermelho puro) / 65280=255*16^2 (verde puro) / 16711680=255*16^4 (azul puro)]
vX                   = b"1"					    #              (posicao X do note): de 1 ate o (largura do note - largura da tela) 
vY                   = b"1"					    #              (posicao Y do note): de 1 ate o (altura do note - altura da tela) 
vWidth               = b"500"                   #                (largura do note): de 1 ate a (largura da tela)-1
vHeight              = b"350"                   #                 (altura do note): de 1 ate a (altura da tela)-1
vSponsored           = b"Yes"                   #(exibir informacoes da TurboNote): campo vazio (nao) ou Yes (sim)
vLFHEIGHT            = b"-18"
vLFWIDTH             = b"0"
vLFESCAPEME          = b"0"
vLFORIENTAT          = b"0"
vLFWEIGHT            = b"400"
vLFITALIC            = b"0"
vLFUNDERLIN          = b"0"
vLFSTRIKEOU          = b"0"
vLFCHARSET           = b"0"
vLFOUTPRECI          = b"3"
vLFCLIPPREC          = b"2"
vLFQUALITY           = b"1"
vLFPITCHAND          = b"22"
vLFFACENAME          = b"Times New Roman"       #(fonte do corpo do texto): Symbol/Arial/Times New Roman/Calibri/...
vLFHEIGHTTI          = b"-13"
vLFWIDTHTI           = b"0"
vLFESCAPETI          = b"0"
vLFORIENTTI          = b"0"
vLFWEIGHTTI          = b"700"
vLFITALICTI          = b"0"
vLFUNDERLTI          = b"1"
vLFSTRIKETI          = b"0"
vLFCHARSETI          = b"0"
vLFOUTPRETI          = b"3"
vLFCLIPPRTI          = b"2"
vLFQUALITTI          = b"1"
vLFPITCHTI           = b"12"
vLFFACENATI          = b"Calibri"               #(fonte do titulo): Calibri
vSZTITLE             = b"Estamos em teste ;)"   #(texto na barra de titulo): Estamos em teste ;)
vALARMTIME           = b"2019,10,27,1,50"       #(data e horario do alarme): vazio eh desativado ou "ano,mes,dia,hora,minuto"
vRECURRINGALARMTYPE  = b"5"                     #(unidade de medida): 1-minutos, 2-horas, 3-dias, 4-semanas, 5-meses
vRECURRINGALARMVALUE = b"10"                    #(valor de minutos/horas/dias/meses ou anos):
vROLLUP              = b"Yes"                   #(encolher note): campo vazio (nao) ou Yes (sim)                     

data = vText + b"End of TCPIP text"    +                        b"#\r\n"
data = data  + b"From="                + vFrom                + b"#\r\n"
data = data  + b"SentBy="              + vSentBy              + b"#\r\n"
data = data  + b"StayOnTop="           + vStayOnTop           + b"#\r\n"
data = data  + b"HasBorder="           + vHasBorder           + b"#\r\n"
data = data  + b"BkColor="             + vBkColor             + b"#\r\n"
data = data  + b"FoColor="             + vFoColor             + b"#\r\n"
data = data  + b"TiBkColor="           + vTiBkColor           + b"#\r\n"
data = data  + b"TiFoColor="           + vTiFoColor           + b"#\r\n"
data = data  + b"X="                   + vX                   + b"#\r\n"
data = data  + b"Y="                   + vY                   + b"#\r\n"
data = data  + b"Width="               + vWidth               + b"#\r\n"
data = data  + b"Height="              + vHeight              + b"#\r\n"
data = data  + b"Sponsored="           + vSponsored           + b"#\r\n"
data = data  + b"LFHEIGHT="            + vLFHEIGHT            + b"#\r\n"
data = data  + b"LFWIDTH="             + vLFWIDTH             + b"#\r\n"
data = data  + b"LFESCAPEME="          + vLFESCAPEME          + b"#\r\n"
data = data  + b"LFORIENTAT="          + vLFORIENTAT          + b"#\r\n"
data = data  + b"LFWEIGHT="            + vLFWEIGHT            + b"#\r\n"
data = data  + b"LFITALIC=0"           + vLFITALIC            + b"#\r\n"
data = data  + b"LFUNDERLIN="          + vLFUNDERLIN          + b"#\r\n"
data = data  + b"LFSTRIKEOU="          + vLFSTRIKEOU          + b"#\r\n"
data = data  + b"LFCHARSET="           + vLFCHARSET           + b"#\r\n"
data = data  + b"LFOUTPRECI="          + vLFOUTPRECI          + b"#\r\n"
data = data  + b"LFCLIPPREC="          + vLFCLIPPREC          + b"#\r\n"
data = data  + b"LFQUALITY="           + vLFQUALITY           + b"#\r\n"
data = data  + b"LFPITCHAND="          + vLFPITCHAND          + b"#\r\n"
data = data  + b"LFFACENAME="          + vLFFACENAME          + b"#\r\n"
data = data  + b"LFHEIGHTTI="          + vLFHEIGHTTI          + b"#\r\n"
data = data  + b"LFWIDTHTI="           + vLFWIDTHTI           + b"#\r\n"
data = data  + b"LFESCAPETI="          + vLFESCAPETI          + b"#\r\n"
data = data  + b"LFORIENTTI="          + vLFORIENTTI          + b"#\r\n"
data = data  + b"LFWEIGHTTI="          + vLFWEIGHTTI          + b"#\r\n"
data = data  + b"LFITALICTI="          + vLFITALICTI          + b"#\r\n"
data = data  + b"LFUNDERLTI="          + vLFUNDERLTI          + b"#\r\n"
data = data  + b"LFSTRIKETI="          + vLFSTRIKETI          + b"#\r\n"
data = data  + b"LFCHARSETI="          + vLFCHARSETI          + b"#\r\n"
data = data  + b"LFOUTPRETI="          + vLFOUTPRETI          + b"#\r\n"
data = data  + b"LFCLIPPRTI="          + vLFCLIPPRTI          + b"#\r\n"
data = data  + b"LFQUALITTI="          + vLFQUALITTI          + b"#\r\n"
data = data  + b"LFPITCHTI="           + vLFPITCHTI           + b"#\r\n"
data = data  + b"LFFACENATI="          + vLFFACENATI          + b"#\r\n"
data = data  + b"SZTITLE="             + vSZTITLE             + b"#\r\n"
data = data  + b"ALARMTIME="           + vALARMTIME           + b"#\r\n"
data = data  + b"RECURRINGALARMTYPE="  + vRECURRINGALARMTYPE  + b"#\r\n"
data = data  + b"RECURRINGALARMVALUE=" + vRECURRINGALARMVALUE + b"#\r\n"
data = data  + b"ROLLUP="              + vROLLUP              + b"#\r\n"

import socket
tcp = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
tcp.connect( ( HOST, PORT ) )
tcp.send ( data )
tcp.close()


## https://docs.python.org/3/library/socket.html
#import socket
## https://docs.python.org/3/library/socket.html#socket.socket
## https://docs.python.org/3/library/socket.html#constants
#tcp = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
## https://docs.python.org/3/library/socket.html#socket.socket.connect
#tcp.connect( ( HOST, PORT ) )
## https://docs.python.org/3/library/functions.html#func-bytearray
## https://docs.python.org/3/library/stdtypes.html#binaryseq
##bytes = b"Everton LindoEnd of TCPIP text#\r\nFrom=Desenvolvedor#\r\nSentBy=ODYCRUZ-PC#\r\nStayOnTop=Yes#\r\nHasBorder=Yes#\r\nBkColor=10485759#\r\nFoColor=0#\r\nTiBkColor=7340031#\r\nTiFoColor=0#\r\nX=853#\r\nY=397#\r\nWidth=203#\r\nHeight=171#\r\nSponsored=#\r\nLFHEIGHT=-13#\r\nLFWIDTH=0#\r\nLFESCAPEME=0#\r\nLFORIENTAT=0#\r\nLFWEIGHT=400#\r\nLFITALIC=0#\r\nLFUNDERLIN=0#\r\nLFSTRIKEOU=0#\r\nLFCHARSET=0#\r\nLFOUTPRECI=3#\r\nLFCLIPPREC=2#\r\nLFQUALITY=1#\r\nLFPITCHAND=22#\r\nLFFACENAME=Arial#\r\nLFHEIGHTTI=-13#\r\nLFWIDTHTI=0#\r\nLFESCAPETI=0#\r\nLFORIENTTI=0#\r\nLFWEIGHTTI=700#\r\nLFITALICTI=0#\r\nLFUNDERLTI=0#\r\nLFSTRIKETI=0#\r\nLFCHARSETI=0#\r\nLFOUTPRETI=3#\r\nLFCLIPPRTI=2#\r\nLFQUALITTI=1#\r\nLFPITCHTI=12#\r\nLFFACENATI=Times New Roman#\r\nSZTITLE=#\r\nALARMTIME=#\r\nRECURRINGALARMTYPE=#\r\nRECURRINGALARMVALUE=#\r\nROLLUP=#\r\n"
#bytes = b"Everton LindoEnd of TCPIP text#\r\nFrom=Desenvolvedor#\r\nSentBy=ODYCRUZ-PC#\r\nStayOnTop=Yes#\r\nHasBorder=Yes#\r\nBkColor=10485759#\r\nFoColor=0#\r\nTiBkColor=7340031#\r\nTiFoColor=0#\r\nX=853#\r\nY=397#\r\nWidth=203#\r\nHeight=171#\r\nSponsored=#\r\nLFHEIGHT=-13#\r\nLFWIDTH=0#\r\nLFESCAPEME=0#\r\nLFORIENTAT=0#\r\nLFWEIGHT=400#\r\nLFITALIC=0#\r\nLFUNDERLIN=0#\r\nLFSTRIKEOU=0#\r\nLFCHARSET=0#\r\nLFOUTPRECI=3#\r\nLFCLIPPREC=2#\r\nLFQUALITY=1#\r\nLFPITCHAND=22#\r\nLFFACENAME=Arial#\r\nLFHEIGHTTI=-13#\r\nLFWIDTHTI=0#\r\nLFESCAPETI=0#\r\nLFORIENTTI=0#\r\nLFWEIGHTTI=700#\r\nLFITALICTI=0#\r\nLFUNDERLTI=0#\r\nLFSTRIKETI=0#\r\nLFCHARSETI=0#\r\nLFOUTPRETI=3#\r\nLFCLIPPRTI=2#\r\nLFQUALITTI=1#\r\nLFPITCHTI=12#\r\nLFFACENATI=Times New Roman#\r\nSZTITLE=#\r\nALARMTIME=#\r\nRECURRINGALARMTYPE=#\r\nRECURRINGALARMVALUE=#\r\nROLLUP=#\r\n"
## https://docs.python.org/3/library/socket.html#socket.socket.send
#tcp.send ( bytes )
## https://docs.python.org/3/library/socket.html#socket.close
#tcp.close()