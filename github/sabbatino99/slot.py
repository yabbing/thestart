def deposit():
    while True:
        amount = input('What would you like to deposit $')
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print('Amount must be great than 0.')
        else:
            print('Please Enter a number.')
    
    return amount