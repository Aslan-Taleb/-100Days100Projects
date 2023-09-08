import pandas as pd


def dictionary_from_data_frame():
    df = pd.read_csv('nato_phonetic_alphabet.csv')
    dico = {row['letter']: row['code'] for index, row in df.iterrows()}
    return dico

def get_name():
    word = input("Enter a word : ")
    return word

def phonetic():
    dico = dictionary_from_data_frame()
    word = get_name().upper().replace(" ","")
    #result = [value for (key,value) in dico.items() if key in word]
    try:
        result = [dico[letter] for letter in word]
    except KeyError:
        print("You must provide a name not numbers.")
    else:
        print(result)



