# +++++++++++++++++ Positive Number Checker ++++++++++++++

numList = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10, 12]
positive_Number_Count = 0

for x in numList:
    if x > 0:
        positive_Number_Count = positive_Number_Count + 1
print('There are ', positive_Number_Count, 'Positive Numbers in the above List of Numbers')