import pandas as pd
from resources.textProcessing import preprocess, ShowWordCloud
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import json

# https://www.kaggle.com/code/lakshmi25npathi/sentiment-analysis-of-imdb-movie-reviews
# https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews


def process(method: str = 'PCA') -> tuple[list[dict], list[int]]:
    imdbData = pd.read_csv("../server/data/IMDB Dataset.csv")
    #print(imdbData.head(10))
    positive, negative = preprocess(imdbData['review'][1:200], imdbData['sentiment'][1:200])
    with open("../server/data/positiveData.json", "w") as outputFile:
        json.dump(positive, outputFile)
    with open("../server/data/negativeData.json", "w") as outputFile:
        json.dump(negative, outputFile)