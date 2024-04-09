import openpyxl
from openpyxl import Workbook, load_workbook
import os

def convert_xl_to_csv(xl_filename, csv_filename):
    
    
    # imposto il percorso del file excel 
    # il file deve risiedere nel desktop in ogni momento
    excel_file_path = os.path.expanduser(f"~/Desktop/{xl_filename}")
    
    book = load_workbook(excel_file_path, data_only=True)
    sheet = book.active
    
    # ricevo le righe
    data = sheet.rows
    
    # apro/creo il file csv
    csv_file = open(csv_filename, 'w+')
    
    
    # leggo i dati
    for row in data:
        # salvo le celle della riga in una lista
        l = list(row)
        
        # leggo ogni elemento nella riga e scrivo il rispettivo valore nel file
        # se sono arrivato alla fine della riga, scrivo solo il valore, altrimenti aggiungo una virgola
        # terminata la riga aggiungo \n
        # chiudo il file quando ho finito
        
        for i in range(len(l)):
            string_to_write = ''
            string_to_write = str(l[i].value)
            
            if i != len(l) - 1:
                string_to_write += '|'

            csv_file.write(string_to_write)
            string_to_write = ''
            
        csv_file.write('\n')        
    
    print(f'Worksheet = {sheet}')

            
    csv_file.close()