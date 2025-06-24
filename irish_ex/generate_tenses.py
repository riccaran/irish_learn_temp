from bs4 import BeautifulSoup
from pprint import pprint
import requests
import time
import json
import os
from tqdm import tqdm
import pandas as pd

####

def extract_tense_1(terms_list):
    tense_data = {
        '1 Singular': {},
        '2 Singular': {},
        '3 Singular': {'Male': {}, 'Female': {}},
        '1 Plural': {'Compressed': {}, 'Extended': {}},
        '2 Plural': {},
        '3 Plural': {},
        'Passive': {}
    }

    # First person singular
    terms_1s = terms_list[0]

    tense_data["1 Singular"] = {
        'Affirmative' : terms_1s[1],
        'Question' : terms_1s[2],
        'Negative' : terms_1s[3]
    }

    # Second person singular
    terms_2s = terms_list[1]

    tense_data["2 Singular"] = {
        'Affirmative' : terms_2s[1],
        'Question' : terms_2s[2],
        'Negative' : terms_2s[3]
    }

    # Third person singular
    terms_3 = terms_list[2] + terms_list[3]

    terms_m = {
        'Affirmative' : terms_3[1],
        'Question' : terms_3[4],
        'Negative' : terms_3[5]
    }

    terms_f = {
        'Affirmative' : terms_3[6],
        'Question' : terms_3[9],
        'Negative' : terms_3[10]
    }

    tense_data["3 Singular"]["Male"] = terms_m
    tense_data["3 Singular"]["Female"] = terms_f

    # First person plural

    terms_1p = terms_list[4] + terms_list[5]

    terms_f1 = {
        'Affirmative' : terms_1p[1],
        'Question' : terms_1p[2],
        'Negative' : terms_1p[3]
    }

    terms_f2 = {
        'Affirmative' : terms_1p[4],
        'Question' : terms_1p[5],
        'Negative' : terms_1p[6]
    }

    tense_data["1 Plural"]["Compressed"] = terms_f1
    tense_data["1 Plural"]["Extended"] = terms_f2

    # Second person plural

    terms_2p = terms_list[6]

    tense_data["2 Plural"] = {
        'Affirmative' : terms_2p[1],
        'Question' : terms_2p[2],
        'Negative' : terms_2p[3]
    }

    # Third person plural

    terms_3p = terms_list[7]

    tense_data["3 Plural"] = {
        'Affirmative' : terms_3p[1],
        'Question' : terms_3p[2],
        'Negative' : terms_3p[3]
    }

    # Passive

    terms_pass = terms_list[8]

    tense_data["Passive"] = {
        'Affirmative' : terms_pass[0],
        'Question' : terms_pass[1],
        'Negative' : terms_pass[2]
    }

    return tense_data


def extract_tense_2(terms_list):
    tense_data = {
        '1 Singular': {},
        '2 Singular': {},
        '3 Singular': {'Male': {}, 'Female': {}},
        '1 Plural': {'Compressed': {}, 'Extended': {}},
        '2 Plural': {},
        '3 Plural': {},
        'Passive': {}
    }

    # First person singular
    terms_1s = terms_list[0]

    tense_data["1 Singular"] = {
        'Affirmative' : terms_1s[1],
        'Question' : terms_1s[2],
        'Negative' : terms_1s[3]
    }

    # Second person singular
    terms_2s = terms_list[1]

    tense_data["2 Singular"] = {
        'Affirmative' : terms_2s[1],
        'Question' : terms_2s[2],
        'Negative' : terms_2s[3]
    }

    # Third person singular
    terms_3 = terms_list[2] + terms_list[3]

    terms_m = {
        'Affirmative' : terms_3[1],
        'Question' : terms_3[4],
        'Negative' : terms_3[5]
    }

    terms_f = {
        'Affirmative' : terms_3[6],
        'Question' : terms_3[9],
        'Negative' : terms_3[10]
    }

    tense_data["3 Singular"]["Male"] = terms_m
    tense_data["3 Singular"]["Female"] = terms_f

    # First person plural

    terms_1p = terms_list[4] + terms_list[5]

    terms_f1 = {
        'Affirmative' : terms_1p[1],
        'Question' : terms_1p[2],
        'Negative' : terms_1p[3]
    }

    terms_f2 = {
        'Affirmative' : terms_1p[4],
        'Question' : terms_1p[5],
        'Negative' : terms_1p[6]
    }

    tense_data["1 Plural"]["Compressed"] = terms_f1
    tense_data["1 Plural"]["Extended"] = terms_f2

    # Second person plural

    terms_2p = terms_list[6]

    tense_data["2 Plural"] = {
        'Affirmative' : terms_2p[1],
        'Question' : terms_2p[2],
        'Negative' : terms_2p[3]
    }

    # Third person plural

    terms_3p = terms_list[7] + terms_list[8]

    terms_f1 = {
        'Affirmative' : terms_3p[1],
        'Question' : terms_3p[2],
        'Negative' : terms_3p[3]
    }

    terms_f2 = {
        'Affirmative' : terms_3p[4],
        'Question' : terms_3p[5],
        'Negative' : terms_3p[6]
    }

    tense_data["3 Plural"]["Compressed"] = terms_f1
    tense_data["3 Plural"]["Extended"] = terms_f2

    # Passive

    terms_pass = terms_list[9]

    tense_data["Passive"] = {
        'Affirmative' : terms_pass[0],
        'Question' : terms_pass[1],
        'Negative' : terms_pass[2]
    }

    return tense_data


