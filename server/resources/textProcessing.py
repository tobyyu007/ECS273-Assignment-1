from collections import defaultdict
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from tqdm import tqdm
from paperai.highlights import Highlights
from txtai.pipeline import Tokenizer
from wordcloud import STOPWORDS


def preprocess(abstracts):
    nltk.download('stopwords')
    nltk.download('wordnet')
    nltk.download('omw-1.4')
    processedAbstracts = defaultdict(int)
    lemmatizer = WordNetLemmatizer()

    # 使用 paperai、nltk 和 wordcloud stopwords
    unionStopWords = Highlights.STOP_WORDS.union(set(stopwords.words("english")), set(STOPWORDS))

    for ogAbstract in tqdm(abstracts):
        if str(ogAbstract) != "nan":  # 在資料集中有資料
            # tokenize 並移除 stopword
            tokened = []
            for token in Tokenizer.tokenize(ogAbstract.lower()):
                if token not in unionStopWords:
                    tokened.append(token)

            # word lemmatisation
            for word in tokened:
                processedAbstracts[lemmatizer.lemmatize(word)] += 1

    return processedAbstracts
