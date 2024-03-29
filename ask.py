from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import mysql.connector

def language_analysis(text):
            client = language.LanguageServiceClient()   ###  Hashed code is Old code as per video 
                    #document = client.document_from_text(text)
            document = types.Document(content=text, type=enums.Document.Type.PLAIN_TEXT)
                                    #sent_analysis = client.analyze_sentiment()
            sent_analysis = client.analyze_sentiment(document=document).document_sentiment
                                                            #sentiment = sent_analysis.sentiment
                                                                    #ent_analysis = document.analyze_entities()
            entities = client.analyze_entities(document).entities
                                                                                    #entities = ent_analysis.entities
            return sent_analysis, entities
                                                                                        #example = u'is it not obvious that python is the best programming language'
                                                                                        ### content taken from Python wiki pagei
# example = "I want perfume"
example = raw_input("Search: ")

sentiment, entities = language_analysis(example)

entity_type = ('UNKNOWN', 'PERSON', 'LOCATION', 'ORGANIZATION', 'EVENT', 'WORK_OF_ART', 'CONSUMER_GOOD', 'OTHER')

e = entities[0].name

# -------

mydb = mysql.connector.connect(
       host='##.##.###.###',
       database='####',
       user='####',
       password='##')

mycursor = mydb.cursor()

query = "SELECT BRAND_NAME, DISPLAY_NAME, LIST_PRICE FROM Catalog WHERE CATEGORY_NAME = '{}' ORDER BY LIST_PRICE DESC LIMIT 5, 15".format(e)

mycursor.execute(query)

myresult = mycursor.fetchall()

for x in myresult:
  p = x
  print("{} - {} PRICE: ${}".format(p[0], p[1], p[2]))
