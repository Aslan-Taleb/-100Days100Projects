REPLACE = '[name]'


def create_letter():
    number_letter = 0
    with open("Input/Letters/starting_letter.txt", mode="r") as myLetter_file:
        with open("./Input/Names/refused_names.txt", mode="r") as names_file:
            myLetter_str = myLetter_file.read()
            names_str = names_file.read()
            names_str = names_str.replace(" ", "")
            names_list = names_str.split()
            for name in names_list:
                myLetter_str_new = myLetter_str.replace(REPLACE, name)
                with open(f"./Output/ReadyToSend_{name}.txt", mode="w") as readyToSend:
                    readyToSend.write(myLetter_str_new)
                    print(f"Letter Created For : {name}\n")
                    number_letter += 1
                myLetter_str_new = myLetter_str
    return number_letter
