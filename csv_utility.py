import csv
import dates_operations as do


def parse_csv(filename, today_date):
    # nella funzione di parsing del csv, passo come parametri il file csv da leggere e la data di oggi
    
    # converto la data di oggi
    today_days = do.days(today_date)
    
    # creo un dizionario dei dipendenti
    employee_dic = {}
    
    # creo un dizionario per i corsi con relativa scadenza
    course_dic = {}
    
    # creo una cache di date per evitare di ripetere più volte i calcoli delle varie date che si ripetono
    days_cache = {}
    
    # apro il csv
    with open(filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        
        # skippo la prima riga che contiene la leggenda della colonna
        next(csv_file)
        
        # leggo tutte le righe
        for line in csv_reader:

            # gestisco la cache delle date: se una certa data non è già stata calcolata, 
            # eseguo la sua conversione, calcolo la differenza con il giorno di oggi
            # e salvo il risultato in un dizionario per non dover ripetere il calcolo ogni volta che vedo la stessa data
            if line[3] not in days_cache:
                temp_days = do.days(line[3])
                days_cache.update({line[3] : temp_days - today_days})
                
                
            # se la data specifica rientra nella condizione 'mancano meno di 160 giorni a tale data'
            # inserisco il corso nel dizionario dei corsi
            if days_cache[line[3]] < 160 and days_cache[line[3]] > 0:
                
                if line[1] not in course_dic:
                    #course_dic.update({line[1] : days_cache[line[3]]})
                    course_dic[line[1]] = days_cache[line[3]]
                # else:
                #     course_dic[line[1]] = days_cache[line[3]]
                
                if line[0] not in employee_dic:
                    # employee_dic.update({line[0] : {line[1] : course_dic[line[1]]}})
                    employee_dic[line[0]] = {line[1] : course_dic[line[1]]}
                else:
                    # employee_dic[line[0]] = {line[1] : course_dic[line[1]]}
                    employee_dic.update({line[0] : {line[1] : course_dic[line[1]]}})
                
        return employee_dic       
        print(employee_dic)