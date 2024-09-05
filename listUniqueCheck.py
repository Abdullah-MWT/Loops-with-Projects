# ++++++++++++++++ List Unique Checker ++++++++++++++++

List = ['Mango', 'Apple', 'Banana', 'Mango', 'Apple']

unique_item = set()

for item in List:
    if item in unique_item:
        print('Duplicate Found', item)
        break
    else:
        unique_item.add(item)
        print('No Duplicate Found')

