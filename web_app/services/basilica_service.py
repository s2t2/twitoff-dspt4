import basilica
import os
from dotenv import load_dotenv

load_dotenv()

BASILICA_API_KEY = os.getenv("BASILICA_API_KEY")

connection = basilica.Connection(BASILICA_API_KEY)
print(type(connection)) #> <class 'basilica.Connection'>

embedding = connection.embed_sentence("hey this is a cool tweet", model="twitter")
print(embedding)
# > a list of 768 numbers

tweets = ["Hello workd", "artificial intelligence", "another tweet here #cool"]
embeddings = connection.embed_sentences(tweets, model="twitter")
for embed in embeddings:
    print("-----")
    print(len(embed))
