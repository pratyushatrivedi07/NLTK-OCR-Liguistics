from spellchecker import SpellChecker
import nltk
import sys
import language_check
from importlib import reload

reload(sys)

spell = SpellChecker()

# find those words that may be misspelled
sentence=input("Enter a sentence  :  ")
a=sentence.split()
# print(a)

misspelled = spell.unknown(a)

for word in misspelled:
    # Get the one `most likely` answer
    print(spell.correction(word))

    # Get a list of `likely` options
    print(spell.candidates(word))
    
tool = language_check.LanguageTool('en-US')
# text = u'I fli dubai'
matches = tool.check(sentence)
len(matches)
print(matches)

ac = language_check.correct(sentence,matches)
print(ac)

# tokens = nltk.word_tokenize(sentence)
# print(tokens)
# tagged=nltk.pos_tag(tokens)
# print(tagged)
# entities = nltk.chunk.ne_chunk(tagged)
# print(entities)