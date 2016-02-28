from stop_words import get_stop_words
import numpy as np
import lda
import textmining
import json
import os
import psycopg2
import unicodedata
from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer

def generate_subtopics(business):
	tdm = textmining.TermDocumentMatrix()
	tokenizer = RegexpTokenizer(r'\w+')  
	en_stop = get_stop_words('en') 
	p_stemmer = PorterStemmer()

	data_dir = os.path.dirname(os.path.abspath(__file__))

	reviews = business["review_texts"]

	# Add the documents
	for n, review in enumerate(reviews):
		raw = review.lower()
		tokens = tokenizer.tokenize(raw)
		stopped_tokens = [i for i in tokens if not i in en_stop]
		stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]
		#print(stemmed_tokens)
		tdm.add_doc(" ".join(stemmed_tokens))

	# create a temp variable with doc-term info
	temp = list(tdm.rows(cutoff=1))
	# get the vocab from first row
	vocab = tuple(temp[0])

	# get document-term matrix from remaining rows
	X = np.array(temp[1:])

	model = lda.LDA(n_topics=3, n_iter=100, random_state=1)
	model.fit(X)
	topic_word = model.topic_word_  # model.components_ also works
	words_per_topic = 10
	topics_list = []
	for i, topic_dist in enumerate(topic_word):
		topic_words = np.array(vocab)[np.argsort(topic_dist)][:-words_per_topic:-1]
		#print('Topic {}: {}'.format(i, ' '.join(topic_words)))
		topics_list.append(' '.join(topic_words))
	return topics_list