# ++++++++++++++++ Validate Input ++++++++++++++++

while True:
    number = int(input('Enter a number between between 1-10: '))
    if 1 <= number <= 10:
        print('Thanks')
        break
    else:
        print('Invalid Number, Try Again')
    

