import os
import xml.etree.ElementTree as ET
import nltk
from string import punctuation
from nltk.tokenize import RegexpTokenizer
from nltk.stem import PorterStemmer
from operator import itemgetter
import pandas as pd


def stemming(tokens_list):  # Identifies known suffixes and removes them
    suffixes_list = ['ो', 'े', 'ू', 'ु', 'ी', 'ि', 'ा', 'िए', 'ाई', 'ाए', 'ने', 'नी', 'ना', 'ते', 'ीं', 'ती',
                      'ता', 'ाँ', 'ां', 'ों', 'ें', 'ाकर', 'ाइए', 'ाईं', 'ाया',
                      'ाते', 'ाती', 'ाता', 'तीं', 'ाओं', 'ाएं', 'ुओं', 'ुएं', 'ुआं', 'ाएगी', 'ाएगा', 'ाओगी', 'ाओगे',
                      'ेंगी', 'ेंगे', 'ूंगी', 'ूंगा', 'नाओं', 'नाएं', 'ताओं', 'ताएं', 'ियाँ', 'ियों', 'ियां',
                      'ाएंगी', 'ाएंगे', 'ाऊंगी', 'ाऊंगा', 'ाइयाँ', 'ाइयों', 'ाइयां']

    output_list = []

    for token in tokens_list:
        for suffix in suffixes_list:
            if token.endswith(suffix):
                index = token.rfind(suffix)
                output_list.append(token[:index])
            else:
                output_list.append(token)

    return output_list


def stopwords_removal(tokens_list):
    """Dataset used for stopwords: https://data.mendeley.com/datasets/bsr3frvvjc/1"""

    stopwords = ['मैं', 'मुझको', 'मेरा', 'अपने', 'आप', 'को', 'हमने', 'हमारा', 'अपना', 'हम', 'आप', 'आपका', 'तुम्हारा',
                 'अपने', 'आप', 'स्वयं', 'वह', 'इसे', 'उसके', 'खुद', 'को', 'कि', 'वह', 'उसकी', 'उसका', 'खुद', 'ही', 'यह',
                 'इसके', 'उन्होने', 'अपने', 'क्या', 'जो', 'किसे', 'किसको', 'कि', 'ये', 'हूँ', 'होता', 'है', 'रहे', 'थी',
                 'थे', 'होना', 'गया', 'किया', 'जा', 'रहा', 'है', 'किया', 'है', 'है', 'पडा', 'होने', 'करना', 'करता', 'है',
                 'किया', 'रही', 'एक', 'लेकिन', 'अगर', 'या', 'क्यूंकि', 'जैसा', 'जब', 'तक', 'जबकि', 'की', 'पर', 'द्वारा',
                 'के', 'लिए', 'साथ', 'के', 'बारे', 'में', 'खिलाफ', 'बीच', 'में', 'के', 'माध्यम', 'से', 'दौरान', 'से',
                 'पहले', 'के', 'बाद', 'ऊपर', 'नीचे', 'को', 'से', 'तक', 'से', 'नीचे', 'करने', 'में', 'निकल', 'बंद', 'से',
                 'अधिक', 'तहत', 'दुबारा', 'आगे', 'फिर', 'एक', 'बार', 'यहाँ', 'वहाँ', 'कब', 'कहाँ', 'क्यों', 'कैसे',
                 'सारे', 'किसी', 'दोनो', 'प्रत्येक', 'ज्यादा', 'अधिकांश', 'अन्य', 'में', 'कुछ', 'ऐसा', 'में', 'कोई',
                 'मात्र', 'खुद', 'समान', 'इसलिए', 'बहुत', 'सकता', 'जायेंगे', 'जरा', 'चाहिए', 'अभी', 'और', 'कर', 'दिया',
                 'रखें', 'का', 'हैं', 'इस', 'होता', 'करने', 'ने', 'बनी', 'तो', 'ही', 'हो', 'इसका', 'था', 'हुआ', 'वाले',
                 'बाद', 'लिए', 'सकते', 'इसमें', 'दो', 'वे', 'करते', 'कहा', 'वर्ग', 'कई', 'करें', 'होती', 'अपनी', 'उनके',
                 'यदि', 'हुई', 'जा', 'कहते', 'जब', 'होते', 'कोई', 'हुए', 'व', 'जैसे', 'सभी', 'करता', 'उनकी', 'तरह', 'उस',
                 'आदि', 'इसकी', 'उनका', 'इसी', 'पे', 'तथा', 'भी', 'परंतु', 'इन', 'कम', 'दूर', 'पूरे', 'गये', 'तुम', 'मै',
                 'यहां', 'हुये', 'कभी', 'अथवा', 'गयी', 'प्रति', 'जाता', 'इन्हें', 'गई', 'अब', 'जिसमें', 'लिया', 'बड़ा',
                 'जाती', 'तब', 'उसे', 'जाते', 'लेकर', 'बड़े', 'दूसरे', 'जाने', 'बाहर', 'स्थान', 'उन्हें', 'गए', 'ऐसे',
                 'जिससे', 'समय', 'दोनों', 'किए', 'रहती', 'इनके', 'इनका', 'इनकी', 'सकती', 'आज', 'कल', 'जिन्हें',
                 'जिन्हों', 'तिन्हें', 'तिन्हों', 'किन्हों', 'किन्हें', 'इत्यादि', 'इन्हों', 'उन्हों', 'बिलकुल',
                 'निहायत', 'इन्हीं', 'उन्हीं', 'जितना', 'दूसरा', 'कितना', 'साबुत', 'वग़ैरह', 'कौनसा', 'लिये', 'दिया',
                 'जिसे', 'तिसे', 'काफ़ी', 'पहले', 'बाला', 'मानो', 'अंदर', 'भीतर', 'पूरा', 'सारा', 'उनको', 'वहीं', 'जहाँ',
                 'जीधर', '\ufeffके', 'एवं', 'कुछ', 'कुल', 'रहा', 'जिस', 'जिन', 'तिस', 'तिन', 'कौन', 'किस', 'संग', 'यही',
                 'बही', 'उसी', 'मगर', 'कर', 'मे', 'एस', 'उन', 'सो', 'अत']

    output_list = []

    for token in tokens_list:
        if token not in stopwords:
            output_list.append(token)

    return output_list


