from data_preprocessing import ph_restos, ph_reviews, city_pop_densities
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ------------------------------------
# See average rating of restaurants per city
cities = ph_restos["City"].unique();
city_counts = ph_restos.groupby("City")["AverageRating"].count()
# print(type(city_counts))
city_means = ph_restos.groupby("City")["AverageRating"].mean()

print(pd.concat([city_counts, city_means], axis=1))
# print(cities)

# xpoints = list(city_pop_densities.values())
# ypoints = city_means.to_numpy()
# labels = list(city_pop_densities.keys())

# combined = list(zip(xpoints, ypoints, labels))
# combined.sort(key=lambda x: x[0])
# print(combined)

# x, y, _ = zip(*combined)

# plt.plot(x, y)

# plt.xlabel("City Population Densities (2020)")
# plt.ylabel("Average Ratings per City on Foodpanda (2025)")

# plt.show()

# city_count_pts = city_counts.to_numpy()
# combined_2 = list(zip(city_count_pts, ypoints))
# combined_2.sort(key=lambda x: x[0])

# x2, y2 = zip(*combined_2)
# plt.plot(x2, y2)

# plt.xlabel("Number of Foodpanda Stores/Restaurants per City")
# plt.ylabel("Average Ratings per City on Foodpanda (2025)")

# plt.show()

# ------------------------------------
# Boxplot of foodpanda ratings per city + medians
ratings_grouped_by_city = ph_restos.groupby("City")['AverageRating'];
datasets = []

for city in cities:
    rating_of_city = ratings_grouped_by_city.get_group(city)
    plt.hist(rating_of_city)
    plt.title("Histogram for Ratings of " + city)
    plt.xlabel("Rating")
    plt.ylabel("Amount of Ratings")
    plt.show()
    # datasets.append(rating_of_city)
    print(city, rating_of_city.median())

# plt.figure(figsize=(20, 6))
# box_plot = plt.boxplot(datasets, tick_labels=list(cities), showmeans=True)
# plt.xlabel("Cities")
# plt.ylabel("Average Ratings from Foodpanda")
# plt.xticks(rotation=45);
# plt.show()

# ------------------------------------
# Get the weighted average rating of a city 

# average_ratings_per_city = {};
# reviews_grouped_by_store = ph_reviews.groupby("StoreId");
# stores_grouped_by_city = ph_restos.groupby("City");

# for city in cities:
#     print(city)
#     stores = stores_grouped_by_city.get_group(city);
#     averageCityRating = 0;
#     cityReviews = 0;
#     for store in list(stores["StoreId"]):
#         if store in list(ph_reviews["StoreId"]):
#             reviews = reviews_grouped_by_store.get_group(store)["StoreId"].count()
#             cityReviews += reviews
#             averageCityRating += stores.loc[stores["StoreId"] == store, ["AverageRating"]].values[0] * reviews 
#             print(store, averageCityRating)
    
#     print(city, "Weighted Rating:", averageCityRating/cityReviews)
#     average_ratings_per_city[city] = (averageCityRating/cityReviews, cityReviews)

# print("-------------------- \n")
# print(average_ratings_per_city)