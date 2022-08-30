# Matheus Tonini, Mauricio Ueso, Larissa Gouveia, Ezequiel Leandro e Henrique Medeiros - SIS

import psutil
import time
import datetime
from datetime import date
import math
import mysql.connector

# pretty library


i = 0
while (i < 5):
    i += 1
    try:
        db_connection = mysql.connector.connect(
           host='localhost', user='root', password='#Gf44456839813', database='MIC')
        print("Conectei no banco!")
    except mysql.connector.Error as error:
        if error.errno == errorcode.ER_BAD_DB_ERROR:
             print("Não encontrei o banco")
        elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
           print("Credenciais erradas")
        else:
           print(error)
        
    """ else:
    db_connection.close()
    print('connection close') """

    totalRAM =  round( (psutil.virtual_memory()[0]) * (10 ** -9),1)   
    totalVirtual =  round((psutil.virtual_memory()[1]) * (10 ** -8),1)
    totalDisco = round((psutil.disk_usage('/')[0]) * (10 ** -9))
    freqMax = round(((psutil.cpu_freq().max) / 1000),2)
    uploadPack = round((psutil.net_io_counters()[2]) * (10 ** -3))
    downloadPack = round((psutil.net_io_counters()[3]) * (10 ** -3))
    


    # print("\n")
    # print('--- CPU ---')
    # print("\n")

    PrcntCPU =  psutil.cpu_percent() 
    FreqCPU =  freqMax
    PortasLogicas = psutil.cpu_count()

    # print("\n")
    # print('--- Memoria RAM ---')
    # print("\n")
    
    TotalRAM = totalRAM
    PrcntRAM = psutil.virtual_memory()[2] 
    TotalVirtual = totalVirtual

    # print("\n")
    # print('--- Disco ---')
    # print("\n")

    TotalDisco = totalDisco
    PrcntDisco = psutil.disk_usage('/')[3] 

    # print("\n")
    # print('--- Rede ---')
    # print("\n")

    Upload = uploadPack
    Download = downloadPack
    DropDown = psutil.net_io_counters()[6]
    DropUp = psutil.net_io_counters()[7]


   #VARIAVEIS SIMULADOR 

    cpu1 = PrcntCPU
    memo1 = PrcntRAM
    disco1 = PrcntDisco

    disco2 = disco1 - (disco1 * 0.05)

    cpu3 = cpu1 + (cpu1 * 0.15) 
    memo3 = memo1 + (memo1 * 0.1)
    disco3 = (disco2 * 3)


    cpu2 = (cpu1 + (cpu1 * 1.10)) - (cpu3 - 1.05)
    memo2 = (memo1 + (memo1 * 0.15)) + (memo3 + 0.05)
   


    cursor = db_connection.cursor()

    fkmaquinaSim = 1
    sql = "INSERT INTO leitura (fkmaquinaSim, cpuLeitura, discoLeitura, memoriaLeitura) VALUES (%s,%s,%s,%s)"
    values = [fkmaquinaSim, cpu1, disco1, memo1]
    cursor.execute(sql, values)
   

    fkmaquinaSim = 2
    sql = "INSERT INTO leitura(fkmaquinaSim, cpuLeitura, discoLeitura, memoriaLeitura) VALUES (%s,%s,%s,%s)"
    values = [fkmaquinaSim, cpu2, disco2, memo2]
    cursor.execute(sql, values)
    
   
    fkmaquinaSim = 3
    sql = "INSERT INTO leitura (fkmaquinaSim, cpuLeitura, discoLeitura, memoriaLeitura) VALUES (%s,%s,%s,%s)"
    values = [fkmaquinaSim, cpu3, disco3, memo3]
    cursor.execute(sql, values)
    

    print()
    print(cursor.rowcount, "Inseri no banco")

    db_connection.commit()
    db_connection.close()


   
    time.sleep(3) #tempo de 3 segundos para a repetição
    print("Processo finalizado!")