import openpyxl                             # modulo per leggere excel .xlsx (solo questo formato!)
import dates_operations  as do              # script esterno creato per gestire le date
from smtplib import SMTP                    # modulo per email



def login_to_mail(body):
    
    # address, port number
    # questi valori cambiano insieme in base al servizio che viene usato
    server = SMTP('smtp.gmail.com', 587)
    
    
    # creao una connessione sicura con SSL o TLS
    server.starttls()
    
    # username, password
    server.login('bonetto.matteof@gmail.com', 'uojtdczjuoetpuxg')
    
    # sender, receiver, message
    server.sendmail('matthew.bonetto@gmail.com', 'bonetto.matteof@gmail.com', body)
    
    print('Mail sent')



if __name__ == "__main__":
    

    today = do.get_today_date()
    print(f'Oggi è il {today}.')   
    expiration = input('expire dd/mm/yyyy: ')  
    
    difference_between_dates = do.days(expiration) - do.days(today)
    
    login_to_mail(f'Ciao vecio! mancano {difference_between_dates} giorni a {expiration}.')
    
    print(f'tot is {difference_between_dates}')