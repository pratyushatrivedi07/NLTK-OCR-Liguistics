from django.shortcuts import render
import requests
import sys
import subprocess
from subprocess import run, PIPE
from spellchecker import SpellChecker
import nltk
import sys
import language_check
from importlib import reload
from translate import Translator
import codecs
from urllib import request
from bs4 import BeautifulSoup as bs
import re
import nltk
import heapq
import imp
from numpy import unicode
import urllib.request
from django.core.files.storage import FileSystemStorage
from django.core.files.storage import default_storage
from django.core.files import File
import os
import pytesseract
from PIL import Image
import argparse
import cv2


reload(sys)
 
def button1(request):
    return render(request,'hom.html')

def output(request):
    data=requests.get("hom.html")
    print(data.text)
    data=data.text
    return render(request,'hom.html',{'data':data})

#------------------------GRAMMAR CHECK------------------------------

def spellc(request):
    # return render(request,'home2.html')
    # def bu()
    # :
    imp = request.POST.get('param')
    print(imp)
    if imp == None:
        ac = ""
        b = ""
        c = ""
    else:
        a=imp.split()
        
        spell = SpellChecker()
        print(imp)
        # find those words that may be misspelled

        # print(a)

        misspelled = spell.unknown(a)
        
        for word in misspelled:
            # Get the one `most likely` answer
            b = spell.correction(word)

            # Get a list of `likely` options
            c = spell.candidates(word)
            
        tool = language_check.LanguageTool('en-US')
        # text = u'I fli dubai'
        matches = tool.check(imp)
        len(matches)
        print(matches)

        ac = language_check.correct(imp,matches)
        print(ac)
        imp=None
        
    return render(request,'grammar.html',{'data1': ac,'data2':b,'data3':c})


#-----------------------------------TRANSLATION-------------------------------------

def transf(request):
    imp2 = request.POST.get('param2')
    translf=""
    if imp2 == None:
        pass
    else:
        translator= Translator(to_lang="French")
        translf = translator.translate(imp2)
        print (translf)
    return render(request,'card.html',{'textf':translf})

def transh(request):
    imp2 = request.POST.get('param2')
    transl=""
    if imp2 == None:
        pass
    else:
        translator= Translator(to_lang="Hindi")
        translh = translator.translate(imp2)
        print (transl)
    return render(request,'card.html',{'texth':translh})
        
def transs(request):
    imp2 = request.POST.get('param2')
    transl=""
    if imp2 == None:
        pass
    else:
        translator= Translator(to_lang="Spanish")
        transls = translator.translate(imp2)
        print (transl)
    return render(request,'card.html',{'texts':transls})
        
def transg(request):
    imp2 = request.POST.get('param2')
    transl=""
    if imp2 == None:
        pass
    else:
        translator= Translator(to_lang="German")
        translg = translator.translate(imp2)
        print (transl)
    return render(request,'card.html',{'textg':translg})

#----------------------------------------SUMMARIZATION--URL-------------------------------------------

def summ(request):
    url1=request.POST.get('param3')
    summary_MachineLearning = ""
    summML = ""
    allParagraphContent = ""
    if url1==None:
        pass
    else:
        htmlDoc =urllib.request.urlopen(url1)
        print(htmlDoc)
        soupObject = bs(htmlDoc, 'html.parser')
        paragraphContents = soupObject.findAll('p')
        for paragraphContent in paragraphContents:
            allParagraphContent += paragraphContent.text

        """here re.sub stands for remove substring, then [[0-9]] stands for removing all square brackets and numbers within it
        ' '--> this stands for removing all spaces and s+ stands for removing the whitespaces
        """
        allParagraphContent_cleanerData = re.sub(r'\[[0-9]*\]',' ',allParagraphContent)
        allParagraphContent_cleanedData = re.sub(r'\s+',' ',allParagraphContent_cleanerData)

        sentences_tokens = nltk.sent_tokenize(allParagraphContent_cleanedData)

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

        #calculate weighted Frequency
        maximum_frequency_word = max(word_frequencies.values())

        for word in word_frequencies.keys():
            word_frequencies[word] =  (word_frequencies[word]/maximum_frequency_word)

        #calculate sentence score with each word weighted Frequency

        sentences_scores = {}
        for sentence in sentences_tokens:
            for word in nltk.word_tokenize(sentence.lower()):
                if word in word_frequencies.keys():
                    if(len(sentence.split( ))) < 20:
                        if sentence not in sentences_scores.keys():
                            sentences_scores[sentence] = word_frequencies[word]
                        else:
                            sentences_scores[sentence] += word_frequencies[word]

        num=request.POST.get('param4')
       
        n = int(num)
        summary_MachineLearning = heapq.nlargest(n, sentences_scores, key= sentences_scores.get)
        print(summary_MachineLearning)
        summML=summML.join(summary_MachineLearning)
    return render(request,'summ.html',{'textsum': summML}) 

#----------------------------------------SUMMARIZATION--TEXTAREA-------------------------------------------

def textarea(request):
    imp6=request.POST.get("par3")
    paragraphContents=imp6
#    print(paragraphContents)
    allParagraphContent = ""
    summary_MachineLearning = ""
    summML = ""
    if imp6==None:
        pass
    else:
        for paragraphContent in paragraphContents:
            allParagraphContent += paragraphContent
        
        allParagraphContent_cleanerData = re.sub(r'\[[0-9]*\]',' ',allParagraphContent)
        allParagraphContent_cleanedData = re.sub(r'\s+',' ',allParagraphContent_cleanerData)
        sentences_tokens = nltk.sent_tokenize(allParagraphContent_cleanedData)
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

            #calculate weighted Frequency
        maximum_frequency_word = max(word_frequencies.values())

        for word in word_frequencies.keys():
            word_frequencies[word] =  (word_frequencies[word]/maximum_frequency_word)

        #calculate sentence score with each word weighted Frequency
        sentences_scores = {}

        for sentence in sentences_tokens:
            for word in nltk.word_tokenize(sentence.lower()):
                if word in word_frequencies.keys():
                    if(len(sentence.split( ))) < 20:
                        if sentence not in sentences_scores.keys():
                            sentences_scores[sentence] = word_frequencies[word]
                        else:
                            sentences_scores[sentence] += word_frequencies[word]

        num1=request.POST.get("pa6")

        n = int(num1)

        summary_MachineLearning = heapq.nlargest(n, sentences_scores, key= sentences_scores.get)
        print(summary_MachineLearning)   
        summML=summML.join(summary_MachineLearning)
    return render(request, 'summ.html', {'text2': summML})


#------------------------------TEXT EXTRACTION----------------------------------------------------

def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        upl_file=uploaded_file
        print(upl_file.name)
        print(upl_file.size)
        fs = FileSystemStorage()
        name=fs.save(upl_file.name, upl_file)
        context['url'] =fs.url(name)
        print(context)
    return render(request, 'extract.html', context)

def textm(request):
    inp=request.POST.get("pa5")
    outi=""
    abc="Your output is ready!\nClick below to Download the File!"
    if inp==None:
        pass
    else:
        outi=pytesseract.image_to_string(Image.open('//Users//apple//Desktop//djangof 2//button//'+inp))
        print(outi)
        with open("//Users//apple//Desktop//djangof 2//button//media//output.txt", "w") as file:
            file.write(outi)
            file.close()
    return render(request, 'extract.html',{'text3': abc})
    