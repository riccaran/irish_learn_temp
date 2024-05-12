import pandas as pd
import random

path = "ir_verbs.csv"

def load_dataset(path):
    verbs_df = pd.read_csv(path, sep=";", encoding="utf-8")
    verbs_df = verbs_df[verbs_df["used"] == 1][["ir", "eng"]].reset_index()
    nums = verbs_df.index
    return verbs_df, nums

def find_origin():
    origin = input("Translate from: ")
    targets = ("eng", "ir")

    for p_target in targets:
        if origin != p_target:
            target = p_target

    return origin, target

def find_terms(origin, target):
    terms = verbs_df.iloc[random.choice(nums), :]

    term = terms[origin]
    translation = terms[target]

    return term, translation

def start_exercise():
    times = input("Number of questions:")
    print()
    for time in range(int(times)):
        term, translation = find_terms(origin, target)
        print(term)
        input("Translation: ")
        print("Actual translation: {}\n".format(translation))

if __name__ == "__main__":
    verbs_df, nums = load_dataset(path)
    origin, target = find_origin()
    start_exercise()
    input("Press 'Enter' to close")

