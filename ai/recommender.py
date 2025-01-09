import pandas as pd
from utils.preprocess import preprocess_ingredients
from utils.similarity import calculate_similarity

class RecipeRecommender:
    def __init__(self, dataset_path):
        self.df = pd.read_csv(dataset_path)
        self.df["processed_ingredients"] = self.df["Ingredients"].apply(preprocess_ingredients)
        self.df["ingredients_str"] = self.df["processed_ingredients"].apply(lambda x: " ".join(x))

    def recommend_recipes(self, user_ingredients, top_n=5):
        user_ingredients = preprocess_ingredients(user_ingredients)
        user_ingredients_str = " ".join(user_ingredients)
        similarities = calculate_similarity(user_ingredients_str, self.df["ingredients_str"])
        top_indices = similarities.argsort()[-top_n:][::-1]
        return self.df.iloc[top_indices]