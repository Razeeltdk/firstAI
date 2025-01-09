from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(user_ingredients, recipe_ingredients):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(recipe_ingredients)
    user_vector = vectorizer.transform([user_ingredients])
    similarities = cosine_similarity(user_vector, tfidf_matrix).flatten()
    return similarities