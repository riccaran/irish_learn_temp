import pandas as pd
import os
import random
import json
import numpy as np
import tkinter as tk
from tkinter import Label, Entry, Button, Scrollbar, Frame, Listbox, END

# Processing functions
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

# UI Application
class VerbConjugationApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Irish Verb Conjugation Practice")
        self.geometry("800x600")  # Adjust the window size if necessary
        self.configure(bg='#333333')  # Set background color to a dark grey
        self.create_widgets()
        self.previous_answers = []

    def create_widgets(self):
        # User instructions
        self.label = Label(self, text="Click 'Start' to begin the quiz.", font=('Helvetica', 16, 'bold'), bg='#333333', fg='#FFFFFF')
        self.label.pack(pady=20)

        # Start button
        self.start_button = Button(self, text="Start", command=self.load_question, font=('Helvetica', 14, 'bold'), bg='#555555', fg='#00FF00')
        self.start_button.pack(pady=10)

        # Entry field for user answer
        self.user_answer = Entry(self, font=('Helvetica', 14), width=50, bg='#555555', fg='#FFFFFF')
        self.user_answer.pack(pady=10)
        self.user_answer.bind("<Return>", self.check_answer)  # Bind the return key

        # Submit button
        self.submit_button = Button(self, text="Submit", command=self.check_answer, font=('Helvetica', 14, 'bold'), bg='#555555', fg='#000000')
        self.submit_button.pack(pady=10)

        # Frame for the list of previous answers
        self.answers_frame = Frame(self)
        self.answers_frame.pack(fill=tk.BOTH, expand=True)
        self.answers_scrollbar = Scrollbar(self.answers_frame)
        self.answers_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.answers_list = Listbox(self.answers_frame, font=('Helvetica', 14), bg='#333333', fg='#FFFFFF', yscrollcommand=self.answers_scrollbar.set)
        self.answers_scrollbar.config(command=self.answers_list.yview)
        self.answers_list.pack(fill=tk.BOTH, expand=True)

    def load_question(self):
        verbs = [verb.split(".")[0] for verb in os.listdir("conjugations") if verb.endswith("json")]
        df_dict = pd.read_csv("ir_verbs.csv", sep=";", encoding="utf-8")

        self.file_verb = random.choice(verbs)
        verb = process_letters(self.file_verb)
        translation = df_dict[df_dict["ir"] == verb]["eng"].values[0]

        with open(f"conjugations/{self.file_verb}.json", "r") as f:
            verb_d = json.load(f)
            x = dict()
            x["Present"] = verb_d["present"] # tenses
            x["Past"] = verb_d["past"]
            
            self.verb_conj = x

        test_choice = conj_choice(self.verb_conj).split("-")
        self.conj_test = test_choice[:-1]
        self.conj_answer = test_choice[-1]

        self.label.config(text=f"Verb: {verb} (translation: {translation})\nConjugation: {' - '.join(self.conj_test)}")
        self.user_answer.delete(0, tk.END)

    def check_answer(self, event=None):  # 'event' parameter to handle the key bind
        user_input = self.user_answer.get()
        correct_answer = accents_conv(self.conj_answer)
        result_text = f"Verb: {' - '.join(self.conj_test)} - Your answer: {user_input} / Correct answer: {correct_answer}"
        if accents_conv(user_input) == correct_answer:
            self.answers_list.insert(END, result_text + " - Correct!")
            self.answers_list.itemconfig(END, {'bg': '#006400', 'fg': '#FFFFFF'})  # Dark green with white text
        else:
            self.answers_list.insert(END, result_text + " - Incorrect!")
            self.answers_list.itemconfig(END, {'bg': '#8B0000', 'fg': '#FFFFFF'})  # Dark red with white text
        self.answers_list.see(END)  # Automatically scroll to the end
        self.load_question()

# Run the application
if __name__ == "__main__":
    app = VerbConjugationApp()
    app.mainloop()
