# Работа сервера или с сервером
import socket
from threading import Thread
import threading
from colorama import Fore, Back, Style
from Modulsys.Gamesdel.Cmds.Command import CD, EXIT, INFO, YES, NO, OFF, HELP, YESG, NOG, INFOG
print ( Fore.YELLOW + "" )
print ( " GAMES_DEL VERSION 3.0.0 TERMINAL " )

while True:
    SERVERSYS = input (Fore.CYAN + " >>> Введите IP-DEL :")
    
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
                
        client.sendall(bytes(Fore.YELLOW + "== > Модуль: GAMES_DEL TERMINAL <==", "UTF-8\n"))
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
                    # GAMES ( 3.0.0. )
                    
                    # Подключение модулей
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
                    GRF5 = ("\n===== < GAMES.DEL TERMINAL > ===============================\n")
                    
                    # Приветствие
                    time.sleep (2.6)
                    
                    #=============================================================================================================================================================
                    
                    from colorama import Fore
                    import os
                    import time

                    print(Fore.YELLOW + " ОЖИДАНИЕ [ ? GAMES ] ")
                    time.sleep(1.0)
                    
                    while True:
                        cherrycom = input(Fore.YELLOW + GRF5 + "|                                                          |\n| >   DEL/SYS/CLE/USR/GMR/                                 |\n" + Fore.GREEN + "|                                                          |\n| !   Commands > HELP                                      |\n" + Fore.YELLOW + "|                                                          |\n" + GRF4 + " ?   >>>  ")
                        if cherrycom == CD:
                            print ( Fore.RED + " DEL/SYS/TER \n" )
                            break
                                    
                        elif cherrycom == EXIT:
                            print ( Fore.RED + " DEL/SYS/ \n" )
                            print (" Выключение системы через 0.05 ")
                            for i in tqdm (range (100),
                                    desc=  "  Попытка выключения...",
                                    ascii=False, ncols=75):
                                time.sleep(0.05)
                            os.abort()
                                    
                        elif cherrycom == OFF:
                            print (" Выключение системы через 0.05 ")
                            for i in tqdm (range (100),
                                    desc=  "  Попытка выключения...",
                                    ascii=False, ncols=75):
                                time.sleep(0.05)
                            os.abort()
                                    
                        else:
                            print (Fore.RED + " Введено не верное значение. " + Fore.YELLOW)
                                    
                        # Работа с командой HELP
                        if cherrycom == HELP:
                            print ("\n LCPD #1     ( Server №1 )       Перейти для подробной информации ? \n \n [ > Да=(YESLOG)   > Нет=(NOSYSLOG)   > Информация=(INFOLOGLCPD1) ] \n ")
                            print ("\n GAMES       ( Игры в системе )  Перейти для подробной информации ? \n \n [ > Да=(YESG)     > Нет=(NOSYSG)     > Информация=(INFOLOGGAMES) ] \n ")
                            time.sleep(1.0)
                                        
                            # LCPD №1
                            while True:
                                gameover = input(Fore.MAGENTA + " Введите значение:   " + Fore.GREEN)
                                if gameover == YES:
                                    print (Fore.GREEN + " Для игры с друзьями вы должны перейти на оффисальный сайт. \n [ https://deliexdel.bitrix24site.ru/gamesdel/ ] " + Fore.YELLOW)
                                    time.sleep(1.0)
                                                
                                elif gameover == NO:
                                    print (Fore.RED + " Переходим назад " + Fore.YELLOW)
                                    break
                                            
                                elif gameover == INFO:
                                    print (Fore.YELLOW + " Игровой комплекс Deliex.DEL предоставляет личные сервера для совместной игры с друзьями в популярные игры разного жанра. \n Для дополнительной информации перейдите на оффисальный сайт Gamse.DEL \n [ https://deliexdel.bitrix24site.ru/gamesdel/#b112 ] " + Fore.YELLOW)
                                                
                            # GAMES
                                elif gameover == YESG:
                                    print (Fore.GREEN + " Для загрузки игр вы должны перейти на оффисальный сайт. \n [ https://deliexdel.bitrix24site.ru/gamesdel/ ] " + Fore.YELLOW)
                                    time.sleep(1.0)
                                    from Modulsys.Gamesdel.Games.Menu import time
                                                
                                elif gameover == NOG:
                                    print (Fore.RED + " Переходим назад " + Fore.YELLOW)
                                    break
                                            
                                elif gameover == INFOG:
                                    print (Fore.YELLOW + " Разрабатываемые игры DELIEX.DEL \n" + Fore.YELLOW)
                                
                                elif gameover == CD:
                                    print (Fore.YELLOW + " Выход из MENU GAMES_DEL \n" + Fore.YELLOW)
                                    time.sleep(3.0)
                                    break
                                                
                                else:
                                    print (Fore.RED + " Введено не верное значение. ")
                                    
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
