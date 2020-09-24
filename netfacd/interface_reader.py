#!/usr/bin/env python3



import netifaces



print(netifaces.interfaces())


for i in netifaces.interfaces():

        print('\n**************Details of Interface - ' + i + ' *********************')

        try:

            print('MAC: ', end='') # This print statement will always print MAC withoutan end of line

            print(netifaces.ifaddresses(i))

            print(netifaces.ifaddresses(i)[netifaces.AF_LINK])

            print(netifaces.ifaddresses(i)[netifaces.AF_LINK][0]['addr']) # prints the mac address

            print('IP: ', end='') # This print statement will always print IP withoutan end of line

            print(netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr']) # prints the ip address
        
        except: #This is a new line

            print('Could not collect adapter information') # Print an error message
