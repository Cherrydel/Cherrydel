import socket, threading
from tqdm import tqdm
from colorama import Fore, Back, Style
import time
import os
import webbrowser
import sys
import subprocess
import requests

print ( Fore.CYAN + " Подготовка к устоновки... ")
for i in tqdm (range (100),
        desc=  " Проверка файлов",
        ascii=False, ncols=75):
    time.sleep(0.10)

#================================================================================================================================================================
from colorama import Fore
import os
import time

print(Fore.YELLOW + " ОЖИДАНИЕ [ ? OS_DEL ] ")
time.sleep(1.0)
print(Fore.GREEN + " Проверка LOG SYS [ ? Выполнение ] ")

while True:
    cherrycom = input(Fore.RED + "DEL/SYS/OS_DEL/ |? START_LOG >>>  ")
    if cherrycom == "START_LOG":
        print (Fore.GREEN + " Подключено, необходимо проверить наличие прав пользователя! [ START_LOG ] ")
        try:
            # OS_DEL
            #--------------------------------------------------------------------------------------------
            os.system('cls')
            filenames = ["OS_SYSTEM.bat", "OS.bat", "OSIPLOG.bat", "OSPINGSYS.bat"]
            frames = []

            for name in filenames:
                with open(name, "r",encoding="utf8") as f:
                    frames.append(f.readlines())
                                                
                    for frame in frames:
                        print ("".join(frame))
                        time.sleep(1)
                        os.system('cls')
                        print(Fore.GREEN + " Проверка файла.")
                        print(" OS_DEL\LOG-FIELS ")
            #--------------------------------------------------------------------------------------------

            #=================================================================================================================================================================

            while True:
                osdelsystemog = input ( Fore.CYAN + "\n [ START -Y ] \n SYS/OS/CONF/ST \n />>>  :" + Fore.GREEN + "  " )
                
                if osdelsystemog == 'START -Y':
                    print ( Fore.GREEN + " Начнём... " )
                    
                    print ( Fore.GREEN + " Для установки нам нужно загрузить эти файлы... \n" )
                    
                    print ( Fore.YELLOW + " boot... " )
                    print ( Fore.YELLOW + " cmdsys... " )
                    print ( Fore.YELLOW + " ping... " )
                    print ( Fore.YELLOW + " systemdel... " )
                    print ( Fore.YELLOW + " prgdel... \n" )
                    
                    print ( Fore.GREEN + " Для распаковки и сборки файлов введите \n [ Я соглашаюсь с устоновкой компонентов в модуль OS-DEL ] \n" )
                    
                elif osdelsystemog == 'Я соглашаюсь с устоновкой компонентов в модуль OS-DEL':
                    print ( Fore.GREEN + " Выполняется... " )
                    
                    print ( Fore.CYAN + "\n Компиляция файлов... ")
                    for i in tqdm (range (100),
                            desc=  " Установка",
                            ascii=False, ncols=75):
                        time.sleep(0.1)
                        
                    print ( Fore.CYAN + "\n Распаковка файлов... ")
                    for i in tqdm (range (100),
                            desc=  " Установка",
                            ascii=False, ncols=75):
                        time.sleep(1.5)
                        
                    print ( Fore.CYAN + "\n Поиск обновлений... ")
                    for i in tqdm (range (100),
                            desc=  " Установка",
                            ascii=False, ncols=75):
                        time.sleep(0.5)
                        
                    print ( Fore.CYAN + "\n Установка файлов в OS_DEL... ")
                    for i in tqdm (range (100),
                            desc=  " Установка",
                            ascii=False, ncols=75):
                        time.sleep(1.10)
                        
                    print ( Fore.CYAN + "\n Завершение устоновки... ")
                    for i in tqdm (range (100),
                            desc=  " Установка",
                            ascii=False, ncols=75):
                        time.sleep(0.1)
                    
                    while True:
                        osdelsystemog = input ( Fore.CYAN + "\n [ PING YES ] [ PING NO ] [ PING INFO ]  \n SYS/ \n />>>  :" + Fore.GREEN + "  " )
                        if osdelsystemog == 'PING INFO':
                            print ( Fore.GREEN + " Установка ( УСПЕШНО ) " )
                            
                        elif osdelsystemog == 'PING YES':
                            from Modulsys.Osdel.ping.Startping import *
                            
                        elif osdelsystemog == 'PING NO':
                            print ( Fore.RED + " Запуск системы отменено... " )
                            
                        elif osdelsystemog == 'cd':
                            print ( Fore.RED + " Выход из запуска системы. " )
                            time.sleep (3.0)
                            break
                            # os.abort()
                        
                        else:
                            print ( Fore.RED + " Нет такого условия [ ERROR-SYS ] " )
                    
                elif osdelsystemog == 'cd':
                    print ( Fore.RED + " Выход из программы установки " )
                    time.sleep (3.0)
                    break
                    # os.abort()
                
                else:
                    print ( Fore.RED + " Нет такого условия [ ERROR-SYS ] " )
                    
        except FileNotFoundError:
            print (Fore.YELLOW + " Не найдены файлы LOG_DEL [ OS_DEL\LOG-FIELS ] \n \n" )
            time.sleep(0.1)
