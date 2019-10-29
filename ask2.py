from google.cloud import language
import io
import os
import mysql.connector
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
def language_analysis(text):
    
    from google.cloud.language import enums
    from google.cloud.language import types

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
# example = raw_input("Search: ")

# Instantiates a client
client = speech.SpeechClient()

# The name of the audio file to transcribe
file_name = os.path.join(
    os.path.dirname(__file__),
    'samples',
    'testNum.flac')

# Loads the audio into memory
with io.open(file_name, 'rb') as audio_file:
    content = audio_file.read()
    audio = types.RecognitionAudio(content=content)

config = types.RecognitionConfig(
    encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
    sample_rate_hertz=48000,
    language_code='en-US')

# Detects speech in the audio file
response = client.recognize(config, audio)
voiceText = ''
for result in response.results:
    voiceText += result.alternatives[0].transcript

str(voiceText)
sentiment, entities = language_analysis(voiceText)
#print('Text: {}'.format(example))
#print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))
entity_type = ('UNKNOWN', 'PERSON', 'LOCATION', 'ORGANIZATION', 'EVENT', 'WORK_OF_ART', 'CONSUMER_GOOD', 'OTHER',)


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

for p in myresult:
  print("{} - {} PRICE: ${}".format(p[0], p[1], p[2]))
