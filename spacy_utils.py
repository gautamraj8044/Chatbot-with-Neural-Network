import spacy
import numpy as np
nlp = spacy.load('en_core_web_sm')

def tokenize(sentence):
    doc = nlp(sentence)
    return [token.text for token in doc]

def stem(word):
    doc = nlp(word)
    return doc[0].lemma_

def bag_of_words(tokenized_sentence, words):
    sentence_words = [stem(word) for word in tokenized_sentence]
    bag = np.zeros(len(words), dtype=np.float32)
    for idx, w in enumerate(words):
        if w in sentence_words:
            bag[idx] = 1
    return bag
