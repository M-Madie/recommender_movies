"""
UTILS 
- Helper functions to use in recommender.py and app.py
- Data: imported from pickled files
    - movies:
      1.top10_dict (Movie Name : Average Rating), used as Baseline_recommendor
      2.movie_dict (MovieId : Movie Title)
      3.average_Dict (Movie Title : Avergae Rating), used for imputation
- Models:
    - nmf_model: trained sklearn NMF model
"""
import pandas as pd
import numpy as np
import pickle

# Load pickled Dictionarries: 
# 1 - top10_dict
with open(r"top10_dict.pickle", "rb") as input_file:
    top10_dict = pickle.load(input_file)

# 2 - movie_dict
with open(r"movie_dict.pickle", "rb") as input_file:
    movie_dict = pickle.load(input_file)

# 3 - average_dict
with open(r"average_dict.pickle", "rb") as input_file:
    average_dict = pickle.load(input_file)

#load saved NMF model + Calculate Q
with open(r"nmf_movierecomendor250.pickle", "rb") as input_file:
    model = pickle.load(input_file)
Q = model.components_
