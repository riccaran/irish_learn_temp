import pandas as pd
import random

times = input("Number of questions: ")

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

for time in range(int(times)):
    df_dict = pd.read_csv("ir_verbs.csv", sep = ";", encoding = "utf-8")

    # Choose category
    scores_dict = df_dict["score"]
    scores_sets = [scores_dict[scores_dict == score].index for score in range(11)]

    n = df_dict["score"].max() + 1
    categories = list(range(n))
    weights = [n - x for x in categories]
    chosen_category = random.choices(categories, weights=weights, k=1)[0]
    category = scores_sets[chosen_category]

    while len(category) == 0:
        chosen_category = random.choices(categories, weights=weights, k=1)[0]
        category = scores_sets[chosen_category]

    # Chose position
    pos = random.choices(category)[0]

    ir_word, eng_word, prev_score = df_dict.iloc[pos]

    print("{}. {}".format(time + 1, eng_word))
    answer = input("Translation: ")
    print("Actual translation: {}".format(ir_word))
    answer = accents_conv(answer)

    if (answer == ir_word) and (prev_score != 10):
        df_dict.loc[pos, "score"] += 1
    elif (answer == ir_word) and (prev_score != 0):
        df_dict.loc[pos, "score"] -= 1

    print("\nprevious score: {}".format(prev_score))
    print("new score: {}\n".format(df_dict["score"].iloc[pos]))

    df_dict.to_csv("ir_verbs.csv", index = False, sep = ";", encoding = "utf-8")

progress = df_dict["score"].mean()

print("Total progress: {:.4f} %".format(progress * 10, 4))
input("Press 'Enter' to close")