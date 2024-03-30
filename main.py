import openpyxl                             # modulo per leggere excel .xlsx (solo questo formato!)
import mail                                 # script esterno creato per login ed invio della email
import csv_utility                          # script esterno creato per la gestione della lettura dei file csv



if __name__ == "__main__":
    
    # ricevo la data formattata tramite lo script
    # today = do.get_today_date()
    # print(f'Oggi è il {today}.')  
    
    
    output = "Buongiorno Eleonora ❤️ Sono in scadenza i seguenti corsi per i seguenti dipendenti:\n"
    
    output_dictionary = csv_utility.parse_csv('csv_prova.csv')
    
    # se ci sono dati da visualizzare prepara il corpo della mail
    if output_dictionary:
        for nomi, corsi in output_dictionary.items():
            output += f'- {nomi}: '
            
            for corso, giorni in corsi.items():
                output += f'{corso} ({giorni} giorni alla scadenza), '
                
            output = output[:-2]
            output += f'.\n'
            
        # invia la mail solo se ci sono corsi da visualizzare, aka se il dizionario non è vuoto
        print(output)
        #mail.send(output)
        
    else:
        print('Nessun valore')
        
        
        
        
        
# >>>>>>>>>>>>>>> inserisco la data da cui calcolare i giorni rimasti 
    # >>>>>>>>>>>>>>> expiration = input('expire dd/mm/yyyy: ')  
    
    
    # difference_between_dates = do.days(expiration) - do.days(today)
    
    # invio la email 
    #mail.send(f'Ciao vecio! mancano {difference_between_dates} giorni a {expiration}.')
    
    #   >>>>> print(f'tot is {difference_between_dates}')
    
    
    # cosa resa da fare: implementare la lettura dal file xlsx
    # eseguire lo script in questo modo:
    # creao un dizionario: {nome_dipendente : {nome_del_corso : giorni rimasti alla scadeza}}
    # esempio:
    # corsi_in_scadenza = {
    #     'Matteo Bonetto' : {
    #         'transpallet elettrico' : 126,
    #         'scaffali' : 154,
    #         'cassa' : 67
    #     },
        
    #     'Eleonora Mori' : {
    #         'scaffali' : 154,
    #         'sicurezza' : 139
    #     } 
    # } 
    
    # il nome del dipendente diventa la chiave primaria del dizionario dei dipendenti
    # ad ogni dipendente viene associato un dizionario che ha come chiave il nome del corso e come valore i giorni rimanenti alla scadenza del corso
    # il corpo della mail viene formattato così: nome del dipendente, li sta dei corsi in scadenza
    # esempio:
    
    # messaggio_esempio = f'Sono in scadenza per Matteo Bonetto i corsi transpallet elettrico (126 giorni), scaffali (154 giorni), cassa (67 giorni).\nSono in scadenza per Eleonora Mori i corsi scaffali (154 giorni), sicurezza (139 giorni)'
    
    # nella funzione per il controllo dei giorni in scadenza è peresente un dizionario di cache per ottimizzare la memoria:
    # quando viene riscontrata una data, se non è presente nella cache viene inserita come chiave, mentre il suo valore è il risultato del calcolo
    # il risultato del calcolo viene già inserito nel dizionario dei dipendenti