# ++++++++++++++++ Factorial of Number ++++++++++++++

number = int(input('Plesae! Enter the Number whose Factorial You want: '))
Factorial = 1

while number > 0:
    Factorial = Factorial * number
    number = number - 1

print('Factorial Value of above Number ,', 'is', Factorial)