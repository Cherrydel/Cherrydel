from Modulsys.Serverdel.Config import log, zmr, off, names
import socket, threading
from tqdm import tqdm
from colorama import Fore, Back, Style
import time
import os
import webbrowser
import sys
import subprocess
import requests

print (Fore.YELLOW + "")

while True:
    print ( "\n Ваш IP. " )
    ip = input ( " Введите значение " )
    
    LOCALHOST = ip
    PORT = 1488
    
    try:
        if ip == ip:
            print (" Анализация DEL... ")
            time.sleep(2.0)
            input ( " >>> Нажмите на ENTER " )
            print ( Fore.YELLOW )
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

            # Поиск порта и IP
            server.bind((LOCALHOST, PORT))
            print(" > Сервер запущен успешно! ")

        else:
            print (" Не выполнимо! ")
            input ()

        # Ожидание клиента
        class ClientThread(threading.Thread):
            def __init__(self,clientAddress,clientsocket):
                threading.Thread.__init__(self)
                self.csocket = clientsocket
                print (Fore.GREEN + "\n >>> Новое подключение: ", clientAddress)

            def run(self):
                print (" >>> Подключение клиента : ВЫПОЛНЕНО ")

                msg = ''
                # Упровление сервером в клиенской части.
                try:
                    while True:
                        try:
                            self.csocket.send(bytes( Fore.YELLOW + "\n Вы подключены к другому серверу. \n IP < " + ip + " > \n PROJECT < " + names + " > \n", 'UTF-8'))
                            data = self.csocket.recv(4096)
                            msg = data.decode()
                            print(msg)
                        except BrokenPipeError:
                            print( " Плавное отключение потоков в системе DEL " )
                            break
                        except:
                            print( " Неизвестная ошибка " )
                        
                        if msg == log:
                            os.system("SYS.bat")
                            print ( " Отчистка выполнена успешно... " )
                            self.csocket.send(bytes( Fore.YELLOW + " Вы под защитой системы. Помните что всё что вы водите и исполняете, всё ложится на вас. Проект Deliex.DEL не отвечает за ваши действия и не нисёт ответственость в защищёном режиме. ", 'UTF-8'))

                        elif msg == 'restart':
                            while True:
                                server.listen(1)
                                clientsock, clientAddress = server.accept()
                                newthread = ClientThread(clientAddress, clientsock)
                                newthread.start()
                            
                        elif msg == off:
                            self.csocket.send(bytes( Fore.YELLOW + " Выключение сервера через 1.10 ", 'UTF-8'))
                            print (" Выключение системы через 1.10 ")
                            for i in tqdm (range (100),
                                    desc=  "  Попытка выключения...",
                                    ascii=False, ncols=75):
                                time.sleep(1.10)
                            self.csocket.send(bytes( Fore.YELLOW + " Выполнена выключение Сервера (" + names + ") [ НЕОБРАТИМО... ] ", 'UTF-8'))
                            print ( " Выполнена выключение Сервера " + names )
                            os.abort()
                            
                        elif msg == zmr:
                            self.csocket.send(bytes( Fore.YELLOW + " Переход в систему через 0.10 ", 'UTF-8'))
                            print (" Замарозка системы через 0.10 ")
                            for i in tqdm (range (100),
                                    desc=  "  Попытка выключения...",
                                    ascii=False, ncols=75):
                                time.sleep(0.10)
                            self.csocket.send(bytes( Fore.YELLOW + " Выполнена замарозка Сервера (" + names + ") [ НЕОБРАТИМО... ] ", 'UTF-8'))
                            print ( " Выполнена замарозка Сервера " + names )
                            break
                        
                        else:
                            print (Fore.RED + "   >> Не верное значение... " )
                            
                except ConnectionResetError:
                        print (Fore.RED + "\n >>> Принудительное отключение: ")
                        
        # Бесконечный цыкл ожидания клиента
        while True:
            print( Fore.GREEN + "\n > Ожидание клиента... \n" )
            server.listen(1)
            clientsock, clientAddress = server.accept()
            newthread = ClientThread(clientAddress, clientsock)
            newthread.start()
            
    except socket.gaierror:
        print (Fore.RED +  " Этот IP не является локальным... " )
        LOCALHOST
        
    except SyntaxWarning:
            print (Fore.RED +   " ERROR-SYS " )
            
    except OSError:
            print (Fore.RED +   " SYS ERROR INFO-DEL SERVER SYS\SYS ERROR INFO-DEL CLIENT SYS " )
            LOCALHOST
