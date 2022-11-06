import nltk
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()

text = """The youth of Pakistan must equip themselves with the skill set that will end enable them to benefit from the 
massive available opportunities in all sectors. 
President Dr. Arif Alvi addressed the Career Guide Expo 2022 in Islamabad"""

tokenization = nltk.word_tokenize(text)

print("				*******   LEMMATIZATION  *******				")

for w in tokenization:
	print("{}  :  {}".format(w, wordnet_lemmatizer.lemmatize(w)))

