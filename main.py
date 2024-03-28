import smtplib                   # modulo per email
import openpyxl                  # modulo per leggere excel .xlsx (solo questo formato!)
import dates_operations  as do   # script esterno creato per gestire le date



if __name__ == "__main__":

    today = do.get_today_date()
    print(f'Oggi è il {today}.')
    expiration = input('expire dd/mm/yyyy: ')
    
    difference_between_dates = do.days(expiration) - do.days(today)
    
    print(f'tot is {difference_between_dates}')