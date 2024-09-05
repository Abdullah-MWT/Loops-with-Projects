# +++++++++++++ Reverse String ++++++++++++++

enter_String = input("Please Enter a String: ")
reversed_String = ""

for char in enter_String:
    reversed_String = char + reversed_String

print(reversed_String)

