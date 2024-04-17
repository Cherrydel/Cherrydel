import time
import os

time.sleep(1.0)

#=============================================================================================================================================================
from colorama import Fore
import os
import time

print(Fore.YELLOW + " ОЖИДАНИЕ [ ? GAMES TERMINAL ] ")
time.sleep(1.0)
print(Fore.GREEN + " Проверка LOG SYS [ ? Выполнение ] ")

while True:
    cherrycom = input(Fore.RED + "DEL/SYS/GAMES/ |? START_LOG >>>  ")
    if cherrycom == "START_LOG":
        print (Fore.GREEN + " Подключено, необходимо проверить наличие прав пользователя! [ START_LOG ] ")
        try:
            # GAMES
            #--------------------------------------------------------------------------------------------
            os.system('cls')
            filenames = ["GAMES.bat", "SYS.bat", "GAMES_SYS.bat", "IPLOG.bat"]
            frames = []

            for name in filenames:
                with open(name, "r",encoding="utf8") as f:
                    frames.append(f.readlines())
                                                        
                    for frame in frames:
                        print ("".join(frame))
                        time.sleep(1)
                        os.system('cls')
                        print(Fore.GREEN + " Проверка файла.")
                        print(" GAMES\GAMES-FIELS ")
            #--------------------------------------------------------------------------------------------
#=============================================================================================================================================================

            print (" ERROR SYS [ PING-MODUL ] ")
            while True:
                gamessys = input(" Введите значение: >>>  ")
                
                if gamessys == 'PING-MODUL':
                    puti = input ( " Введите путь до модуля или программного обеспечения с файлом запуска " )
                    os.system ( "" + puti + "" )
                
                if gamessys == "cd":        
                    print (" Переходим назад ")
                    break
                
        except FileNotFoundError:
            print (Fore.YELLOW + " Не найдены файлы LOG_DEL [ GAMES_DEL\LOG-FIELS ] \n \n" )
            time.sleep(0.1)
