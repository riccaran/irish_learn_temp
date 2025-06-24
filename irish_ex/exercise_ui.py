import tkinter as tk
import pandas as pd
import random

class IrishVerbPracticeApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Irish Verb Practice")
        self.master.configure(bg='black')

        self.load_data()
        self.create_widgets()

    def load_data(self):
        self.df = pd.read_csv("ir_verbs.csv", sep=";", encoding="utf-8")
        self.calculate_weights()

    def calculate_weights(self):
        n = self.df["score"].max() + 1
        categories = list(range(n))
        self.weights = [n - x for x in categories]
        self.scores_sets = [self.df[self.df["score"] == score].index.tolist() for score in range(11)]

    def create_widgets(self):
        self.label = tk.Label(self.master, text="Translate the English verb to Irish:", fg="white", bg="black", font=('Helvetica', 18))
        self.label.pack()

        self.verb_label = tk.Label(self.master, text="", font=('Helvetica', 24), fg="white", bg="black")
        self.verb_label.pack()

        self.entry = tk.Entry(self.master, font=('Helvetica', 18))
        self.entry.bind("<Return>", self.process_answer)
        self.entry.pack()

        self.result_label = tk.Label(self.master, text="", font=('Helvetica', 18), fg="white", bg="black")
        self.result_label.pack()

        self.progress_label = tk.Label(self.master, text="Progress: 0.00 %", font=('Helvetica', 18), fg="white", bg="black")
        self.progress_label.pack()

        self.leaderboard_label = tk.Label(self.master, text="", font=('Helvetica', 18), fg="white", bg="black", justify=tk.LEFT)
        self.leaderboard_label.pack()

        self.next_question()

    def next_question(self):
        category = []
        while not category:
            chosen_category = random.choices(range(len(self.scores_sets)), weights=self.weights, k=1)[0]
            category = self.scores_sets[chosen_category]
        pos = random.choice(category)
        self.current_verb = self.df.loc[pos]
        self.verb_label.config(text=self.current_verb["eng"])
        self.entry.delete(0, tk.END)

    def accents_conv(self, text):
        accents = {"à": "á", "è": "é", "ì": "í", "ò": "ó", "ù": "ú"}
        return ''.join(accents.get(char, char) for char in text)

    def process_answer(self, event):
        user_answer = self.accents_conv(self.entry.get().strip())
        correct_answer = self.current_verb["ir"]
        if user_answer == correct_answer:
            self.result_label.config(text="Correct!")
            if self.current_verb["score"] < 10:
                self.df.loc[self.current_verb.name, "score"] += 1
        else:
            self.result_label.config(text=f"Wrong! Correct answer was {correct_answer}")
            if self.current_verb["score"] > 0:
                self.df.loc[self.current_verb.name, "score"] -= 1

        self.df.to_csv("ir_verbs.csv", sep=";", index=False, encoding="utf-8")
        self.update_progress()
        self.update_leaderboard()
        self.next_question()

    def update_progress(self):
        progress = self.df["score"].mean() * 100
        self.progress_label.config(text=f"Progress: {progress:.2f} %")

    def update_leaderboard(self):
        sorted_verbs = self.df.sort_values(by="score", ascending=False)
        leaderboard_text = "Top Verbs:\n" + "\n".join([f"{verb['ir']} - {verb['score']}" for _, verb in sorted_verbs.head(10).iterrows()])
        self.leaderboard_label.config(text=leaderboard_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = IrishVerbPracticeApp(root)
    root.mainloop()
