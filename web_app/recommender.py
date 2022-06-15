"""
Contains a recommondation implementation:
model - NMF based, returns top 10 predicted movies

returns a list of movie names
"""

import pandas as pd
import numpy as np
from utils import top10_dict, movie_dict, average_dict, model, Q

# model -Functions to recommend with NMF recomendor

# 1 create user data frame with NaNs and add user reviews for 5 movies
def create_table(user_rating, movie_dict):
    user_df = pd.DataFrame(np.nan, index=[0], columns=movie_dict.values())
    for i, title in enumerate(user_rating.keys()):
        user_df[title][0] = user_rating[title]
    return user_df

# 2 Creates a data frame with user_specific recomendations
def calculate_recom(user_df, movie_dict, average_dict, Q):
    user_array = user_df.copy(deep=True).values
    for title in movie_dict.values():
        user_df.loc[user_df[title].isnull(),title] = 0    #average_dict[title]
    user_imp_array = user_df.values
    user_P = model.transform(user_imp_array)
    user_R = np.dot(user_P, Q)
    user_recom = pd.DataFrame({'user_input':user_array[0], 'predicted_ratings':user_R[0]}, index = user_df.columns)
    return user_recom

# 3 Main Function - activates 1-2 and finalizes top10 recom for user
def recommend_5(user_rating):
    user_df = create_table(user_rating, movie_dict)
    user_recom = calculate_recom(user_df, movie_dict, average_dict, Q)
    recom_5 = user_recom[user_recom['user_input'].isna()].sort_values(by = 'predicted_ratings', ascending= False).iloc[:5,:]
    return list(recom_5.index)
