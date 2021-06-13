# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 16:29:47 2021

@author: user
"""
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_title_from_index(index):
	return df[df.index == index]["title"].values[0]

def get_index_from_title(title):
	return df[df.title == title]["index"].values[0]
df=pd.read_csv("movie_dataset.csv")
#print(df.head)
#print(df.shape)
#print(df.columns)
features=["keywords","cast","genres","director"]
for feature in features:
    df[feature]=df[feature].fillna("")
def combine_features(row):
    return row["keywords"]+" "+row["cast"]+" "+row["genres"]+" "+row["director"]
df["combined_features"]=df.apply(combine_features,axis=1)
#print(df["combined_features"].head)
cv=CountVectorizer()
count_matrix=cv.fit_transform(df["combined_features"])
movie_user_likes="Avatar"
similarity_score=cosine_similarity(count_matrix)
movie_index=get_index_from_title(movie_user_likes)
similar_movies=list(enumerate(similarity_score[movie_index]))
sorted_similar_movies=sorted(similar_movies,key=lambda x:x[1],reverse=True)
i=0
for movie in sorted_similar_movies:
    print(get_title_from_index(movie[0]))
    i=i+1
    if i>50:
        break
