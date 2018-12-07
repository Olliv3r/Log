#!/data/data/com.termux/files/usr/bin/python3
# login
# autor : <olive>

from time import sleep as s
from os import system as S

def banner():
    print("""\033[01;92m
─────█─▄▀█──█▀▄─█───── 
────▐▌──────────▐▌──── 
────█▌▀▄──▄▄──▄▀▐█──── 
───▐██──▀▀──▀▀──██▌─── 
──▄████▄──▐▌──▄████▄──  
    
\033[0m""")

# tool padrao
usuario = "root"
senha = "toor"

# pedindo dados

try:
    banner()
    user = str(input("\033[00;94mUSUARIO [*] \033[01;94m\033[01;93m=\033[01;94m>\033[0m "))
    while user != usuario:
        print("\033[00;93mUsuario Incorreto [❌]\033[0m")
        s(1)
        S("clear")
        banner()
        user = str(input("\033[00;94mUSUARIO [*] \033[01;93m=\033[01;94m>\033[01m "))
    else:
        Pass = str(input("\033[00;94mSENHA [*] \033[01;93m=\033[01;94m>\033[0m "))
        while Pass != senha:
            print("\033[00;93mSenha Incorreta [❌]\033[0m")
            s(1)
            S("clear")
            banner()
            Pass = str(input("\033[00;94mSENHA [*] \033[01;93m=\033[01;94m>\033[0m "))
        else:
            s(1)
            S("clear")
            print("\033[0mAcesso liberado <🔑🔓>")
            print("\n\n")
except KeyboardInterrupt:
    print("Saindo...")
    S("killall -9 com.termux")
    s(1)
except EOFError:
    print("Saindo...")
    s(1)
    S("killall -9 com.termux")
