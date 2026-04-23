from data_preprocessing import ph_restos, ph_reviews, city_pop_densities
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

cities = ph_restos["City"].unique()

for city in cities:
    stores_reviews = dict()
    stores_types = dict()
    store_codes = set()

    # Gets all City Store Codes
    for index, resto in ph_restos.iterrows():
        if resto["City"] == city: 
            store_codes.add(resto["StoreId"])
            stores_reviews[resto["FoodType"]] = 0 
            stores_types[resto["StoreId"]] = resto["FoodType"]

    # print(store_codes)

    for index, review in ph_reviews.iterrows():
        if review["StoreId"] in store_codes:
            food_type = stores_types[review["StoreId"]]
            stores_reviews[food_type] += 1

    # print(stores_reviews)

    top_5_types = list(stores_reviews.items())
    top_5_types.sort(key=lambda x: x[1], reverse=True)
    print(city, "Top 10 Foodpanda Resto Types:", top_5_types[:10])

    if (len(top_5_types) > 10):
        types, values = zip(*top_5_types[:10])
    else:
        types, values = zip(*top_5_types)
    types = list(types)
    values = list(values)

    plt.bar(types, values)
    plt.title("Foodpanda Resto Types in " + city.capitalize())
    plt.xlabel("Food Types")
    plt.ylabel("Amount of Reviews")
    plt.xticks(rotation=45)
    plt.show()
    # plt.pause(1)
    # plt.close()