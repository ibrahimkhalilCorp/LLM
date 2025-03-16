import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
nltk.download('all')
nltk.download('punkt')

text = "Natural Language Processing is fascinating! Let's explore it step by step."
print("Sentences:", sent_tokenize(text))
print("Words:", word_tokenize(text))


# import spacy

# nlp = spacy.load("en_core_web_sm")
# text = "Natural Language Processing is fascinating! Let's explore it step by step."
# doc = nlp(text)

# sentences = [sent.text for sent in doc.sents]
# words = [token.text for token in doc]

# print("Sentences:", sentences)
# print("Words:", words)
