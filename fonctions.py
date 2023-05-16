from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

import string

def text_processing(text):
     #Charger les stop-words en anglais
    stop_words = set(stopwords.words('english'))

    # Initialiser le lemmatizer
    lemmatizer = WordNetLemmatizer()

    # Appliquer la tokenisation à tous les textes
    tokens = word_tokenize(text.lower())

    # Supprimer les ponctuations
    tokens = [word for word in tokens if word not in string.punctuation]
    

    # Supprimer les stop-words
    tokens = [word for word in tokens if word not in stop_words]
    
    # Supprimer les stop-words BIS
    tokens = [word for word in tokens if word[0:4] != "http"]
    tokens = [word for word in tokens if word[0:7] != "//t.co/"]
    

    # Appliquer la lemmatisation à tous les tokens
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    
    
    # Supprimer les stop-words après lemmatisation
    tokens = [word for word in tokens if len(word) > 1]
    tokens = [word for word in tokens if word[0] != "'"]
    tokens = [word for word in tokens if word != "n't"]
    tokens = [word for word in tokens if word != "amp"]
    tokens = [word for word in tokens if word != "new"]
    tokens = [word for word in tokens if word != "one"]
    tokens = [word for word in tokens if word != "like"]
    tokens = [word for word in tokens if word != "get"]
    tokens = [word for word in tokens if word != "would"]
    
    tokens = [word for word in tokens if word[0:len("\x89")] != "\x89"]
    tokens = [word for word in tokens if word[0:len("û_")] != "û_"]
    tokens = [word for word in tokens if word[0:len("û")] != "û"]
    
    tokens = ' '.join(tokens)
    
    return tokens