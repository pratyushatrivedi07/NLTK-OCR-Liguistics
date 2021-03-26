"""Data collection from web through Web-scraping
 Data Cleanup (Like special characters, numeric values, stopwords, punctuations etc)
Tokenization - Creation of tokens (Word Tokens & Sentence tokens)
Calculate Word Frequency for each word by excluding stop words
Calculate Weighted Frequency for each word
Calculate Sentence scores based on each word within sentence
Creation of summary with top 10 highest scored sentences"""

#To scrap the data from the data given like the url or the file.
from urllib import request
from bs4 import BeautifulSoup as bs
import re
import nltk
import heapq


what=int(input("what you want to summarize?\n 1.WebPage \n 2.Text File\n "))

if(what==2):
    filename=input("enter the filename you want to summarize\n")
    f=open(filename,encoding='utf-8',mode="r+")
    paragraphContents = f.read()
    f.close()
    allParagraphContent = ""
    for paragraphContent in paragraphContents:
        allParagraphContent += paragraphContent

else:
    url=input("enter the webpage url you want to summarize\n")
    #url = "https://en.wikipedia.org/wiki/Machine_learning"
    allParagraphContent = ""
    htmlDoc = request.urlopen(url)
    soupObject = bs(htmlDoc, 'html.parser')
    paragraphContents = soupObject.findAll('p')
    for paragraphContent in paragraphContents:
        allParagraphContent += paragraphContent.text

#print(paragraphContents)
#print(allParagraphContent)

"""here re.sub stands for remove substring, then [[0-9]] stands for removing all square brackets and numbers within it
' '--> this stands for removing all spaces and s+ stands for removing the whitespaces
"""
allParagraphContent_cleanerData = re.sub(r'\[[0-9]*\]',' ',allParagraphContent)
allParagraphContent_cleanedData = re.sub(r'\s+',' ',allParagraphContent_cleanerData)

sentences_tokens = nltk.sent_tokenize(allParagraphContent_cleanedData)
#print(allParagraphContent_cleanedData)

allParagraphContent_cleanedData = re.sub(r'[^a-zA-z]', ' ', allParagraphContent_cleanedData)
allParagraphContent_cleanedData = re.sub(r'\s+',' ',allParagraphContent_cleanedData)

#creating sentence Tokens


words_tokens     = nltk.word_tokenize(allParagraphContent_cleanedData)

#calculate the Frequency and remove stopwords

stopwords = nltk.corpus.stopwords.words('english')

word_frequencies = {}

for word in words_tokens:
    if word not in stopwords:
        if word not in word_frequencies.keys():
            word_frequencies[word]=1
        else:
            word_frequencies[word]+=1

#print(word_frequencies)

#calculate weighted Frequency
maximum_frequency_word = max(word_frequencies.values())

for word in word_frequencies.keys():
    word_frequencies[word] =  (word_frequencies[word]/maximum_frequency_word)

#print(word_frequencies)

#calculate sentence score with each word weighted Frequency

sentences_scores = {}

for sentence in sentences_tokens:
    for word in nltk.word_tokenize(sentence.lower()):
        if word in word_frequencies.keys():
            if(len(sentence.split( ))) < 30:
                if sentence not in sentences_scores.keys():
                    sentences_scores[sentence] = word_frequencies[word]
                else:
                    sentences_scores[sentence] += word_frequencies[word]

#print(sentences_scores)

n = int(input("How many line summary do you want?"))

summary_MachineLearning = heapq.nlargest(n, sentences_scores, key= sentences_scores.get)
print(summary_MachineLearning)
