import os
import xml.etree.ElementTree as ET
import pandas as pd
from matplotlib import pyplot as plt
from operator import itemgetter
import math
from string import punctuation


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

token_count = {}
document_no = 0

print("Number of documents: ", len(book))

for document in book:
    document_path = cwd + "//" + document

    if os.path.isfile(document_path):

        try:
            tree = ET.parse(document_path)
            root = tree.getroot()
            text = ""

            for child in root:
                if child.tag == "TEXT":
                    text += child.text

            tokens = tokenize(text)
            tokens = stopwords_removal(tokens)
            tokens = stemming(tokens)

            for token in tokens:
                if token not in token_count:
                    token_count[token] = 1
                else:
                    token_count[token] += 1

            print(document_no)
            document_no += 1

        except Exception as e:
            print(e)

tokens_list = []

for token in token_count:
    tokens_list.append([token, token_count[token]])

dataframe = []

for token_row in tokens_list:
    dataframe.append([token_row[0], token_row[1]])

dataframe = sorted(dataframe, key=itemgetter(1), reverse=True)
print(dataframe[:100])

graph_x_rank = []
graph_y_frequency = []

for i in range(10):
    graph_x_rank.append(i+1)
    graph_y_frequency.append(math.log(dataframe[i][1]))

plt.rcParams["font.family"] = "Devanagari"

plt.plot(graph_x_rank, graph_y_frequency, marker='o', markerfacecolor='red')
plt.title("Luhn's Law")


for i in range(10):
    plt.annotate(dataframe[i][0], (graph_x_rank[i], graph_y_frequency[i]))

plt.grid(True)
plt.xlabel("Rank")
plt.ylabel("log(frequency)")
plt.show()

df = pd.DataFrame(dataframe, columns=["Word", "Frequency"])
df.to_excel("luhn_hindi.xlsx")