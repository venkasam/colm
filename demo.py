from os import access
from turtle import pd
import numpy as np
import pandas as pd
df=pd.read_csv("final.csv")
c=df["vote_average"].mean()
m=df["vote_count"].quantile(0.9)
qmovie=df.copy().loc[df["vote_count"]>=m]
def rated(x,m=m,c=c):
    v=x["vote_count"]
    r=x["vote_average"]
    return (v/(v+m)*r)+(m/(m+v)*c)
qmovie["score"]=qmovie.apply(rated,axis=1)
qmovie=qmovie.sort_values("score",ascending=False)
output=qmovie[["title","vote_count","vote_average","poster_link"]].head(20).values.tolist()

