import re
from collections import defaultdict
import matplotlib.pyplot as plt
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.stem.porter import PorterStemmer
from wordcloud import WordCloud, STOPWORDS
from tqdm import tqdm
import string

def preprocess(abstracts):
    nltk.download('stopwords')
    nltk.download('wordnet')
    nltk.download('omw-1.4')
    processedAbstracts = defaultdict(int)
    tokenizer = ToktokTokenizer()
    lemmatizer = WordNetLemmatizer()
    nltkStopWord = nltk.corpus.stopwords.words('english')
    wordCloudStopWord = set(STOPWORDS)
    porterStemmer = PorterStemmer()

    for ogAbstract in tqdm(abstracts):
        if str(ogAbstract) != "nan":  # 在資料集中有資料
            # 只保留字母，再將文字轉為小寫
            # Remove non-letter characters and convert the string to lower case
            reTitle = re.sub('[^a-zA-Z]', " ", ogAbstract)
            reTitle = reTitle.lower()

            # 切字 Tokenization
            tokens = tokenizer.tokenize(reTitle)
            tokens = [token.strip() for token in tokens]

            # 移除 stopwords
            stopped = []
            for token in tokens:
                if token not in nltkStopWord and token not in wordCloudStopWord:
                    stopped.append(token)

            # Text stemming
            #stemmed = [porterStemmer.stem(word) for word in stopped]
            lemmatized = [lemmatizer.lemmatize(word) for word in stopped]
            #stemmed = [porterStemmer.stem(word) for word in lemmatized]

            for word in lemmatized:
                if len(word) > 1:  # 不要包含單一字母 (可能是代號)
                    processedAbstracts[word] += 1

    return processedAbstracts


def ShowWordCloud(word_list: list[str]):
    all_words = " ".join(word_list)

    wordcloud = WordCloud(width=700, height=700,
                          background_color='white',
                          min_font_size=10).generate(all_words)

    # plot the WordCloud image
    plt.figure(figsize=(5, 5), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)

    plt.show()
