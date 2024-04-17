import socket, threading
from tqdm import tqdm
from colorama import Fore, Back, Style
import time
import os
import webbrowser
import sys
import subprocess
import requests

commands = input ( "\n \n Комманда для запуска вашего решения. ( Пример: Start_DEL ) " )
print ( " Далее необходимо создать условие на языке программирования Python и сохранить файл по дириктории C:\DELIEX_SYS\Modulsys\OS_DEL\cmdsys\Modul\Project\\n Имя файла с расширением py " )
os.system ("C:\DELIEX_SYS\Modulsys\OS_DEL\cmdsys\soult.exe")

uslovie = input ( " Запуск вашего решения. ( Путь к файлу который вы сохранили > ) " )

print ( Fore.MAGENTA + " Starting " )
time.sleep (0.1)

while True:
    osdelsystemog = input ( Fore.RED + "\n [ START-FIEL ] \n />>>  :" + Fore.GREEN + "  " )
    
    if osdelsystemog == commands:
        print ( Fore.GREEN + " Перенаправление на файл SYS/OS/CONF/USER/Modul/Project" + uslovie )
        time.sleep(0.1)
        os.system ( "" + uslovie + "" )
    
    elif osdelsystemog == '0':
        print ( Fore.GREEN + " Перенаправление на файл = ? " + uslovie )
        time.sleep(0.1)
        os.system ( "" + uslovie + "" )
        break
        
    elif osdelsystemog == 'cd':
        print ( Fore.RED + " Выход из системы редактирования MODUL_SYS " )
        time.sleep (3.0)
        break
        
    else:
        print ( Fore.RED + " Нет такого условия [ ERROR-SYS ] " )
