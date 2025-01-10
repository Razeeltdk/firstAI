import pandas as pd
# The Ingredients column contains comma-separated values, that will be preprocessed
# Define the data
data = {
    "Recipe Name": [
        "Spaghetti Bolognese", "Chicken Curry", "Vegetable Stir Fry", "Tomato Soup",
        "Grilled Cheese Sandwich", "Pasta Carbonara", "Fruit Salad", "Omelette",
        "Pancakes", "Caesar Salad"
    ],
    "Ingredients": [
        "tomato, onion, garlic, beef, spaghetti, olive oil, salt, pepper",
        "chicken, onion, garlic, curry powder, coconut milk, salt, pepper",
        "carrot, broccoli, bell pepper, soy sauce, garlic, ginger, olive oil",
        "tomato, onion, garlic, vegetable stock, cream, salt, pepper",
        "bread, cheese, butter",
        "pasta, egg, bacon, parmesan cheese, garlic, salt, pepper",
        "apple, banana, orange, grapes, yogurt, honey",
        "egg, milk, salt, pepper, cheese, tomato",
        "flour, milk, egg, sugar, baking powder, butter",
        "lettuce, croutons, parmesan cheese, chicken, caesar dressing"
    ],
    "Instructions": [
        "1. Cook spaghetti. 2. Fry beef with onion and garlic. 3. Add tomatoes and simmer. 4. Serve with spaghetti.",
        "1. Cook chicken with onion and garlic. 2. Add curry powder and coconut milk. 3. Simmer until cooked. 4. Serve with rice.",
        "1. Heat oil in a pan. 2. Add garlic and ginger. 3. Stir fry vegetables. 4. Add soy sauce and serve.",
        "1. Cook onion and garlic. 2. Add tomatoes and stock. 3. Blend until smooth. 4. Add cream and serve.",
        "1. Butter the bread. 2. Add cheese between slices. 3. Grill until golden brown. 4. Serve hot.",
        "1. Cook pasta. 2. Fry bacon with garlic. 3. Mix eggs and cheese. 4. Combine everything and serve.",
        "1. Chop fruits. 2. Mix with yogurt and honey. 3. Serve chilled.",
        "1. Beat eggs with milk. 2. Pour into a hot pan. 3. Add cheese and tomato. 4. Fold and serve.",
        "1. Mix dry ingredients. 2. Add wet ingredients. 3. Cook on a hot pan. 4. Serve with syrup.",
        "1. Chop lettuce. 2. Add croutons and cheese. 3. Top with chicken. 4. Drizzle dressing and serve."
    ]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("data/recipes.csv", index=False)
