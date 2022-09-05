import psutil
import time
import datetime
from datetime import date
import math
import mysql.connector


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

    #VARIAVEIS SIMULADOR 

    PrcntCPU =  psutil.cpu_percent() 
    PortasLogicas = psutil.cpu_count()

    PrcntRAM = psutil.virtual_memory()[2] 
    
    PrcntDisco = psutil.disk_usage('/')[3] 
 
    TotalVirtual =  round((psutil.virtual_memory()[1]) * (10 ** -8),1)
    uploadPack = round((psutil.net_io_counters()[2]) * (10 ** -3))
    downloadPack = round((psutil.net_io_counters()[3]) * (10 ** -3))

    Upload = uploadPack
    Download = downloadPack
    DropDown = psutil.net_io_counters()[6]
    DropUp = psutil.net_io_counters()[7]
    
    DataHora = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')

    cpu1 = PrcntCPU
    cpu2 = (cpu1 + (cpu1 * 0.1)) 
    cpu3 = cpu2 + (cpu2 * 0.05) 

    memo1 = PrcntRAM
    memo2 = memo1 + (memo1 * 0.15)
    memo3 = memo1 + (memo1 * 0.05)

    disco1 = PrcntDisco
    disco2 = disco1 - (disco1 * 0.05)
    disco3 = disco2 * 3

    cursor = db_connection.cursor()

    fkMaquina = 1
    sql = "INSERT INTO leitura (fkMaquina,DataHora,PrcntCPU,PortasLogicas,PrcntRAM,TotalVirtual,PrcntDisco,Upload,Download,DropDown,DropUp) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    values = [fkMaquina, DataHora, cpu1, PortasLogicas, memo1, TotalVirtual, disco1, Upload, Download, DropDown, DropUp]
    cursor.execute(sql, values)
    current_date = date.today()
    formatted_date = current_date.strftime('%d/%m/%Y')

    fkMaquina = 2
    sql = "INSERT INTO leitura (fkMaquina,DataHora,PrcntCPU,PortasLogicas,PrcntRAM,TotalVirtual,PrcntDisco,Upload,Download,DropDown,DropUp) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    values = [fkMaquina, DataHora, cpu2, PortasLogicas, memo2, TotalVirtual, disco2, Upload, Download, DropDown, DropUp]
    cursor.execute(sql, values)
    current_date = date.today()
    formatted_date = current_date.strftime('%d/%m/%Y')

    fkMaquina = 3
    sql = "INSERT INTO leitura (fkMaquina,DataHora,PrcntCPU,PortasLogicas,PrcntRAM,TotalVirtual,PrcntDisco,Upload,Download,DropDown,DropUp) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    values = [fkMaquina, DataHora, cpu3, PortasLogicas, memo3, TotalVirtual, disco3, Upload, Download, DropDown, DropUp]
    cursor.execute(sql, values)
    current_date = date.today()
    formatted_date = current_date.strftime('%d/%m/%Y')

    print(formatted_date)
    print(cursor.rowcount, "Inseri no banco")
    db_connection.commit()
    db_connection.close()


   
    time.sleep(3) #tempo de 3 segundos para a repetição
    print("Processo finalizado!")

    # Grupo 09
    # EZEQUIEL LEANDRO JUNGE DA SILVA           RA:03221063
    # HENRIQUE MEDEIROS ALVES                   RA:03221029
    # LARISSA DA SILVA GOUVEIA                  RA:03221031
    # MATHEUS TONINI MATSUMOTO PANTELEÃO        RA:03221025
    # MAURICIO UESSO MARTINS                    RA:03221039

