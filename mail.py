from smtplib import SMTP                    # modulo per email


def send(body):
    
    # address, port number
    # questi valori cambiano insieme in base al servizio che viene usato
    server = SMTP('smtp.gmail.com', 587)
    
    
    # creao una connessione sicura con SSL o TLS
    server.starttls()
    
    # username, password ( la password non è la stessa dell'account, bensì la password per le app terze parti generata apposta da google )
    server.login('bonetto.matteof@gmail.com', 'uojtdczjuoetpuxg')
    
    # sender, receiver, message
    server.sendmail('matthew.bonetto@gmail.com', 'bonetto.matteof@gmail.com', body)
    
    print('Mail sent')