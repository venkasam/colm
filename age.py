from xml.etree.ElementTree import indent
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

df=pd.read_csv("final.csv")
df=df[df["soup"].notna()]
count=CountVectorizer(stop_words="english")
count_matrice=count.fit_transform(df["soup"])
cosinesim=cosine_similarity(count_matrice,count_matrice)
df=df.reset_index()
indices=pd.Series(df.index,index=df["title"])
def get(title):
    idx=indices[title]
    simp=list(enumerate(cosinesim[idx]))
    simp=sorted(simp,key=lambda x:x[1], reverse=True)
    simp=simp[1:11]
    movieindcies=[i[0] for i in simp]
    return df[["title","vote_count","vote_average","poster_links"]].iloc[movieindcies].values.tolist()