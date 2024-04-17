import socket, threading
from tqdm import tqdm
from colorama import Fore, Back, Style
import time
import os
import webbrowser
import sys
import subprocess
import requests

for3 = "|________________________________________________________"
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

            print ( Fore.GREEN + " \n")

            print ( Fore.RED +      "       ::::::::   ::::::::            :::::::::  :::::::::: :::   " )
            time.sleep (0.1)
            print ( Fore.YELLOW +   "     :+:    :+: :+:    :+:           :+:    :+: :+:        :+:    " )
            time.sleep (0.1)
            print ( Fore.WHITE +    "    +:+    +:+ +:+                  +:+    +:+ +:+        +:+     " )
            time.sleep (0.1)
            print ( Fore.GREEN +    "   +#+    +:+ +#++:++#++           +#+    +:+ +#++:++#   +#+      " )
            time.sleep (0.1)
            print ( Fore.CYAN +     "  +#+    +#+        +#+           +#+    +#+ +#+        +#+       " )
            time.sleep (0.1)
            print ( Fore.BLUE +     " #+#    #+# #+#    #+#           #+#    #+# #+#        #+#        " )
            time.sleep (0.1)
            print ( Fore.MAGENTA +  " ########   ######## ########## #########  ########## ########## "  )
            time.sleep (0.1)


            print ( Fore.GREEN + "\n \n Starting OS TERMINAL_SYS ")
            print ( Fore.GREEN + " Version 2.0.5 \n")
            time.sleep (0.1)
            print ( Fore.RED + " Server > OFF ")
            time.sleep (0.1)
            print ( Fore.RED + " GRF & GUI > OFF ")
            time.sleep (0.1)
            print ( Fore.GREEN + " Command_del > ON ")
            time.sleep (0.1)
            print ( Fore.YELLOW + " WEB-SYS > INFO ")
            time.sleep (0.1)
            print ( Fore.YELLOW + " CHERRY > INFO ")
            time.sleep (0.1)
            print ( Fore.RED + " GAMES > OFF ")
            time.sleep (0.1)
            print ( Fore.RED + " STR_DEL > OFF ")
            time.sleep (0.1)
            print ( Fore.MAGENTA + "\n " )
            time.sleep (0.1)

            # Проверка обновлений

            print ("[ Starting. TERMINAL_SYS ]")
            import time
            import sys
            toolbar_width = 40
            sys.stdout.write("[%s]" % (" " * toolbar_width))
            sys.stdout.flush()
            sys.stdout.write("\b" * (toolbar_width+1))
            for i in range(toolbar_width):
                time.sleep(0.1)
                sys.stdout.write("-")
                sys.stdout.flush()
            sys.stdout.write("]\n")

            while True:
                osdelsystemog = input ( Fore.MAGENTA + for3 + "\n|========== SYS/OS/CONF/PN === [USER] \n|=== />>>  :" + Fore.YELLOW + "  " )
                
                # HELP Информация и значение системы ==========================================================================================================
                if osdelsystemog == 'HELP -l':
                    print ( Fore.GREEN +    "|\n|          [ Команда ]                  ( Функция команды ) " )
                    
                    print ( Fore.GREEN +    "|          [ Переходы ]                 ( Стандарт функции OS ) " )
                    print ( Fore.CYAN +     "|          [ cd ]                       ( Перейти назад ) " )
                    print ( Fore.CYAN +     "|          [ ls ]                       ( Вывести каталог ) " )
                    
                    print ( Fore.GREEN +    "|          [ Систематизация ]           ( Функции ядра модуля ) " )
                    print ( Fore.CYAN +     "|          [ / ]                        ( Перейти к модулю или катологу ) " )
                    print ( Fore.CYAN +     "|          [ > ]                        ( Запуск чего либо ) " )
                    print ( Fore.CYAN +     "|          [ - ]                        ( Система подтверждения или расширения 'Y' 'l' 'и.тп' ) " )
                    
                    print ( Fore.GREEN +    "|          [ Питание ]                  ( Функции ошибок и питания ) " )
                    print ( Fore.YELLOW +   "|          [ USER ]                     ( Пользователь ) " )
                    print ( Fore.RED +      "|          [ EXIT ]                     ( Выход ) \n|" )
                    
                # LS Программы =================================================================================================================================
                elif osdelsystemog == 'ls':
                    print ( Fore.GREEN +    "|\n|          [ Программа ]                ( Цель программы ) " )
                    
                    print ( Fore.GREEN +    "|          [ Скриптинг ]                ( Консольное приложение ) " )
                    print ( Fore.CYAN +     "|          [ SYS_MODUL ]                ( Создание модулей [ ОПАСНО ] ) " )
                    
                    print ( Fore.GREEN +    "|          [ MODUL ]                    ( Модульные приложения ) " )
                    print ( Fore.CYAN +     "|          [ > PING-MODUL ]             ( Запуск стороних модулей ) " )
                    
                    print ( Fore.GREEN +    "|          [ Питание ]                  ( Функции ошибок и питания ) " )
                    print ( Fore.RED +      "|          [ EXIT ]                     ( Выход ) \n|" )
                    
                # Список модулей =================================================================================================================================
                elif osdelsystemog == '/':
                    print ( Fore.GREEN +    "|\n|          [ Программа ]                ( Цель программы ) " )
                    
                    print ( Fore.GREEN +    "|          [ MODUL ]                    ( Модульные приложения ) " )
                    print ( Fore.CYAN +     "|          [ / > SYS_MODUL ]            ( Создание модулей [ ОПАСНО ] ) " )
                    
                # LS Server =====================================================================================================================================
                    
                elif osdelsystemog == 'ERROR-SYS':
                    print ( Fore.GREEN +    "|\n Подключение к ERROR-SYS " )
                    from Modulsys.Osdel.systemdel.Errorsys import *
                    
                elif osdelsystemog == 'USER':
                    print ( Fore.GREEN +    "|\n Вы вошли как USER " )
                    
                elif osdelsystemog == '/ > SYS_MODUL':
                    print ( Fore.GREEN +    "|\n Запуск SYS_MODUL " )
                    from Modulsys.Osdel.cmdsys.sysmodul.ckelet import *
                    
                if osdelsystemog == ' > PING-MODUL':
                    puti = input ( " Введите путь до модуля или программного обеспечения с файлом запуска " )
                    os.system ( "" + puti + "" )
                    
                elif osdelsystemog == 'EXIT':
                    print ( Fore.RED + "|    />  Выход из OS_DEL " )
                    time.sleep (3.0)
                    os.abort()
                
                else:
                    print ( Fore.RED + "|=== /> [ ERROR-SYS ]" + Fore.YELLOW + " > ( " + osdelsystemog + " )")
                    
        except FileNotFoundError:
            print (Fore.YELLOW + " Не найдены файлы LOG_DEL [ OS_DEL\LOG-FIELS ] \n \n" )
            time.sleep(0.1)
