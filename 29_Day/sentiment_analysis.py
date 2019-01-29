# Dependencies 
from textblob import TextBlob # Its provide a simple API to do NLP task
sent1 = "It was awesome day with you"
sent2 = "When i can't talk with you then my day goes wrong"
pre_sent1 = TextBlob(sent1)
pre_sent2 = TextBlob(sent2)
print(pre_sent1.sentiment)
print(pre_sent2.sentiment)
