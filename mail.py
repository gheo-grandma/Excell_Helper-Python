from smtplib import SMTP                            # modulo per email
from email.mime.multipart import MIMEMultipart      # moduli per la formattazione del corpo della mail
from email.mime.text import MIMEText
from conf import Credentials                        # file con credenziali, mail e pw


def send(body):
    
    mail_credentials = Credentials()
    
    sender_email = mail_credentials.get_sender()
    receiver_email = mail_credentials.get_receiver()
    pw = mail_credentials.get_pw()
    
    # creo la email in tutte le sue parti
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = 'Corsi in scadenza'
    
    # mi assicuro di allegare correttasmente la mail formattata come corpo
    msg.attach(MIMEText(body, 'plain'))

    # converto le info fornattate a stringa
    email_text = msg.as_string()
    
    
    # avvio il server per l'invio della mail
    
    # questi valori cambiano insieme in base al servizio che viene usato
    server = SMTP('smtp.gmail.com', 587)
    
    # creo una connessione sicura con SSL o TLS
    server.starttls()
    
    # username, password ( la password non è la stessa dell'account, bensì la password per le app terze parti generata apposta da google )
    server.login(receiver_email, pw)
    
    # sender, receiver, message
    server.sendmail(receiver_email, receiver_email, email_text)
    
    
    # chiudo la connessione
    server.quit()