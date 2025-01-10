from models.recommender import RecipeRecommender

def main():
   
    recommender = RecipeRecommender("")

    # user input
    user_ingredients = input("Enter the ingredients you have (comma-separated): ")

    # recommendations
    recommended_recipes = recommender.recommend_recipes(user_ingredients)

    #  results
    print("\nRecommended Recipes:")
    print(recommended_recipes[["Recipe Name", "Ingredients"]])

if __name__ == "__main__":
    main()