def tokenize(text_string):  # Remove punctuations and tokenize
    new_string = ""
    for character in text_string:

        if character not in (punctuation + "।"):
            new_string += character

    new_string = new_string.split()

    return new_string


cwd = os.getcwd() + "//Hindi Dataset"
book = os.listdir(cwd)  # List of folder names

document_id = 0
document_index = {}
data = {}

tokens_all = set()

print("Number of documents: ", len(book))

for document in book:
    document_path = cwd + "//" + document

    if os.path.isfile(document_path):
        try:
            tree = ET.parse(document_path)
            root = tree.getroot()
            text = ""

            for child in root:
                if child.tag == "TEXT":  # Get all data between the <TEXT> tags in the file
                    text += child.text

            tokens = tokenize(text)
            tokens = stopwords_removal(tokens)
            tokens = stemming(tokens)

            tokens_set = set(tokens)
            tokens_all = tokens_all.union(tokens_set)

            document_dict = {}

            for token in tokens:
                if token not in document_dict:
                    document_dict[token] = 1
                else:
                    document_dict[token] += 1

            document_index[document_id] = document  # Map names of documents in a dictionary to numbers

            data[document_id] = document_dict

        except Exception as e:
            print(e)

        document_id += 1
        print("Document ID: ", document_id)


postings_list = {}
token_frequency = {}

for doc_id in data:
    for token in data[doc_id]:
        if token not in token_frequency:
            token_frequency[token] = 1
        else:
            token_frequency[token] += data[doc_id][token]
        if token not in postings_list:
            postings_list[token] = [doc_id]
        else:
            postings_list[token].append(doc_id)

dataframe = []
print("Number of tokens: ", len(tokens_all))
token_no = 1

for token in tokens_all:
    print("Token Number: ", token_no)
    dataframe.append([token, token_frequency[token], postings_list[token]])

dataframe = sorted(dataframe, key=itemgetter(1), reverse=True)

df = pd.DataFrame(dataframe, columns=["Word", "Frequency", "Postings List"])
df.to_excel("hindi_postings.xlsx")