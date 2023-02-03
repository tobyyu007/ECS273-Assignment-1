import pandas as pd
from resources.textProcessing import preprocess, ShowWordCloud
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import json
from collections import defaultdict, ChainMap

# https://www.kaggle.com/code/lakshmi25npathi/sentiment-analysis-of-imdb-movie-reviews
# https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews


def process(titlesPath, journalsPath):
    covid19Data = pd.read_csv("../server/data/COVID-19.csv")
    titles = preprocess(covid19Data['title'][1:200])
    publishTime = defaultdict(int)
    unknownTime = defaultdict(int)
    beforeTime = defaultdict(int)
    for time in covid19Data['publish_time'][1:]:
        if str(time).split('-')[0] != "nan":
            year = int(str(time).split('-')[0])
            if year < 2000:
                beforeTime["Before 2000"] += 1
            else:
                publishTime[year] += 1
        else:
            unknownTime["Unknown"] += 1

    publishTime = dict(sorted(publishTime.items()))
    publishTime = dict(ChainMap(publishTime, dict(beforeTime)))
    publishTime = dict(ChainMap(dict(unknownTime), publishTime))

    """
    journals = defaultdict(int)
    for journal in covid19Data['journal'][1:]:
        journals[journal] += 1
    journals = dict(sorted(journals.items(), key=lambda item: item[1], reverse=True))
    """

    with open(titlesPath, "w") as outputFile:
        json.dump(titles, outputFile)
    with open(journalsPath, "w") as outputFile:
        json.dump(publishTime, outputFile)