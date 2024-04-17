import socket, threading
from tqdm import tqdm
from colorama import Fore, Back, Style
import time
import os
import webbrowser
import sys
import subprocess
import requests
print ( Fore.YELLOW + "\n OS_DEL\DELIEX_DEL\SERVER_DEL VERSION 3.0.0 TERMINAL_SYS \n \n" )

print ( Fore.MAGENTA + " Starting OS_del TERMINAL_SYS " )
time.sleep (0.1)
print ( Fore.GREEN + " Conect sys " )
time.sleep (0.1)
print ( Fore.MAGENTA + " Ping os-sys start " )
time.sleep (0.1)
print ( Fore.RED + " SYS-SERVER Starting > Conect sys " )
time.sleep (0.1)
print ( Fore.MAGENTA + " Starting HELP > HOME-SYS " )
time.sleep (0.1)
print ( Fore.RED + " ERROR-GRF & GUI " )
time.sleep (0.1)
print ( Fore.MAGENTA + " Starting WEB-Modul sys error " )
time.sleep (0.1)
print ( Fore.GREEN + " Log- deliex.del sys info " )
time.sleep (0.1)
print ( Fore.MAGENTA + " Cherry.os.del " )
time.sleep (0.1)

while True:
    osdelsystemog = input ( Fore.MAGENTA + "\n [ HELP -l ] \n />>>  :" + Fore.GREEN + "  " )
    
    if osdelsystemog == 'SYS/OS/CONF/ST':
        print ( Fore.GREEN + " Перейти к устоновки OS-DEL. Если ДА > [ YESOSST ], Если НЕТ > [ NOOSST ] " )
        
    # PING ( Запуск установленой OS )   =========================================================================================================================
    elif osdelsystemog == 'SYS/OS/CONF/PN':
        print ( Fore.GREEN + " Перейти к запуску системы OS-DEL. Если ДА > [ YESOSPING ], Если НЕТ > [ NOOSPING ] " )
    
    elif osdelsystemog == 'YESOSPING':
        from Modulsys.Osdel.ping.Startping import time
        
    elif osdelsystemog == 'NOOSPING':
        print ( Fore.RED + " Запуск системы отменено... " )
    
    # START ( Установка )   ======================================================================================================================================
    elif osdelsystemog == 'YESOSST':
        from Modulsys.Osdel.boot.bootst import time
        
    elif osdelsystemog == 'NOOSST':
        print ( Fore.RED + " Установка отменена... " )
        
    # Информация и выход   =======================================================================================================================================
    elif osdelsystemog == 'HELP -l':
        print ( Fore.GREEN + "\n          [ SYS/OS/CONF/ST ] ( Запуск скрипта установки OS ) " )
        print ( Fore.CYAN + "          [ YESOSST ] ( Положительное подтверждение устоновки OS ) " )
        print ( Fore.CYAN + "          [ NOOSST ] ( Отрицательное подтверждение устоновки OS ) " )
        print ( Fore.GREEN + "          [ SYS/OS/CONF/PN ] ( Запуск скрипта Старта OS ) " )
        print ( Fore.CYAN + "          [ YESOSPING ] ( Положительное подтверждение запуска OS ) " )
        print ( Fore.CYAN + "          [ NOOSPING ] ( Отрицательное подтверждение запуска OS ) " )
        print ( Fore.YELLOW + "          [ INFO -l ] ( Информационный блок ) " )
        print ( Fore.RED + "          [ EXIT ] ( Выход ) \n" )
        
    elif osdelsystemog == 'EXIT':
        print ( Fore.RED + " Выход из OS-DEL " )
        time.sleep (3.0)
        break
        # os.abort()
    
    elif osdelsystemog == 'ERROR-SYS':
        time.sleep(1.0)
        from Modulsys.Osdel.systemdel.Errorsys import time
    
    else:
        print ( Fore.RED + " Нет такого условия [ ERROR-SYS ] " )
