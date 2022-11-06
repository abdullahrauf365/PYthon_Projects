import nltk
from nltk.stem.porter import PorterStemmer
porter_stemmer = PorterStemmer()
text = """The youth of Pakistan must equip themselves with the skill set that will end enable them to benefit from the 
massive available opportunities in all sectors. 
President Dr. Arif Alvi addressed the Career Guide Expo 2022 in Islamabad"""

tokenization = nltk.word_tokenize(text)

print("				*******   STEMMING   *******				")
print("\nWord    :   Root Word \n")
for w in tokenization:
	print("{}  :  {}".format(w, porter_stemmer.stem(w)))

