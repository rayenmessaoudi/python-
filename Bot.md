


```python
import sys
import socket
import time


server="irc.freenode.net"
botnick="Test"
channel="#name_channel"

#Establish connection
irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
irc.connect((server,6667))
irc.setblocking(False)
time.sleep(1)
irc.send("USER "+botnick+" "+botnick+" "+botnick+" :Hello! I am a test bot!\r\n")
time.sleep(1)
irc.send("NICK "+botnick+"\n")
time.sleep(1)
irc.send("JOIN "+channel+"\n")

while 1:
     time.sleep(0.1)
     try:
          text=irc.recv(2040)
          print(text)
     except Exception:
          pass
     if text.find("PING")!=-1:
          irc.send("PONG "+text.split()[1]+"\r\n")
     if text.lower().find(":@hi")!=-1:
          irc.send("PRIVMSG "+channel+" :hello!\r\n")
     text=""
input()

```