def extract_tense_3(terms_list):
    tense_data = {
        '1 Singular': {},
        '2 Singular': {},
        '3 Singular': {'Male': {}, 'Female': {}},
        '1 Plural': {'Compressed': {}, 'Extended': {}},
        '2 Plural': {},
        '3 Plural': {},
        'Passive': {}
    }

    # First person singular
    terms_1s = terms_list[0]

    tense_data["1 Singular"] = {
        'Affirmative' : terms_1s[1],
        'Negative' : terms_1s[2]
    }

    # Second person singular
    terms_2s = terms_list[1]

    tense_data["2 Singular"] = {
        'Affirmative' : terms_2s[1],
        'Negative' : terms_2s[2]
    }

    # Third person singular
    terms_3 = terms_list[2] + terms_list[3]

    terms_m = {
        'Affirmative' : terms_3[1],
        'Negative' : terms_3[4]
    }

    terms_f = {
        'Affirmative' : terms_3[5],
        'Negative' : terms_3[8]
    }

    tense_data["3 Singular"]["Male"] = terms_m
    tense_data["3 Singular"]["Female"] = terms_f

    # First person plural

    terms_1p = terms_list[4] + terms_list[5]

    terms_f1 = {
        'Affirmative' : terms_1p[1],
        'Negative' : terms_1p[2]
    }

    terms_f2 = {
        'Affirmative' : terms_1p[3],
        'Negative' : terms_1p[4]
    }

    tense_data["1 Plural"]["Compressed"] = terms_f1
    tense_data["1 Plural"]["Extended"] = terms_f2

    # Second person plural

    terms_2p = terms_list[6]

    tense_data["2 Plural"] = {
        'Affirmative' : terms_2p[1],
        'Negative' : terms_2p[2]
    }

    # Third person plural

    terms_3p = terms_list[7] + terms_list[8]

    terms_f1 = {
        'Affirmative' : terms_3p[1],
        'Negative' : terms_3p[2]
    }

    terms_f2 = {
        'Affirmative' : terms_3p[3],
        'Negative' : terms_3p[4]
    }

    tense_data["3 Plural"]["Compressed"] = terms_f1
    tense_data["3 Plural"]["Extended"] = terms_f2

    # Passive

    terms_pass = terms_list[9]

    tense_data["Passive"] = {
        'Affirmative' : terms_pass[0],
        'Negative' : terms_pass[1]
    }

    return tense_data

