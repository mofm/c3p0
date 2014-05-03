#!/usr/bin/env python

import socket,datetime 

def commands(nick,channel,message):
   if message.find(botnick+': oylama')!=-1:
         ircsock.send('PRIVMSG %s : 3\r\n' % (channel))
   elif message.find(botnick+': itiraf')!=-1:
	 ircsock.send('PRIVMSG %s :%s: itiraf, oylama\r\n' % (channel,nick))


server = "irc.freenode.net" # Server
channel = "#pyistanbul" # Channel
botnick = "3rd3m" # Your bots nick

def ping(): 
  ircsock.send("PONG :pingis\n")  

def sendmsg(chan , msg): 
  ircsock.send("PRIVMSG "+ chan +" :"+ msg +"\n") 

def joinchan(chan): 
  ircsock.send("JOIN "+ chan +"\n")

def slm(): 
  ircsock.send("PRIVMSG "+ channel +" :selam!\n")

def cuma():
  ircsock.send("PRIVMSG "+ channel +" :Hayirli Cumalar\n")
  
                  
ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ircsock.connect((server, 6667)) 
ircsock.send("USER "+ botnick +" "+ botnick +" "+ botnick +" : ben geldimmmm\n") 
ircsock.send("NICK "+ botnick +"\n") 

joinchan(channel) 

while 1: 
  ircmsg = ircsock.recv(2048) 
  ircmsg = ircmsg.strip('\n\r') 
  holyday = datetime.datetime.today().weekday()

  print(ircmsg) 
  
  if ircmsg.find(' PRIVMSG ')!=-1:
     nick=ircmsg.split('!')[0][1:]
     channel=ircmsg.split(' PRIVMSG ')[-1].split(' :')[0]
     commands(nick,channel,ircmsg)
  
  if ircmsg.find(":slm "+ botnick) != -1: 
     slm()

  if holyday == "5":
     cuma()

  if ircmsg.find("PING :") != -1: 
     ping()
