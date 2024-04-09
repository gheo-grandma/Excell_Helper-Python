import datetime             # modulo per la data di oggi


# datetime:

# datetime.time.today() -> data di oggi yyyy-mm-dd
# con la funzione strftime() posso formattare la data come voglio, scrivendola come f string
# %d -> giorno
# %m -> mese
# %Y -> anno
# %B -> mese scritto a parola



def days(date):
    # Questa funzione serve a convertire la data in numero di giorni dall'anno 0.
    # Questa variabile servirà poi per calcolare la differenza tra due date espressa in giorni.


    # lista con il numero di giorni per ciascun mese
    calender = [
        31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
        ]
 
    # dati presi dalla data
    # gestione di casi in cui le date siano scritte in maniera diversa dal previsto
    match len(date): 
        
        # 2019-12-01 00:00:00
        case 19:
            # yyyy/mm/dd
            dds = date[8] + date[9]
            mms = date[5] + date[6]
            yys = date[0] + date[1] + date[2] + date[3]
            
            # conversione dei dati in cifre (int)
            dd = int(dds)
            mm = int(mms)
            yy = int(yys)
            
        case 10:
            # yyyy/mm/dd
            dds = date[8] + date[9]
            mms = date[5] + date[6]
            yys = date[0] + date[1] + date[2] + date[3]
            
            # conversione dei dati in cifre (int)
            dd = int(dds)
            mm = int(mms)
            yy = int(yys)
            
        # case 7:
        #     # yyyy/mm
        #     mms = date[5] + date[6]
        #     yys = date[0] + date[1] + date[2] + date[3]
            
        #     dd = 1
        #     mm = int(mms)
        #     yy = int(yys)
            
        # case 4:
        #     # yyyy
        #     yys = date[0] + date[1] + date[2] + date[3]
            
        #     dd = 1
        #     mm = 1
        #     yy = int(yys)
    
    
        # formato della data errato
        case _:
            return -1

    
    # per convertire le date in numero di giorni, seguiamo un algoritmo semplice
    
    # prendiamo in considerazione tutti i giorni dall'anno 0 all'anno precedente
    # includiamo nel conteggio gli anni bisestili: anni // 4 = anni bisestili passati
    
    # contiamo poi i giorni passati dall'inizio di quest'anno fino al mese precedente
    
    # arrivati al mese attuale, calcoliamo solo i giorni passati
    # se abbiamo superato gennaio, calcoliamo se l'anno è bisestile
    previous_year = (365 * (yy -1)) + (yy-1)//4
    this_year = 0
    for i in range (mm -1):
        this_year += calender[i]
    
    this_year += dd
    
    if mm > 1:
        if yy % 4 == 0:
            this_year += 1
            

    # ritorno della data convertita
    return this_year + previous_year
    
def get_today_date():
    # date is retrieved as yyyy-mm-dd
    temp = datetime.date.today()
    formatted_date = temp.strftime('%Y-%m-%d')
    
    return formatted_date