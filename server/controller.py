import pandas as pd
from resources.textProcessing import preprocess, ShowWordCloud
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import json
from collections import defaultdict, ChainMap

# https://www.kaggle.com/code/lakshmi25npathi/sentiment-analysis-of-imdb-movie-reviews
# https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews


def process(titlesPath, journalsPath):
    pd.set_option('display.max_colwidth', None)
    covid19Data = pd.read_csv("../server/data/COVID-19.csv")
    #print(covid19Data['abstract'][:2])
    abstracts = preprocess(covid19Data['abstract'][:])
    abstracts = dict(sorted(abstracts.items(), key=lambda item: item[1], reverse=True))
    abstractsSliced = {a: abstracts[a] for a in list(abstracts)[:500]}  # 取出次數前五百名
    print(abstractsSliced)

    publishTime = defaultdict(int)
    unknownTime = defaultdict(int)
    beforeTime = defaultdict(int)
    allTime = defaultdict(int)
    special = ""
    for index, time in enumerate(covid19Data['publish_time'][1:]):
        if str(time).split('-')[0] != "nan":
            year = int(str(time).split('-')[0])
            if year < 2020:
                beforeTime["Before 2020"] += 1
            elif year > 2023:
                unknownTime["Unknown"] += 1
            else:
                publishTime[year] += 1
        else:
            unknownTime["Unknown"] += 1
    #print(covid19Data['publish_time'][special])
    publishTime = dict(sorted(publishTime.items()))
    publishTime = dict(ChainMap(publishTime, dict(beforeTime)))
    publishTime = dict(ChainMap(dict(unknownTime), publishTime))

    """
    journals = defaultdict(int)
    for journal in covid19Data['journal'][1:]:
        journals[str(journal)] += 1
    journals["Unknown"] = journals.pop('nan')
    journals = dict(sorted(journals.items(), key=lambda item: item[1], reverse=True))
    print({k: journals[k] for k in list(journals)[:10]})
    """

    with open(titlesPath, "w") as outputFile:
        json.dump(abstractsSliced, outputFile)
    with open(journalsPath, "w") as outputFile:
        json.dump(publishTime, outputFile)