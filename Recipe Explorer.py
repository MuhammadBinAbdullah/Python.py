pasta = ("Pasta Arrabiata", "Italian", 20, "Medium")
biryani = ("Chicken Biryani", "Indian", 45, "Hard")
print("Recipe 1 :", pasta)
print("Name :", pasta[0])
print("Cuisine :", pasta[1])
print("Difficulty :", pasta[-1])

all_recipes = (pasta, biryani)
print("\nFirst Recipe Name :", all_recipes[0][0])
print("Second Recipe Time :", all_recipes[1][2], "mins")

print("\nPasta Recipe Details :")
for detail in pasta:
    print(" -", detail)
    
pasta_ingredients = {"tomato", "garlic", "olive oil", "chilli", "pasta", "garlic"}
biryani_ingredients = {"rice", "chicken", "garlic", "onion", "tomato", "spices"}
print("\nPasta Ingredients :", pasta_ingredients)
print("Biryani Ingredients :", biryani_ingredients)
print("Total Pasta Ingredients :", len(pasta_ingredients))

pasta_ingredients.discard("chilli")
print("\nUpdated Pasta Ingredients :", pasta_ingredients)

all_ingredients = pasta_ingredients.union(biryani_ingredients)
common = pasta_ingredients.intersection(biryani_ingredients)
only_pasta = pasta_ingredients.difference(biryani_ingredients)
unique_to_each = pasta_ingredients.symmetric_difference(biryani_ingredients)

print("\nAll Ingredients (Union) :", all_ingredients)
print("Common Ingredients (Intersection) :", common)
print("Only In Pasta (Difference) :", only_pasta)
print("Not Shared (Sym. Difference) :", unique_to_each)