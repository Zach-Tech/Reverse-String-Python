this_thing = 1
while this_thing == 1:
    txt = input("Enter a string to reverse: ")
    print(txt[::-1])
    ext_input = input("Continue? (Y/N): ")
    if ext_input == "Y".lower():
        continue
    elif ext_input == "N".lower():
        exit()
    elif print("Improper response, please try again"):
        continue
