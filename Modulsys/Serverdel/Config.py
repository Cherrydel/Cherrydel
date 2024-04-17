import socket, threading
from tqdm import tqdm
from colorama import Fore, Back, Style
import time
import os
import webbrowser
import sys
import subprocess
import requests

print ( "\n \n Добро пожаловать в создание Server_DeL. \n Для начала необходимо скачать программу [ LogMein Hamachi ] зарегистрироватся и создать сеть. \n Далее скопируйте IP-Адресс ( IPv4 ) и вставте сюда. \n Ну а дальше я думаю всё понятно... " )
print ( "\n Рекомендуется проводить всю работу на локальном сервере или на своей техние. \n Возможно пользователям предётся подключится к LogMein Hamachi " )

print ( "\n \n Имя вашего проекта. " )
names = input ( " Введите значение " )

print ( " Проверка LOG и Включение защиты. " )
log = input ( " Введите значение " )

print ( " Выключение сервера со стороны пользователя " )
off = input ( " Введите значение " )

print ( " Замарозка сервера со стороны пользователя " )
zmr = input ( " Введите значение " )
