#!/usr/bin/python
import os
import time
def info_of_ip():
    print(' ')
    print(' ')
    print(' ')
    x = os.popen("curl ifconfig.co")
    y = x.read()
    print('Your Public ip is','<><><> ',y)
    print('                         ^^^^^^^^^^^^^^^')
    print('if you wanna print ip info in new text file type (yes) or (no) to cencel and exit')
    print(' ')
    print(' ')
    print(' ')
    val = input('     type here >>> ')
    t = 'yes'
    q = 'no'
    while val != t and val != q:
        val = input('     be sure your type is true >>> ')
    if val == t:
        i = open("ip_result", "w")
        i.write('this is your ip that we fund >> ')
        i.write(y)
        i.close()
        print('the information that you got are saving!')
        b = os.getcwd()
        print(' ')
        print(' if you didnt know your file path then your file path is >>>> ',b)
        print(' ')
        kl = input('Press Enter to exit')
        exit()
    elif val == q:
        print(' ')
        print('     thanks for useing the script it will quit after 3 second')
        time.sleep(3)
        exit()
#(((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((
        
info_of_ip()

