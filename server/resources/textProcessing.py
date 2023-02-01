import matplotlib.pyplot as plt
import nltk
from wordcloud import WordCloud, STOPWORDS
from bs4 import BeautifulSoup
import re, string, unicodedata
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.stem import LancasterStemmer, WordNetLemmatizer
from collections import defaultdict


def preprocess(ogReviews, sentiments):
    nltk.download('stopwords')
    nltk.download('wordnet')
    nltk.download('omw-1.4')
    positive = defaultdict(int)
    negative = defaultdict(int)
    stopword_list = nltk.corpus.stopwords.words('english')
    tokenizer = ToktokTokenizer()
    lemmatizer = WordNetLemmatizer()

    for index, ogReview in enumerate(ogReviews):
        # Remove html strips
        soup = BeautifulSoup(ogReview, "html.parser")
        ogReview = soup.get_text()

        # Remove non-letter characters and convert the string to lower case
        ogReview = re.sub('\[[^]]*\]', '', ogReview)
        ogReview = re.sub("[^a-zA-Z]", " ", ogReview)
        ogReview = ogReview.lower()

        # Text stemming
        text = ' '.join([lemmatizer.lemmatize(word) for word in ogReview.split()])

        # Remove stopwords
        tokens = tokenizer.tokenize(text)
        tokens = [token.strip() for token in tokens]
        filtered_tokens = [token for token in tokens if token not in stopword_list]
        filtered_text = ' '.join(filtered_tokens)

        if sentiments[index + 1] == "positive":
            for token in filtered_tokens:
                positive[token] += 1
        else:
            for token in filtered_tokens:
                negative[token] += 1

    print("Process complete")
    return positive, negative


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