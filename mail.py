from smtplib import SMTP                    # modulo per email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send(body):
    
    sender_email = 'matthew.bonetto@gmail.com'
    receiver_email = 'bonetto.matteof@gmail.com'
    
    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = 'Corsi in scadenza'
    
    # Attach the email body
    msg.attach(MIMEText(body, 'plain'))

    # Convert the email body to a string
    email_text = msg.as_string()
    
    # address, port number
    # questi valori cambiano insieme in base al servizio che viene usato
    server = SMTP('smtp.gmail.com', 587)
    
    
    # creao una connessione sicura con SSL o TLS
    server.starttls()
    
    # username, password ( la password non è la stessa dell'account, bensì la password per le app terze parti generata apposta da google )
    server.login(receiver_email, 'uojtdczjuoetpuxg')
    
    # sender, receiver, message
    server.sendmail(sender_email, receiver_email, email_text)
    
    
    
    server.quit()
    print('Mail sent')