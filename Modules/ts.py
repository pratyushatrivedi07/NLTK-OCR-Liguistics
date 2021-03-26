from translate import Translator
import sys



print("1. English to French\n2. English to Hindi\n3. English to Spanish\n4. English to German")
choice= int(input("Enter Choice: "))
text =str(input("Enter text: ")) 


if (choice==1): 
    translator= Translator(to_lang="French")
    translation = translator.translate(text)
    print (translation)

elif (choice==2):
    translator= Translator(to_lang="hindi")
    translation = translator.translate(text)
    print (translation)

elif (choice==3):
    translator= Translator(to_lang="spanish")
    translation = translator.translate(text)
    print (translation)

elif (choice==4):
    translator= Translator(to_lang="german")
    translation = translator.translate(text)
    print (translation)

