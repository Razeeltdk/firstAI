import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk

nltk.download("punkt")
nltk.download("stopwords")

def preprocess_ingredients(ingredients):
    ingredients = ingredients.lower()
    ingredients = re.sub(r"[^\w\s]", "", ingredients)
    tokens = word_tokenize(ingredients)
    stop_words = set(stopwords.words("english"))
    tokens = [word for word in tokens if word not in stop_words]
    return tokens