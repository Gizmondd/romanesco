
from nltk import sent_tokenize, word_tokenize
import os
import codecs

directory = "./train/pos/"
output = "./dataset.txt"
sentences = []
word_tokenized = []

for filename in os.listdir(directory):
    with codecs.open(directory + filename, encoding="utf-8") as open_file:
        for line in open_file:
            line = line.replace("<br /><br />", "")
            sentences += sent_tokenize(line)

for sentence in sentences:
    word_tokenized.append(word_tokenize(sentence))

with codecs.open(output, "w", encoding="utf-8") as output:
    for sentence in word_tokenized:
        output.write(" ".join(sentence) + "\n")
