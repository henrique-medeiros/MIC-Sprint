from pickletools import decimalnl_short
from unicodedata import decimal
import psutil
import time
import os
import math
#pretty library

totalRAM =  round( (psutil.virtual_memory()[0]) * (10 ** -9),1)   
totalVirtual =  round((psutil.virtual_memory()[1]) * (10 ** -8),1)
totalDisco = round((psutil.disk_usage('/')[0]) * (10 ** -9))
freqMax = round(((psutil.cpu_freq().max) / 1000),2)
uploadPack = round((psutil.net_io_counters()[2]) * (10 ** -3))
downloadPack = round((psutil.net_io_counters()[3]) * (10 ** -3))

while True:
    print()
    print()
    print('--- CPU ---')
    print()

    print('A CPU esta utilizando (%): ', psutil.cpu_percent()) 
    print('Frquencia maxima da CPU (GHz):', freqMax) 
    print('Numero de portas logicas', psutil.cpu_count()) 

    print()
    print('--- Memoria RAM ---')
    print()
    
    print('Total de memoria RAM (GB):', totalRAM) 
    print('Memoria RAM utilizada (%):', psutil.virtual_memory()[2]) 
    print('Total de Memoria virtual(GB):', totalVirtual) 

    print()
    print('--- Disco ---')
    print()

    print('Total de Disco (GB):', totalDisco) 
    print('Disco utilizado (%):', psutil.disk_usage('/')[3]) 

    print()
    print('--- Rede ---')
    print()

    print('Package Upload (Kbps):', uploadPack)
    print('Package Download(Kbps):', downloadPack)
    print('Drop de Download:', psutil.net_io_counters()[6])
    print('Drop de Upload:', psutil.net_io_counters()[7])






    
   
   
    time.sleep(3) #tempo de 3 segundos para a repetição