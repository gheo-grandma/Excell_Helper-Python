import openpyxl
from openpyxl import Workbook, load_workbook

def convert_xl_to_csv(xl_filename, csv_filename):
    book = load_workbook(xl_filename)
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
            if i == len(l) - 1:
                csv_file.write(str(l[i].value))
            else:
                csv_file.write(str(l[i].value) + ',')
        csv_file.write('\n')
        
    csv_file.close()
        
    
    print(sheet)