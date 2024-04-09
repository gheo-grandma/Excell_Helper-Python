import csv
import dates_operations  as do              # script esterno creato per gestire le date
import save_course                          # script esterno per rendere più leggibile il nome del corso


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
    
    # tutti i corsi in ordine da sx a dx
    corsi = []
    
    # gli indici delle colonne in cui si trovano i vari corsi in ordine da sx a dx
    scadenze = []
    
    # la scadenza del corso corsi[x] si troverà nella colonna scadenze[x] nella riga del dipendente a
    
    
    
    # creo una cache per non calcolare più volte la stessa data
    days_cache = {}
    
    # creo i vari dizionari
    corsi_dipendente = {}
    dipendenti = {}
    
    with open(filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = '|')
        
        # con questa variabile posso determinare in quale riga mi trovo
        line_counter = 0
        
        # leggo le righe del file
        for line in csv_reader:
        
            match line_counter - 3:                 
            # salvo i corsi
                case 0:
                    for i in range(len(line)):
                        if line[i] != 'None' and line[i] != 'GENERALE':
                            corsi.append(line[i])
                            
                # salvo gli indici delle scadenze
                case 1:
                    for i in range(len(line)):
                        if line[i] == 'SCADENZA AGGIORNAMENTO':
                            scadenze.append(i)
                            
                # leggo ora i dati dei dipendenti
                case _:
                    name = line[0]
                    
                    # scorro tra le scadenze
                    for i in range(len(scadenze)):
                        s = scadenze[i]
                        
                        temp_corso = {}
                        
                        # se è scritto un valore
                        if line[s] != 'None':
                            
                            # aggiorno la chache dei giorni se mancano
                            if s not in days_cache:
                                days_cache.update({line[s] : do.days(line[s]) - today_days})
                            
                            # procedo con il json solo se la condizione è valida
                            remainig_days = days_cache[line[s]]
                            if remainig_days <= 120 and remainig_days > 0:
                                corso = save_course.prettify_course(corsi[i])
                                
                                # aggiorno il corso per il dipendente
                                if corso not in temp_corso:
                                    temp_corso.update({corso : remainig_days})
                                    
                                # aggiorno i dipendenti con i corsi
                                if name not in dipendenti:
                                    dipendenti.update({name : temp_corso})
                                else:
                                    dipendenti[line[0]][corso] = remainig_days
                                        
                            
            line_counter += 1
        
    csv_file.close()
    
    print(scadenze)
    
    for i in corsi:
        print(i)

    
    return dipendenti
        