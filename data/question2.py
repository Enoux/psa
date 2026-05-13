from data_preprocessing import ph_restos, ph_reviews, city_pop_densities
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import mannwhitneyu, kendalltau, shapiro

cities = ph_restos["City"].unique()
rural = set(['dagupan pangasinan', 'koronadal south cotabato', 'malolos bulacan', 'ormoc leyte', 'valencia bukidnon'])
hucs = dict()
non_hucs = dict()

for city in cities:
    stores_reviews = dict()
    stores_types = dict()
    store_codes = set()

    city_types = set()

    # Gets all City Store Codes
    for index, resto in ph_restos.iterrows():
        if resto["City"] == city: 
            store_codes.add(resto["StoreId"])
            stores_reviews[resto["FoodType"]] = 0 
            stores_types[resto["StoreId"]] = resto["FoodType"]
            city_types.add(resto["FoodType"])
    
    if city in rural:
        non_hucs[city] = len(city_types)
    else:
        hucs[city] = len(city_types)

print("HUC # of Resto Types:", hucs)
print("Non-HUC # of Resto Types:", non_hucs)

huc_pairs = list(hucs.items())
non_huc_pairs = list(non_hucs.items())

huc_pairs.sort(key=lambda x: x[1], reverse=True)
non_huc_pairs.sort(key=lambda x: x[1], reverse=True)

all_pairs = huc_pairs + non_huc_pairs
cities_huc, values_huc = zip(*huc_pairs)
cities_non_huc, values_non_huc = zip(*non_huc_pairs)
_, values_all = zip(*all_pairs)

cities_huc = list(cities_huc)
values_huc = list(values_huc)
cities_non_huc = list(cities_non_huc)
values_non_huc = list(values_non_huc)
values_all = list(values_all)

    # for index, review in ph_reviews.iterrows():
    #     if review["StoreId"] in store_codes:
    #         food_type = stores_types[review["StoreId"]]
    #         stores_reviews[food_type] += 1

    # print(stores_reviews)

    # top_5_types = list(stores_reviews.items())
    # top_5_types.sort(key=lambda x: x[1], reverse=True)
    # print(city, "Top 10 Foodpanda Resto Types:", top_5_types[:10])

    # if (len(top_5_types) > 10):
    #     types, values = zip(*top_5_types[:10])
    # else:
    #     types, values = zip(*top_5_types)
    # types = list(types)
    # values = list(values)

U1, p1 = mannwhitneyu(list(hucs.values()), list(non_hucs.values()), method="exact")
print("P value of HUCs vs non-HUCs (in terms of resto types):", p1)

all_pairs.sort(key=lambda x: x[0])
pop_densities = list(city_pop_densities.items())
pop_densities.sort(key=lambda x: x[0])

_, resto_types = zip(*all_pairs)
_, pop_density = zip(*pop_densities)
# print(all_pairs, pop_densities)
U2, p2 = kendalltau(pop_density, resto_types)
print("P value of Pop Densities -> Resto Types:", p2)
print("Shapiro-Wilk Test", shapiro(values_all).pvalue)

fig, axes = plt.subplots(1, 2, gridspec_kw={'width_ratios': [13, 5]}, figsize=(10, 5), sharey=True)

# First dataset
axes[0].bar(cities_huc, values_huc, color='blue')
axes[0].set_title("HUCs")
axes[0].set_ylabel("Amount of Food Types")
axes[0].tick_params(labelrotation=90, grid_color="r", grid_alpha=0.5)

# Second dataset
axes[1].bar(cities_non_huc, values_non_huc, color='green')
axes[1].set_title("Non-HUCs")
axes[1].set_ylabel("Amount of Food Types")
axes[1].tick_params(labelrotation=90, grid_color="r", grid_alpha=0.5)

# Third dataset (city pop densities)
# pop_densities = list(city_pop_densities.items())
# pop_densities.sort(key=lambda x: x[1], reverse=True)

# cities, densities = zip(*pop_densities)

# cities = list(cities)
# densities = list(densities)

# axes[2].bar(cities, densities, color='green')
# axes[2].set_title("Population Densities of Cities in Foodpanda")
# axes[2].set_ylabel("Population Density (pop/m^2)")
# axes[2].tick_params(labelrotation=90, grid_color="r", grid_alpha=0.5)

plt.tight_layout()
plt.show()

