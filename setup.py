#insuring pip is installed or not !
try:
    import pip
except ImportError:
    try:
        import ensurepip
        ensurepip.bootstrap()
    except ImportError:
        while True:
            nothing=input('pip is not installed try downloading pip first\nafter installation restart the code again:)')
import os
import subprocess
import socket
def check_internet_connection():
    remote_server = "www.google.com"
    port = 80
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)
    try:
        sock.connect((remote_server, port))
        return True
    except socket.error:
        return False
    finally:
        sock.close()
#checking if internet is conected or not !
while True:
    if check_internet_connection():
        print("Internet is connected")
        break
    else:
        answer2=input("internet is not conected? do u wanna refresh?- y ")
        if answer2=='y':
            continue
        else:
            print('please type y or end the code')
#installing libraries
try:
    from termcolor import colored
except ImportError:
    subprocess.call(['pip3','install','termcolor'])
    from termcolor import colored
try:
    import sys
except ImportError:
    subprocess.call(['pip3','install','sys'])
try:
    import getpass
except ImportError:
    subprocess.call(['pip3','install','getpass'])
try:
    import json
except ImportError:
    subprocess.call(['pip3','install','json'])
try:
    import time
except ImportError:
    subprocess.call(['pip3','install','time'])
try:
    import random
except ImportError:
    subprocess.call(['pip3','install','random'])
try:
    import datetime
except ImportError:
    subprocess.call(['pip3','install','datetime'])
try:
    import re
except ImportError:
    subprocess.call(['pip3','install','re'])
#path creatation
path_of_dir='C:\\users\\Public'
if os.path.exists(path_of_dir+'\\'+"tally"):
    pass
else:
    os.mkdir(path_of_dir+'\\'+"tally")
if os.path.exists('C:\\users\\Public\\tally\\tally_dev_info'):
    pass
else:
    os.mkdir('C:\\users\\Public\\tally\\tally_dev_info')
if os.path.exists('C:\\users\\Public\\tally\\company_name'):
    pass
else:
    os.mkdir('C:\\users\\Public\\tally\\company_name')