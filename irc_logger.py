#!/usr/bin/env python

import socket
import struct
import telnetlib
import time
import re
from parse import *
from math import sqrt
import sys
import base64

#creation des variables utiles______________________

HOST = raw_input('HOST: ');			#"irc.root-me.org";
PORT = int(raw_input('PORT: '));	#6667
NICK = raw_input('NICK: ');			#"Esso";
CHANNEL = raw_input('CHANNEL: ');	#"#root-me_challenge";
TARGET = raw_input('TARGET: ');		#"candy";
S_PORT = str(PORT)

#RESUM_______________________________________________
print ("\nResume:\n"\
"HOST: "	+ HOST   + "\n"\
"PORT: "	+ S_PORT + "\n"\
"NICK: "	+ NICK   + "\n"\
"CHANNEL: " + CHANNEL+ "\n"\
"TARGET: "	+ TARGET + "\n");

#_____________________________________________________

line = NICK + " :(.*)\\r";

def sendMessage(target , msg):
  s.send("PRIVMSG "+ target +" :"+ msg +"\r\n");

#on se connecte a l irc
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
s.connect((HOST, PORT));

time.sleep(2);

s.send("NICK %s\r\n" % NICK);
s.send("USER "+ NICK +" "+ NICK +" "+ NICK +" :NIC2\r\n");
time.sleep(1);
s.send("JOIN "+ CHANNEL +"\r\n");

time.sleep(4);
print('__________________________________________________________________');
print s.recv(8192);

time.sleep(4);


#_1st_mess__________________________________________________________________


p1 = "!ep2" ; #sent <-----*


sendMessage(TARGET, p1);
time.sleep(1);
reponse = s.recv(512);

print('__________________________________________________________________');

print reponse;

print('__________________________________________________________________');

result = re.findall(line, reponse);

#end________________________________________________________________________



#EX BACK_2_SCHOOL____________________/\

# tt = result[0].split('/');
# x = float(tt[0]);
# x = sqrt(x);
# y = float(tt[1]);
# x = x * y;
# x = float("{0:.2f}".format(x));
#____________________________________/\




#EX ENCODING_STRING__________________/\

print base64.b64decode('Um9vdE1l') + "<<<<<<<<";

#____________________________________/\








result = ''; #CHECKING_______________

print "CHECK_VALUE[" + result + "]\n";



#_2nd_mess___________________________


p1 = "!ep2 -rep AA" + str(result); #sent <-----*


sendMessage(TARGET, p1);
time.sleep(2);

tt = s.recv(8192);

time.sleep(2);
print('-- --');
print tt;