def extract_tense_4(terms_list):
    tense_data = {
        '1 Singular': {},
        '2 Singular': {},
        '3 Singular': {'Male': {}, 'Female': {}},
        '1 Plural': {'Compressed': {}, 'Extended': {}},
        '2 Plural': {},
        '3 Plural': {},
        'Passive': {}
    }

    # First person singular
    terms_1s = terms_list[0]

    tense_data["1 Singular"] = {
        'Affirmative' : terms_1s[1],
        'Negative' : terms_1s[2]
    }

    # Second person singular
    terms_2s = terms_list[1]

    tense_data["2 Singular"] = {
        'Affirmative' : terms_2s[1],
        'Negative' : terms_2s[2]
    }

    # Third person singular
    terms_3 = terms_list[2] + terms_list[3]

    terms_m = {
        'Affirmative' : terms_3[1],
        'Negative' : terms_3[4]
    }

    terms_f = {
        'Affirmative' : terms_3[5],
        'Negative' : terms_3[8]
    }

    tense_data["3 Singular"]["Male"] = terms_m
    tense_data["3 Singular"]["Female"] = terms_f

    # First person plural

    terms_1p = terms_list[4] + terms_list[5]

    terms_f1 = {
        'Affirmative' : terms_1p[1],
        'Negative' : terms_1p[2]
    }

    terms_f2 = {
        'Affirmative' : terms_1p[3],
        'Negative' : terms_1p[4]
    }

    tense_data["1 Plural"]["Compressed"] = terms_f1
    tense_data["1 Plural"]["Extended"] = terms_f2

    # Second person plural

    terms_2p = terms_list[6]

    tense_data["2 Plural"] = {
        'Affirmative' : terms_2p[1],
        'Negative' : terms_2p[2]
    }

    # Third person plural

    terms_3p = terms_list[7]

    tense_data["3 Plural"] = {
        'Affirmative' : terms_3p[1],
        'Negative' : terms_3p[2]
    }

    # Passive

    terms_pass = terms_list[8]

    tense_data["Passive"] = {
        'Affirmative' : terms_pass[0],
        'Negative' : terms_pass[1]
    }

    return tense_data

def base_forms(soup):
    extracted_data = list()

    # Look for all h3 elements that might contain "VERBAL NOUN" or "VERBAL ADJECTIVE"
    headers = soup.find_all("h3")
    for header in headers:
        if "VERBAL NOUN" in header.text or "VERBAL ADJECTIVE" in header.text:
            # Get the section
            value = header.find_next_sibling("div")
            if value:
                extracted_data.append((header.text.strip(), value.text.strip()))

    return {elem[0].lower() : elem[1] for elem in extracted_data}

def process_letters(word):
    return "".join([accents.get(letter, letter) for letter in word])

def generate_tenses(verb):
    # Load the HTML content from the uploaded file
    with open("webpages/{}.html".format(verb), "r", encoding="utf-8") as file:
        html_content = file.read()

    tenses_comp = dict()

    tenses = ["present", "future", "past", "condi", "imper", "pastConti", "subj"]
    soup = BeautifulSoup(html_content, 'html.parser')

    for tense in tenses:
        section = soup.find('div', id=tense)
        blocks = section.find_all('div', class_='block')

        terms_list = list()

        for block in blocks:
            terms = [term for term in block.strings if term!= "▪"]
            terms_list.append(terms)

        if tense == "subj":
            tenses_comp[tense] = extract_tense_4(terms_list) # For subjunctive
        elif tense == "imper":
            tenses_comp[tense] = extract_tense_3(terms_list) # For imperative
        elif tense in ["past", "condi", "pastConti"]:
            tenses_comp[tense] = extract_tense_2(terms_list) # For past, past habitual and conditional
        else:
            tenses_comp[tense] = extract_tense_1(terms_list) # For present and future

    verbals = base_forms(soup)
    tenses_comp.update(verbals)

    return tenses_comp

####

if not os.path.exists("webpages"):
    os.makedirs("webpages")

if not os.path.exists("conjugations"):
    os.makedirs("conjugations")

base_url = 'https://www.focloir.ie/en/grammar/ei/{}_verb'

accents = {
    "á": "a_x",
    "é": "e_x",
    "í": "i_x",
    "ó": "o_x",
    "ú": "u_x"
}

webpages = os.listdir("webpages")

####

verbs = pd.read_csv("verbs.csv", encoding = "utf-8").values

for verb in tqdm(verbs):
    verb_proc = process_letters(verb[0])
    if "{}.html".format(verb_proc) not in webpages:
        url = base_url.format(verb_proc)
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            with open('webpages/{}.html'.format(verb_proc), 'w', encoding=response.encoding) as file:
                file.write(response.text)
        except requests.exceptions.RequestException as e:
            print('Error', e)
        time.sleep(5)

for verb in tqdm(verbs):
    verb_proc = process_letters(verb[0])
    if "{}.html".format(verb_proc) in webpages:
        try:
            tenses_comp = generate_tenses(verb_proc)
            with open("conjugations/{}.json".format(verb_proc), "w") as f:
                json.dump(tenses_comp, f)
        except:
            pass

# with open("ith.json", "r") as f:
#     ith = json.load(f)

# ith
