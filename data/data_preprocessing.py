import pandas as pd
import re

ph_restos = pd.read_csv("ph_restos_2025.csv", keep_default_na=False)

# Lowercase store names & food type
ph_restos["CompleteStoreName"] = ph_restos["CompleteStoreName"].apply(str.lower)
ph_restos["FoodType"] = ph_restos["FoodType"].apply(str.lower)

# Drop row if 0 reviewers
ph_restos = ph_restos[ph_restos["Reviewers"] != 0]

# print(ph_restos)

ph_reviews = pd.read_csv("ph_reviews_2025.csv", keep_default_na=False)

# Lowercase review
ph_reviews["text"] = ph_reviews["text"].apply(str.lower)

# Remove all punctuation in reviews
ph_reviews["text"] = ph_reviews["text"].apply(lambda s: re.sub(r'[^a-zA-Z0-9 ]', "", s))

# Drop uuid & createdAt columns
ph_reviews = ph_reviews.drop(columns=["uuid", "createdAt", "likeCount", "isLiked"])

# print(ph_reviews)

# City population density from Phil Atlas (2020) per km^2
city_pop_densities = {
    'cebu city': 3061, # highly urbanized
    'dagupan pangasinan': 4682,
    'davao city davao del sur': 727, # highly urbanized
    'koronadal south cotabato': 705, 
    'lapu-lapu city cebu': 8565, # highly urbanized
    'makati city': 25189, # highly urbanized
    'malolos bulacan': 3884,
    'mandaluyong city': 45830, # highly urbanized
    'manila': 73920, # highly urbanized
    'marikina': 21192, # highly urbanized
    'muntinlupa city': 13672, # highly urbanized
    'ormoc leyte': 376,
    'pasay city': 31543, # highly urbanized
    'pasig city': 16574, # highly urbanized
    'quezon city': 17239, # highly urbanized
    'san juan': 21235, # highly urbanized
    'taguig city': 19613, # highly urbanized
    'valencia bukidnon': 369, 
}