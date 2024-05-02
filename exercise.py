import pandas as pd
import random

times = input("Number of times: ")

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
    df_dict = pd.read_csv("ir_dict.csv", sep = ";", encoding = "latin-1")

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

    word, meaning, translation, _ = df_dict.iloc[pos]

    df_translations = df_dict[(df_dict["eng"] == word) & (df_dict["meaning"] == meaning)]
    translations = df_translations["ir"].values

    print("{}. {} (meaning: {})".format(time + 1, word, meaning))
    answer = input()

    answer = accents_conv(answer)

    #print(answer)
    print(translation)

    prev_score = df_dict["score"].iloc[pos]

    if (answer in translations) and (prev_score != 10):
        for pos in df_translations.index:
            df_dict.loc[pos, "score"] += 1
    elif (answer not in translations) and (prev_score != 0):
        for pos in df_translations.index:
            df_dict.loc[pos, "score"] -= 1

    print("\nprevious score: {}".format(prev_score))
    print("new score: {}\n".format(df_dict["score"].iloc[pos]))

    df_dict.to_csv("ir_dict.csv", index = False, sep = ";", encoding = "latin-1")

overall_score = df_dict.iloc[df_dict[["eng", "meaning"]].drop_duplicates().index]["score"].mean()

print("overall score: {:.4f} %".format(overall_score * 10, 4))
input("Press 'Enter' to close")
