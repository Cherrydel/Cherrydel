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

# HELP -l
print ( Fore.WHITE +    "\n|===================================================================================================================")
print ( Fore.WHITE +    "|          [ Функция HELP -l ]          ( Функция команды HELP -l ) " )
print ( Fore.GREEN +    "|          [ Переходы ]                 ( Стандарт функции OS ) " )
print ( Fore.CYAN +     "|          [ cd ]                       ( Перейти назад ) " )
print ( Fore.CYAN +     "|          [ ls ]                       ( Вывести каталог ) " )
print ( Fore.GREEN +    "|          [ Систематизация ]           ( Функции ядра модуля ) " )
print ( Fore.CYAN +     "|          [ / ]                        ( Перейти к модулю или катологу ) " )
print ( Fore.CYAN +     "|          [ > ]                        ( Запуск чего либо ) " )
print ( Fore.CYAN +     "|          [ - ]                        ( Система подтверждения или расширения 'Y' 'l' 'и.тп' ) " )
print ( Fore.WHITE +    "|___________________________________________________________________________________________________________________")
print ( Fore.WHITE +    "|          [ Функция HELP -l ]          ( Функция команды HELP -l ) " )
print ( Fore.GREEN +    "|          [ SYS/OS/CONF/ST ]           ( Запуск скрипта установки OS ) " )
print ( Fore.CYAN +     "|          [ YESOSST ]                  ( Положительное подтверждение устоновки OS ) " )
print ( Fore.CYAN +     "|          [ NOOSST ]                   ( Отрицательное подтверждение устоновки OS ) " )
print ( Fore.GREEN +    "|          [ SYS/OS/CONF/PN ]           ( Запуск скрипта Старта OS ) " )
print ( Fore.CYAN +     "|          [ YESOSPING ]                ( Положительное подтверждение запуска OS ) " )
print ( Fore.CYAN +     "|          [ NOOSPING ]                 ( Отрицательное подтверждение запуска OS ) " )
print ( Fore.RED +      "|          [ EXIT ]                     ( Выход ) " )
print ( Fore.WHITE +    "|===================================================================================================================\n")

# LS
print ( Fore.WHITE +    "\n|===================================================================================================================")
print ( Fore.WHITE +    "|          [ Функция ls ]               ( Функция команды ls )")
print ( Fore.GREEN +    "|          [ Программа ]                ( Цель программы ) " )
print ( Fore.GREEN +    "|          [ Скриптинг ]                ( Консольное приложение ) " )
print ( Fore.GREEN +    "|          [ MODUL ]                    ( Модульные приложения ) " )
print ( Fore.WHITE +    "|===================================================================================================================\n")

# Питание и система.
print ( Fore.YELLOW +   "\n|===================================================================================================================")
print ( Fore.GREEN +    "|          [ Питание ]                  ( Функции ошибок и питания ) " )
print ( Fore.YELLOW +   "|          [ USER ]                     ( Пользователь ) " )
print ( Fore.RED +      "|          [ EXIT ]                     ( Выход ) " )
print ( Fore.YELLOW +   "|===================================================================================================================\n")

print ( Fore.YELLOW +   "\n|======= ( ERROR-SYS ) =============================================================================================")
print ( Fore.GREEN +    "|          [ Питание ]                  ( Функции ошибок и питания ) " )
print ( Fore.RED +      "|          [ 0 ]                        ( Дополнительный блок вашей системы. ) " )
print ( Fore.RED +      "|          [ cd -l ]                    ( Назад ) " )
print ( Fore.RED +      "|          [ EXIT -l ]                  ( Выход ) " )
print ( Fore.YELLOW +   "|===================================================================================================================\n")

while True:
    osdelsystemog = input ( Fore.RED + for3 + "\n|========== SYS/OS/CONF/> === [ERROR-SYS] \n|=== />>>  :" + Fore.WHITE + "  " )
    
    if osdelsystemog == '0':
        print ( Fore.WHITE + " NO SYS DEL " )
    
    elif osdelsystemog == 'cd -l':
        print ( Fore.RED + "|    />  Назад в систему OS_DEL " )
        time.sleep (3.0)
        break
    
    elif osdelsystemog == 'EXIT -l':
        print ( Fore.RED + "|    />  Выход из OS_DEL " )
        time.sleep (3.0)
        os.abort()
    
    else:
        print ( Fore.RED + "|=== /> [ ERROR-SYS ]" + Fore.YELLOW + " > ( " + osdelsystemog + " )")
