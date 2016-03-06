import json
import os
import psycopg2
import csv

tdm = textmining.TermDocumentMatrix()
tokenizer = RegexpTokenizer(r'\w+')  
en_stop = get_stop_words('en') 
p_stemmer = PorterStemmer()

data_dir = os.path.dirname(os.path.abspath(__file__))


#Get Reviews Per Business Per City
json_file = open(data_dir + "\\businesses\\businesses-train.json")
for json_line in json_file:	
	business_reviews = {}
	json_data = json.loads(json_line)
	topic_list = generate_subtopics(json_data)
	topic_list_combined = '|'.join(topic_list)
	print(topic_list_combined)

#	with open('subtopics.csv','wb') as csvfile:
#		csvwriter = csv.writer(csvfile)
#		
#		for topic in topic_list:
#		
#		csvwriter.writerow('hello',delimiter=',')