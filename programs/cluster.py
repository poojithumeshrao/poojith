import nltk
import string
import scipy
import random
import numpy
import pdb

from collections import Counter
from nltk.corpus import stopwords
from nltk.stem.porter import *
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy import spatial

op = 9

strg = []

strg.append("poojith studies in nie")
strg.append("praveen studies in jce")
strg.append("jhon studies in jce")
strg.append("poojith likes ece")
strg.append("praveen likes cs")
strg.append("jhon likes both")
strg.append("poojith drives motorcycle")
strg.append("praveen drives moped")
strg.append("jhon drives car")  

'''with open('bbcsport/cricket/c1.txt') as txt:
    strg.append(txt.read().replace('\n',' '))
with open('bbcsport/cricket/c2.txt') as txt:
    strg.append(txt.read().replace('\n',' '))
with open('bbcsport/cricket/c3.txt') as txt:
    strg.append(txt.read().replace('\n',' '))
with open('bbcsport/tennis/t1.txt') as txt:
    strg.append(txt.read().replace('\n',' '))
with open('bbcsport/tennis/t2.txt') as txt:
    strg.append(txt.read().replace('\n',' '))
with open('bbcsport/tennis/t3.txt') as txt:
    strg.append(txt.read().replace('\n',' '))
with open('bbcsport/football/f1.txt') as txt:
    strg.append(txt.read().replace('\n',' '))
with open('bbcsport/football/f2.txt') as txt:
    strg.append(txt.read().replace('\n',' '))
with open('bbcsport/football/f1.txt') as txt:
    strg.append(txt.read().replace('\n',' '))'''

tokens = {}
count = []
clean = []
stemmer = PorterStemmer()

def stem_tokens(tk,stemmer):
    stemmed = []
    for item in tk:
        stemmed.append(stemmer.stem(item))
    return stemmed

def tokenize(text):
    tk = nltk.word_tokenize(text)
    stems = stem_tokens(tk,stemmer)
    return stems


for i in range(op):
    low = strg[i].lower()
   
    no_pun = low.translate(None,string.punctuation)
    tokens[i] = no_pun
    
tfidf = TfidfVectorizer(tokenizer = tokenize, stop_words = 'english')
tfs = tfidf.fit_transform(tokens.values()).toarray()

tt = []

for i in range(len(tfs)):
    tt.append(tfs[i].tolist())


class clts:
    def __init__(self):
        self.docs = []
        self.centroid = []
        self.status = 0;
    def cent(self):
        
        if(len(self.docs)) != 0:
            self.summ = [0 for i in range(len(self.docs[0]))]
            for i in range(len(self.docs)):
               self.summ  = [x + y for x , y in zip(self.summ,self.docs[i])]
            self.status = 0
            self.temp = self.centroid
            self.centroid = [x/len(self.docs) for x in self.summ]
            if self.centroid == self.temp:
                self.status  = 1;
        else :
            self.status = 0;
        
class files:
    def __init__(self,d):
        self.fl = d
        self.nw = -1
        self.old = self.nw

# number of clusters
n=3

check = 0

cluster = [clts() for i in range(n)]


#for i in range(3):
   # cluster[i].centroid = tt[random.randint(0,op-1)]


cluster[0].centroid = tt[0]
cluster[1].centroid = tt[1]
cluster[2].centroid = tt[2]

doc = [files(tt[i]) for i in range(op)]

check = 0

def ch():
    global check
    for i in range(n):
        if cluster[i].status == 0:
            check = 0
            return 1
    check += 1
    if check == 2:
        return 0
count = 0 

#pdb.set_trace()
while ch():
    for i in range(n):
        del cluster[i].docs[:] 
    for it in range(op):
        m = 0
        f = 0
        for i in range(n):
            a = numpy.array(tt[it])
            b = numpy.array(cluster[i].centroid)
            if len(b)!= 0:
                d = 1 - spatial.distance.cosine(a,b)
           # (tfs[it],cluster[i].centroid)
            if m<d :
                f = i
            m = max(d,m)
        
        doc[it].old = doc[it].nw
        doc[it].nw = f
        cluster[f].docs.append(tt[it])
    for i in range(n):
        cluster[i].cent();
    count +=1
  #  check +=1

for i in range(n):
    for j in range(len(cluster[i].docs)):
        for k in range(len(tt)):
            if cluster[i].docs[j]== tt[k]:
                print strg[k]
    print '------------------'
