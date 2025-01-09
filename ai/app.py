from models.recommender import RecipeRecommender

def main():
    # Initialize the recommender
    recommender = RecipeRecommender("")

    # Get user input
    user_ingredients = input("Enter the ingredients you have (comma-separated): ")

    # Get recommendations
    recommended_recipes = recommender.recommend_recipes(user_ingredients)

    # Display results
    print("\nRecommended Recipes:")
    print(recommended_recipes[["Recipe Name", "Ingredients"]])

if __name__ == "__main__":
    main()