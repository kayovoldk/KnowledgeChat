"""
@author: David Rau

"""
import nltk
import random  # used to generate random responses
import string  # used to remove punctuation


#note this can be easily expanded to be on demand and more interactive
#This however is a proof of concept for demonstration purposes.
#Using the Wikipedia Article History of Berlin as the proof of concept
# https://en.wikipedia.org/wiki/History_of_Berlin


#nltk stuff
nltk.download('punkt') # used to parse the text into sentences
nltk.download('wordnet') # used to parse the sentences into words

