# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 18:07:12 2019

@author: Mohit
"""

import pandas as pd
import re
from nltk.corpus import stopwords
import emoji

amazon_file = open(r"C:\Users\Mohit\Desktop\Language_1\Round1_Problem1-of-2_Dataset_amazon_cells_labelled.txt")
imdb_file = open(r"C:\Users\Mohit\Desktop\Language_1\Round1_Problem1-of-2_Dataset_imdb_labelled.txt")

amazon_csv = pd.read_csv(r"C:\Users\Mohit\Desktop\Language_1\Round1_Problem1-of-2_Dataset_amazon_cells_labelled.txt", delimiter = "\t", names = ("Text", "Sentiment"))
imdb_csv = pd.read_csv(r"C:\Users\Mohit\Desktop\Language_1\Round1_Problem1-of-2_Dataset_imdb_labelled.txt", delimiter = "\t", names = ("Text", "Sentiment"))

data = amazon_csv.append(imdb_csv, ignore_index = True)

#data = amazon_csv.merge()
print[data]
data_1 = []
corpus_imdb = []
"""
for i in range(0, 1000):
    amazon_1 = re.sub(r'[^ a-zA-z0-9,.;:!]', ' ', amazon_csv['Text'][i])
    data.append(amazon_1)
    """
for i in range(0, 1748):
    a = re.sub(r'[^ a-zA-z0-9,.;:!]', ' ', data['Text'][i])
    data_1.append(a)
data_1 = pd.DataFrame(data_1, columns = ['Text'])
data_1 = data_1.join(data['Sentiment'])
print(data_1)
"""for j in range(0, 748):
    imdb_1 = re.sub(r'[^ a-zA-z0-9,.;:!]', ' ', imdb_csv['Text'][j])
    corpus_imdb.append(imdb_1)"""
    
#number one solved above
    
"""for i in range(0, 1000):
    corpus_amazon[i] = re.sub(r'[]', ' ', corpus_amazon[i])"""
data_2 = []
for i in range(0, 1748):
    #data[i] = re.sub(r'''|www\d{0,3}[.]|[a-z.\-]+[.]com/''', " ", data[i])
    #data_1[i] = re.sub((r'|www[.]|[a-z]+|[.]com|)', " ", data_1[i])
    b = re.sub(r'''(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))''', " ", data_1['Text'][i])
    data_2.append(b)
data_2 = pd.DataFrame(data_2, columns = ['Text'])
data_2 = data_2.join(data['Sentiment'])
# number two solved above
data_3 = []
for i in range(0, 1748):
    c = emoji.demojize(data_2['Text'][i])
    data_3.append(c)
data_3 = pd.DataFrame(data_3, columns = ['Text'])
data_3 = data_3.join(data['Sentiment'])

#number three solved above

for i in range(0, 1000):
    corpus_amazon[i] = re.sub(r'[^ a-zA-z0-9,.!]', ' ', corpus_amazon[i])
    
for j in range(0, 748):
    corpus_imdb[j] = re.sub(r'[^ a-zA-z0-9,.!]', ' ', corpus_imdb[j])

#setting proxy

"""http_proxy = http://IPN:PWD@172.16.2.30:8080
set https_proxy = https://IPN:PWD@172.16.2.30:8080
python get-pip.py"""












#number four solved above

import nltk

for i in range(0, 1000):
    rev_amazon = corpus_amazon[i].split()
    rev_amazon = [word for word in rev_amazon if not word in set(stopwords.words('english'))]
    corpus_amazon[i] = rev_amazon
    corpus_amazon[i] = ' '.join(corpus_amazon[i])

for i in range(0, 748):
    rev_imdb = corpus_imdb[i].split()
    rev_imdb = [word for word in rev_imdb if not word in set(stopwords.words('english'))]
    corpus_imdb[i] = rev_imdb
    corpus_imdb[i] = ' '.join(corpus_imdb[i])
    
# number 5 solved above

import nltk

#nltk.download('all')

for i in range(0, 1000):
    corpus_amazon[i] = corpus_amazon[i].lower()

for j in range(0, 748):
    corpus_imdb[j] = corpus_imdb[j].lower()

from nltk.stem import WordNetLemmatizer
lemma = WordNetLemmatizer()

for i in range(0, 1000):
    rev_amazon = corpus_amazon[i].split()
    corpus_amazon[i] = [lemma.lemmatize(word) for word in rev_amazon]
    corpus_amazon[i] = ' '.join(corpus_amazon[i])    

for j in range(0, 748):
    rev_imdb = corpus_imdb[j].split()
    corpus_imdb[j] = [lemma.lemmatize(word) for word in rev_imdb]
    corpus_imdb[j] = ' '.join(corpus_imdb[j])    

#number 6 solved above

from nltk.tokenize import word_tokenize
for i in range(0, 1000):
    corpus_amazon[i] = word_tokenize(corpus_amazon[i])
    
for j in range(0, 748):
    corpus_imdb[j] = word_tokenize(corpus_imdb[j])

#number 7 solved above
"""import gensim
from nltk.corpus import abc
for i in range(0, 1000):
    model = gensim.models.Word2Vec(corpus_amazon[i], size = 20, window = 10)
model.train(documents, total_examples= 1000, epochs=10)
"""
import nltk
import gensim
from nltk.corpus import abc

model = gensim.models.Word2Vec(corpus_amazon, size = 20)
model.train(corpus_amazon, total_examples = 1000, epochs=10)
wl = "love"
print(model)
words = list(model.wv.vocab)
print(words)
print(model['love'])
X_amazon = model[model.wv.vocab]

model_imdb = gensim.models.Word2Vec(corpus_imdb, size = 20)
model_imdb.train(corpus_imdb, total_examples = 1000, epochs=10)
X_imdb = model_imdb[model_imdb.wv.vocab]