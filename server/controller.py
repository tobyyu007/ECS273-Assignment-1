import pandas as pd
from resources.textProcessing import preprocess
import json
from collections import defaultdict, ChainMap


def process(titlesPath, journalsPath):
    covid19Data = pd.read_csv("../server/data/COVID-19.csv")

    # 處理 abstract
    abstracts = preprocess(covid19Data['abstract'][:])
    abstracts = dict(sorted(abstracts.items(), key=lambda item: item[1], reverse=True))
    abstractsSliced = {a: abstracts[a] for a in list(abstracts)[:500]}  # 取出次數前五百名
    print(abstractsSliced)

    # 處理 publish time
    publishTime = defaultdict(int)
    unknownTime = defaultdict(int)
    beforeTime = defaultdict(int)
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
    publishTime = dict(sorted(publishTime.items()))
    publishTime = dict(ChainMap(publishTime, dict(beforeTime)))
    publishTime = dict(ChainMap(dict(unknownTime), publishTime))

    with open(titlesPath, "w") as outputFile:
        json.dump(abstractsSliced, outputFile)
    with open(journalsPath, "w") as outputFile:
        json.dump(publishTime, outputFile)

# process("../server/data/titles.json", "../server/data/publishTime.json")