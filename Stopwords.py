from gensim.parsing.preprocessing import remove_stopwords

text = """The youth of Pakistan must equip themselves with the skill set that will end enable them to benefit from the 
massive available opportunities in all sectors. 
President Dr. Arif Alvi addressed the Career Guide Expo 2022 in Islamabad"""
filtered_sentence = remove_stopwords(text)

print("\n")
print(filtered_sentence)
print("\n")
