import pandas as pd
import re

ph_restos = pd.read_csv("ph_restos_2025.csv")

# Lowercase store names & food type
ph_restos["CompleteStoreName"] = ph_restos["CompleteStoreName"].apply(str.lower)
ph_restos["FoodType"] = ph_restos["FoodType"].astype(str)
ph_restos["FoodType"] = ph_restos["FoodType"].apply(str.lower)

# print(ph_restos)

ph_reviews = pd.read_csv("ph_reviews_2025.csv")

# Lowercase review
ph_reviews["text"] = ph_reviews["text"].astype(str)
ph_reviews["text"] = ph_reviews["text"].apply(str.lower)

# Remove all punctuation in reviews
ph_reviews["text"] = ph_reviews["text"].apply(lambda s: re.sub(r'[^a-zA-Z0-9 ]', "", s))

# Drop uuid & createdAt columns
ph_reviews = ph_reviews.drop(columns=["uuid", "createdAt", "likeCount", "isLiked"])

print(ph_reviews)