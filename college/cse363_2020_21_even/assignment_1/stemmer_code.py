"""Porter-stemmer implementation for Hindi, Sarthak Choudhary, Roll number: 17085066"""

import codecs

suffixes_list = ['ो', 'े', 'ू', 'ु', 'ी', 'ि', 'ा', 'िए', 'ाई', 'ाए', 'ने', 'नी', 'ना', 'ते', 'ीं', 'ती',
                 'ता', 'ाँ', 'ां', 'ों', 'ें', 'ाकर', 'ाइए', 'ाईं', 'ाया',
                 'ाते', 'ाती', 'ाता', 'तीं', 'ाओं', 'ाएं', 'ुओं', 'ुएं', 'ुआं', 'ाएगी', 'ाएगा', 'ाओगी', 'ाओगे',
                 'ेंगी', 'ेंगे', 'ूंगी', 'ूंगा', 'नाओं', 'नाएं', 'ताओं', 'ताएं', 'ियाँ', 'ियों', 'ियां',
                 'ाएंगी', 'ाएंगे', 'ाऊंगी', 'ाऊंगा', 'ाइयाँ', 'ाइयों', 'ाइयां']


# Read the file
f = codecs.open('hindi.txt', encoding='utf-8')
text = f.read()

print("Original Text: ")
print(text)
print()

sentences = text.split("।")  # Hindi sentences end with '|', so split whenever we encounter this character.

sentences_new = []

# Remove initial white space and empty sentences
for i in range(len(sentences)):
    if len(sentences[i]) > 0:
        if i == 0:
            sentences_new.append(sentences[i])
        else:
            sentences_new.append(sentences[i][1:])

# sentence-wise list of words (2D-array where each constituent 1D array contains the words of a sentence)
words_list = []

for sentence in sentences_new:
    words = sentence.split()  # words are separated by space (default separator in python)
    words_list.append(words)


for j in range(len(words_list)):
    for i in range(len(words_list[j])):
        for suffix in suffixes_list:  # Iterate over all suffixes
            if words_list[j][i].endswith(suffix):  # If a words ends with the suffix, remove the suffix from the word.
                index = words_list[j][i].rfind(suffix)
                words_list[j][i] = words_list[j][i][:index]

print("List of words after stemming: ")
print(words_list)
print()


# Write output in file
f = codecs.open('stemming_output.txt', "w", encoding='utf-8')

for words_in_sentence in words_list:
    for word in words_in_sentence:
        f.write(word)
        f.write(" ")

f.close()

# Read output
f = codecs.open('stemming_output.txt', encoding='utf-8')
output_text = f.read()

print("After stemming: ")
print(output_text)

f.close()
