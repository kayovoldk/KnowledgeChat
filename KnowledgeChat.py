"""
@author: David Rau

"""
import nltk
import random  # used to generate random responses
import string  # used to remove punctuation
import wikipedia # why did finding this take so long?????

#note this can be easily expanded to be on demand and more interactive
#This however is a proof of concept for demonstration purposes.
#Using the Wikipedia Article Mercury (planet) as the proof of concept
#https://en.wikipedia.org/wiki/Mercury_(planet)

mercury = wikipedia.page("Mercury (Planet)")

text = mercury.content

#nltk stuff
nltk.download('punkt') # used to parse the text into sentences
nltk.download('wordnet') # used to parse the sentences into words

sent_tokens = nltk.sent_tokenize(text)  # converts to list of sentences 
word_tokens = nltk.word_tokenize(text)  # converts to list of words

lemmer = nltk.stem.WordNetLemmatizer()  # used to consolidate different word forms


# returns cleaned list of consolidated tokens
def lemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]  

remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

# different method for removing non-alphanumeric characters
def lemNormalize(text):
    return lemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up","hey",)

GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]

# checks to see if the input text matches one of the greeting_inputs.  If so,
# return one of the random greeting_responses.
def greeting(sentence):
 
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)
        
from sklearn.feature_extraction.text import TfidfVectorizer  
from sklearn.metrics.pairwise import cosine_similarity  

def response(user_response):
    robo_response=''

    TfidfVec = TfidfVectorizer(tokenizer=lemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)  
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]

    if(req_tfidf==0):
        robo_response=robo_response+"I am sorry! I don't understand you"
        return robo_response
    else:
        robo_response = robo_response+sent_tokens[idx]
        return robo_response

flag=True
print("ROBO: My name is Robo. I will answer your queries about Chatbots. If you want to exit, type Bye!")

while(flag==True):
    user_response = input()
    user_response=user_response.lower()
    if(user_response!='bye'):
        if(user_response=='thanks' or user_response=='thank you' ):
            flag=False
            print("ROBO: You are welcome..")
        else:
            if(greeting(user_response)!=None):
                print("ROBO: "+greeting(user_response))
            else:
                sent_tokens.append(user_response)
                word_tokens=word_tokens+nltk.word_tokenize(user_response)
                final_words=list(set(word_tokens))
                print("ROBO: ",end="")
                print(response(user_response))
                sent_tokens.remove(user_response)
    else:
        flag=False
        print("ROBO: Bye! take care..")