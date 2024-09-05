# ++++++++++++++++ Prime Number Checker ++++++++++++++++

userInput = int(input('Please number till where you want to check prime numbers: '))

for num in range(2,userInput):
        if userInput % num == 0:
            print('Not Prime Number')
            break
        else:
            print('Prime Number')
            break