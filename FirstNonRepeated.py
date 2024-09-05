# +++++++++++++ Find First Non Repeated Character ++++++++++++++


string = input("Please Enter a String: ")

for char in string:
    if string.count(char) == 1:
        print(char)
        break



