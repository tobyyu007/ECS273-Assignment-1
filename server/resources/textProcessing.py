import matplotlib.pyplot as plt
import nltk
from wordcloud import WordCloud, STOPWORDS
from bs4 import BeautifulSoup
import re, string, unicodedata
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.stem import LancasterStemmer, WordNetLemmatizer
from collections import defaultdict


def preprocess(titles):
    nltk.download('stopwords')
    nltk.download('wordnet')
    nltk.download('omw-1.4')
    processedTitles = defaultdict(int)
    stopword_list = nltk.corpus.stopwords.words('english')
    tokenizer = ToktokTokenizer()
    lemmatizer = WordNetLemmatizer()

    for index, ogTitle in enumerate(titles):
        # Remove html strips
        soup = BeautifulSoup(ogTitle, "html.parser")
        ogTitle = soup.get_text()

        # Remove non-letter characters and convert the string to lower case
        ogTitle = re.sub('\[[^]]*\]', '', ogTitle)
        ogTitle = re.sub("[^a-zA-Z]", " ", ogTitle)
        ogTitle = ogTitle.lower()

        # Text stemming
        text = ' '.join([lemmatizer.lemmatize(word) for word in ogTitle.split()])

        # Remove stopwords
        tokens = tokenizer.tokenize(text)
        tokens = [token.strip() for token in tokens]
        filtered_tokens = [token for token in tokens if token not in stopword_list]
        filtered_text = ' '.join(filtered_tokens)

        for token in filtered_tokens:
            processedTitles[token] += 1

    print("Pre-process complete")
    return processedTitles


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