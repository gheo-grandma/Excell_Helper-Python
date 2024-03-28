def days(date):
    calender = [
        31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
        ]
 
    dds = date[0] + date[1]
    mms = date[3] + date[4]
    yys = date[6] + date[7] + date[8] + date[9]
    
    dd = int(dds)
    mm = int(mms)
    yy = int(yys)
    
    # print(f'today is {dd}/{mm}/{yy}')
    
    previous_year = (365 * (yy -1)) + (yy-1)//4
    this_year = 0
    for i in range (mm -1):
        this_year += calender[i]
    
    this_year += dd
    
    if mm > 1:
        if yy % 4 == 0:
            this_year += 1
            
    return this_year + previous_year
    




if __name__ == "__main__":
    today = input('today dd/mm/yyyy: ')
    expiration = input('expire dd/mm/yyyy: ')
    print(f'tot is {days(expiration) - days(today)}')