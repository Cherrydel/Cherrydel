# Работа сервера или с сервером

import socket
from threading import Thread
import threading
from colorama import Fore, Back, Style
import time

print ( Fore.YELLOW + "" )
print ( " CHERRY_DEL VERSION 4.7.0 TERMINAL " )

while True:
    SERVERSYS = input (Fore.CYAN + " Введите IP-Адресс: >>> ")
    
    SERVER = SERVERSYS
    PORT = 1488
    
    try:
        if SERVERSYS == SERVERSYS:
            print (Fore.GREEN + " Попытка подключения... ")
            print ( Fore.YELLOW )
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((SERVER, PORT))
            
        else:
            print (Fore.RED +  "\n \n >>> Не верен IP-SYSTEM DEL " )
                
        client.sendall(bytes(Fore.CYAN + "== > Модуль: CHERRY_DEL 4.7.0 TERMINAL <==", "UTF-8\n"))
        print (Fore.RED)
        
        def task():
            try:
                while True:
                    in_data =  client.recv(4096)
                    print( Fore.RED + "DEL/SYS >> SYS_ERROR | INFO LOG ( От сервера... ) :" ,in_data.decode())
            except ConnectionResetError:
                print (Fore.RED +  " Сервер отключен [ Причина не известно. ] ... \n====================================================================================" )
                
        def task2():
            try:
                while True:
                    out_data = input( " DEL/SYS/  >>>  : " )
                    client.sendall(bytes(out_data,'UTF-8'))
                    print("Отправлено на сервер : >>> " + str(out_data))
                    
#====================================================================================================================================================================================        
        
                    # Работа клиента 
                    # CHERRY ( 4.7.0. )
                    from tqdm import tqdm
                    from colorama import Fore, Back, Style
                    import time
                    import os
                    import webbrowser
                    import sys
                    import subprocess
                    import requests
                    
                    # Графический редактор
                    GRF =  ("_________________________________________________________________________________________________\n")
                    GRF2 = ("=================================================================================================\n")
                    GRF3 = ("_______________________________________________\n")
                    GRF4 = ("============================================================\n")
                    GRF5 = ("\n===== < Cherry.DEL 4.7.0 TERMINAL > ========================\n")
                    
                    # Приветствие
                    time.sleep (2.6)

                    try:
                        while True:
                            cherrycom = input(Fore.RED + GRF5 + "|                                                          |\n| >   DEL/SYS/TER/                                         |\n" + Fore.YELLOW + "|                                                          |\n| !   Commands > on-Starting >>> Admin                     |\n" + Fore.CYAN + "|                                                          |\n" + GRF4 + " ?   >>>  ")
                            if cherrycom == "Admin":
                                time.sleep (0.1)
                                print (" Для перехода в систему DEL TERMINAL необходимо соеденится с сервером. \n Для этого введите команду ( cd ) после вы перейдёте в режим системы и сервера. \n C этого режима вы можете отправлять команды на сервер. \n Для Авторизации DEL_ROOT введите команду для сервера ( AUTADMIN ) \n ")
                                
                            elif cherrycom == 'ADMINNAME': # Администраторы
                                time.sleep (0.1)
                                print (Fore.GREEN + " Проверка файловой системы DEL " )
                                print (Fore.GREEN + " Попытка импорта модульной системы " )
                                print (Fore.GREEN + " Проверка LOG DEL " )
                                time.sleep(5.0)
                                from Starting.adm.Startadm import time
                                
                            elif cherrycom == 'cd':
                                print ( Fore.RED + " DEL/SYS/ \n" )
                                break
                            
                            elif cherrycom == 'EXIT':
                                print ( Fore.RED + " DEL/SYS/ \n" )
                                print (" Выключение системы через 0.05 ")
                                for i in tqdm (range (100),
                                        desc=  "  Попытка выключения...",
                                        ascii=False, ncols=75):
                                    time.sleep(0.05)
                                os.abort()

                            elif cherrycom == 'https://t.me/modulsys':
                                print ( " Скопируйте ссылку и перейдите в телеграмм. " )
                                
                            else:
                                print (Fore.RED + " Введено не верное значение. " + Fore.YELLOW)
                    except:
                        print (Fore.RED + " Ошибка выполнения программного обеспечения. " )
                            
            except ConnectionResetError:
                print (Fore.RED +  " Выполнено выключение Сервера () [ НЕОБРАТИМО... ] ... \n============================================================================" )

# Конечная работа КЛИЕНТА
#====================================================================================================================================================================================

        t1 = Thread(target=task2)
        t2 = Thread(target=task)
        
        t1.start()
        t2.start()
        
        t1.join()
        t2.join()
        
    except socket.gaierror:
        print (Fore.RED +  " Не верный IP-Адресс... " )
        SERVERSYS
        
    except SyntaxWarning:
            print (Fore.RED +   " ERROR-SYS " )
            
    except OSError:
            print (Fore.RED +   " SYS ERROR INFO-DEL SERVER SYS\SYS ERROR INFO-DEL CLIENT SYS " )
            SERVERSYS
