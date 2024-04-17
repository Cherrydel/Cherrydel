from tqdm import tqdm
from colorama import Fore, Back, Style
import time
import os
import webbrowser
import sys
import subprocess
import requests
from tqdm import tqdm
from colorama import Fore, Back, Style
import time
import os

# Графический редактор
GRF =  ("_________________________________________________________________________________________________\n")
GRF2 = ("=================================================================================================\n")
GRF3 = ("_______________________________________________\n")
GRF4 = ("============================================================\n")

while True:
    cherrycom = input(Fore.YELLOW + GRF4 + "|                                                          |\n| >   DEL/SYS/CLE/ADMIN/                                  |\n" + Fore.GREEN + "|                                                          |\n| !   START_LOG > ADMIN                                   |\n" + Fore.CYAN + "|                                                          |\n" + GRF4 + " ?   >>>  ")
    if cherrycom == "START_LOG":
        print (Fore.GREEN + " Подключено, необходимо проверить наличие прав пользователя! [ START_LOG ] ")
        
        #====================================================================================================================================================================
        from colorama import Fore
        import os
        import time
        
        print(Fore.YELLOW + " ОЖИДАНИЕ [ ? ADMIN_DEL ] ")
        time.sleep(1.0)
        print(Fore.GREEN + " Проверка LOG SYS [ ? Выполнение ] ")

        try:
            # ADMIN
            #--------------------------------------------------------------------------------------------
            os.system('cls')
            filenames = ["ADMIN.bat", "ADMINdelsystem.bat", "ADMINibturs.bat", "ADMINiLpotf.bat", "ADMINosonping.bat", "ADMINsys.bat"]
            frames = []

            for name in filenames:
                with open(name, "r",encoding="utf8") as f:
                    frames.append(f.readlines())
                                                
                    for frame in frames:
                        print ("".join(frame))
                        time.sleep(1)
                        os.system('cls')
                        print(Fore.GREEN + " Проверка файла.")
                        print(" ADMIN_DEL\LOG-FIELS ")
            #--------------------------------------------------------------------------------------------
            #====================================================================================================================================================================
            
            GRF =  ("_________________________________________________________________________________________________\n")
            GRF2 = ("=================================================================================================\n")
            GRF3 = ("_______________________________________________\n")
            GRF4 = ("============================================================\n")
            GRF5 = ("\n===== < Cherry.DEL 4.7.0 TERMINAL ADM > ====================\n")
                    
                    # Приветствие
            time.sleep (2.6)

            try:
                while True:
                    cherrycom = input(Fore.GREEN + GRF5 + "|                                                          |\n| >   DEL/SYS/ADM/                                         |\n" + Fore.YELLOW + "|                                                          |\n| !   Commands > on-Starting >>> [ INFO ]                  |\n" + Fore.GREEN + "|                                                          |\n" + GRF4 + " ?   >>>  ")
                                
                    if cherrycom == 'cd':
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
                            
                    elif cherrycom == 'INFO':
                        print (Fore.YELLOW + "\n___________________________________________________________________________")
                        print("========================= Меню системы DEL ================================")
                        print(" Для загрузки модулей перейдитне на канал MODUL [ https://t.me/modulsys ] \n")
                                
                        print("= OS_DEL-MODUL      =")
                        print("= GAMES_DEL-MODUL   =")
                        print("= SERVER_DEL-MODUL  =")
                        print("___________________________________________________________________________\n" + Fore.CYAN)
                                
                    elif cherrycom == 'OS_DEL-MODUL':
                        from Modulsys.Osdel.SETUPSYS import time
                                
                    elif cherrycom == 'GAMES_DEL-MODUL':
                        from Modulsys.Gamesdel.STARTING import time

                    elif cherrycom == 'SERVER_DEL-MODUL':
                        from Modulsys.Serverdel.server import time
                                
                    elif cherrycom == 'https://t.me/modulsys':
                        print ( " Скопируйте ссылку и перейдите в телеграмм. " )
                                
                    elif cherrycom == "":
                        print (Fore.RED + " ERROR-SYS [ INFO ] " )
                                
                    else:
                        print (Fore.RED + " Введено не верное значение. [ INFO ] " + Fore.YELLOW)
            except:
                print (Fore.RED + " Ошибка выполнения программного обеспечения. " )

        except FileNotFoundError:
            print ( " Не найдены файлы LOG_DEL [ ADMIN_DEL\LOG-FIELS ] " )
            time.sleep(0.1)
