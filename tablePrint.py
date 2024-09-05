# ++++++++++++++++ Table Printer with Skipping the fifth Iteration ++++++++++++++++

table_of = int(input("What Digit Table Do You want to Print "))
limit_Number = int(input("Please Enter a number till where you want the Tables of "))

for num in range(1,limit_Number+1):
    if num == 5:
        continue
    print(table_of, 'X', num, '=', table_of * num)