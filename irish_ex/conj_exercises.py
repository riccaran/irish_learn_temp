import pandas as pd
import os
import random
import json
import numpy as np

####

def process_letters(word):
    accents = {
        "a_x": "á",
        "e_x": "é",
        "i_x": "í",
        "o_x": "ó",
        "u_x": "ú"
    }
    for key, value in accents.items():
        word = word.replace(key, value)
    return word

def accents_conv(text):
    accents = {
        "à": "á",
        "è": "é",
        "ì": "í",
        "ò": "ó",
        "ù": "ú"
    }

    characters = list(text)

    for i in range(len(characters)):
        if characters[i] in accents:
            characters[i] = accents[characters[i]]

    return ''.join(characters)

def conj_choice(verb):
    if type(verb) == str:
        return verb
    choice = np.random.choice(list(verb.keys()))
    return choice + '-' + conj_choice(verb[choice])

times = input("Number of questions: ")

for time in range(int(times)):
    ####
    verbs = [verb.split(".")[0] for verb in os.listdir("conjugations") if verb.endswith("json")]
    df_dict = pd.read_csv("ir_verbs.csv", sep = ";", encoding = "utf-8")

    file_verb = random.choice(verbs)
    verb = process_letters(file_verb)
    translation = df_dict[df_dict["ir"] == process_letters(verb)]["eng"].values[0]

    with open("conjugations/{}.json".format(file_verb), "r") as f:
        verb_conj = json.load(f)["present"]

    ####
    test_choice = conj_choice(verb_conj).split("-")
    conj_test = test_choice[:-1]
    conj_answer = test_choice[-1]

    print("Verb: {} (translation: {})".format(verb, translation))
    print("Conjugation: {}".format(" - ".join(conj_test)))
    user_answer = input("Answer: ")
    print("\nYour Answer: {}\nActual anser: {}\n".format(accents_conv(user_answer), conj_answer))

input("Quiz ended. Press 'Enter' to close")
