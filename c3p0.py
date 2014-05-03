#!/usr/bin/env python

# Import some necessary libraries.
import socket 
#  Set up our commands function

def commands(nick,channel,message):
   if message.find(botnick+': oylama')!=-1:
         ircsock.send('PRIVMSG %s :%s: 3\r\n' % (channel,nick))
   elif message.find(botnick+': help')!=-1:
	 ircsock.send('PRIVMSG %s :%s: help, oylama\r\n' % (channel,nick))

# Some basic variables used to configure the bot        

server = "irc.freenode.net" # Server
channel = "#pyistanbul" # Channel
botnick = "tnt_2" # Your bots nick

def ping(): # This is our first function! It will respond to server Pings.
  ircsock.send("PONG :pingis\n")  

def sendmsg(chan , msg): # This is the send message function, it simply sends messages to the channel.
  ircsock.send("PRIVMSG "+ chan +" :"+ msg +"\n") 

def joinchan(chan): # This function is used to join channels.
  ircsock.send("JOIN "+ chan +"\n")

def slm(): # This function responds to a user that inputs "Hello Mybot"
  ircsock.send("PRIVMSG "+ channel +" :selam!\n")

                  
ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ircsock.connect((server, 6667)) # Here we connect to the server using the port 6667
ircsock.send("USER "+ botnick +" "+ botnick +" "+ botnick +" : ben geldimmmm\n") # user authentication
ircsock.send("NICK "+ botnick +"\n") # here we actually assign the nick to the bot

joinchan(channel) # Join the channel using the functions we previously defined

while 1: # Be careful with these! it might send you to an infinite loop
  ircmsg = ircsock.recv(2048) # receive data from the server
  ircmsg = ircmsg.strip('\n\r') # removing any unnecessary linebreaks.
  print(ircmsg) # Here we print what's coming from the server
  if ircmsg.find(' PRIVMSG ')!=-1:
     nick=ircmsg.split('!')[0][1:]
     channel=ircmsg.split(' PRIVMSG ')[-1].split(' :')[0]
     commands(nick,channel,ircmsg)
  if ircmsg.find(":slm "+ botnick) != -1: # If we can find "Hello Mybot" it will call the function hello()
     slm()

  if ircmsg.find("PING :") != -1: # if the server pings us then we've got to respond!
     ping()