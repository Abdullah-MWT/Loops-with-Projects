# +++++++++++++ Even Number Sum ++++++++++++++

# limit_Number = int(input("Please Enter the Number till where you want the Sum of Even Numbers "))
# sum_Even_Num = 0

# for num in range(1, limit_Number+1):
#     if num % 2 == 0:
#         sum_Even_Num += 1
#         print(num)
# print('There are', sum_Even_Num, 'Even Numbers till', limit_Number)


# +++++++++++++ Odd Number Sum ++++++++++++++
limit_Num = int(input('Please Enter the Number till where you want the Sum of Odd Numbers: '))
sum_Odd_Num = 0

for num in range(1,limit_Num+1):
    if num % 2 != 0:
        sum_Odd_Num += 1
        print(num)
    
print('There are', sum_Odd_Num, 'Odd Numbers till', limit_Num)
        