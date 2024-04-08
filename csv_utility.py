import csv
import dates_operations  as do              # script esterno creato per gestire le date


def parse_csv(filename):
    # nella funzione di parsing del csv, passo come parametri il file csv da leggere e la data di oggi
    
    # converto la data di oggi
    today_days = do.days(do.get_today_date())
    
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
            first_name = line[0]
            last_name = line[1]
            course = line[2]
            exp = line[4]
            
            
            tmp_name = f'{last_name} {first_name}'

            # gestisco la cache delle date: se una certa data non è già stata calcolata, 
            # eseguo la sua conversione, calcolo la differenza con il giorno di oggi
            # e salvo il risultato in un dizionario per non dover ripetere il calcolo ogni volta che vedo la stessa data
            if exp not in days_cache:
                temp_days = do.days(exp)
                days_cache.update({exp : temp_days - today_days})
                
                
            # se la data specifica rientra nella condizione 'mancano meno di 160 giorni a tale data'
            # inserisco il corso nel dizionario dei corsi
            # la struttura è quanto segue:
            # dizionario dei corsi = { corso : giorni alla scadenza }
            # dizionario dei dipendenti = { nome : { corso : gg, corso : gg }, nome : { corso : gg } }
            # i dati vengono aggiunti al dizionario solo se non esistono già
            
            if days_cache[exp] < 160 and days_cache[exp] > 0:
                if course not in course_dic:
                    course_dic[course] = days_cache[exp]
                    
                if tmp_name not in employee_dic:
                    employee_dic[tmp_name] = {course: course_dic[course]}
                else:
                    if course not in employee_dic[tmp_name]:
                        employee_dic[tmp_name][course] = course_dic[course]

                
        # ritorna il dizionario per permettere a main di proseguire con la mail
        return employee_dic       
    
    
    
def parse_formazione_csv(filename):
    
    # ricevo e converto la data di oggi
    today_days = do.days(do.get_today_date())
    
    corsi = []
    scadenze = []
    
    with open(filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        
        # le prime 3 righe sono vuote
        next(csv_file)
        next(csv_file)
        next(csv_file)
        
        # leggo le righe del file
        
        for line in csv_reader:
            for cell in line:
                if cell != 'None':
                    print(cell)
            
            # # salvo i corsi
            # for cell in line:
            #     if cell != '':
            #         corsi.append(cell)
                    
        print(corsi)
        
    csv_file.close()
        
        