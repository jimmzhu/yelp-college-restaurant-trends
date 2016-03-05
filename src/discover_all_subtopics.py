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
from scipy import sparse

tdm = textmining.TermDocumentMatrix()
tokenizer = RegexpTokenizer(r'\w+')  
en_stop = get_stop_words('en') 
p_stemmer = PorterStemmer()

data_dir = os.path.dirname(os.path.abspath(__file__))

json_file = open(data_dir + "\\businesses\\businesses-train.json")

counter = 0;
for json_line in json_file:	
	counter = counter + 1
	print('{}:{}'.format("Stage 1",counter))
	business_reviews = {}
	json_data = json.loads(json_line)
	reviews = json_data["review_texts"]
	# Add the documents
	for n, review in enumerate(reviews):
		raw = review.lower()
		tokens = tokenizer.tokenize(raw)
		stopped_tokens = [i for i in tokens if not i in en_stop]
		stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]
		tdm.add_doc(" ".join(stemmed_tokens))

ndocs = len(tdm.sparse)
nwords = len(tdm.doc_count)
words = tdm.doc_count.keys()		
print(len(words))
		
# initialize output sparse matrix
X = sparse.lil_matrix((ndocs, nwords),dtype=int)

counter = 0;
# iterate over documents, fill in rows of X
for ii, doc in enumerate(tdm.sparse):
#	counter = counter + 1
#	print('{}:{}'.format("Stage 2",counter))
	for word, count in doc.iteritems():
		jj = words.index(word)
		X[ii, jj] = count
X = X.tocsr()

print('Format is (Document Count, Vocab Count): {}'.format(X.shape))
model = lda.LDA(n_topics=15, n_iter=200, random_state=1)
model.fit(X)
topic_word = model.topic_word_  # model.components_ also works
n_top_words = 20
for i, topic_dist in enumerate(topic_word):
	topic_words = np.array(words)[np.argsort(topic_dist)][:-n_top_words:-1]
	print('Topic {}: {}'.format(i, ' '.join(topic_words)))