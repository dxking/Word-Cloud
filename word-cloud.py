import pandas as pd
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import sys
script = sys.argv[1]

text = open(script).read()

stopwords = set(STOPWORDS)

with open(script) as f:
    for line in f:
        for word in line.split():
            if word.isupper():
                stopwords.add(word)
text = text.lower()

stopwords.add("int.")
stopwords.add("int")
stopwords.add("ext.")
stopwords.add("ext")
stopwords.add("cont'd")

wordcloud = WordCloud(background_color='black', max_words=150, stopwords=stopwords, margin=10, 
width=1000, height=800).generate(text)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis=('off')
plt.show()
