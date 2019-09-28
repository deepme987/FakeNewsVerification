
# from bs4 import BeautifulSoup
# import urllib.request
# from googlesearch import search
from google import google
import nltk.stem.snowball
from nltk.stem import WordNetLemmatizer
import string


def remove_stopwords(title):
    global stopwords, lemmatizer

    title = set([x for x in title.split()]).difference(stopwords)
    title = " ".join(title).lower()
    for char in [',', '.', '\'', '!', ':']:
        title = title.replace(char, '')
    title = [lemmatizer.lemmatize(x) for x in title.split()]

    return " ".join(title)


def search_query(query):
    print("Searching for '{}' over internet".format(query))
    results = [result for result in google.search(query, 1)]
    # results.pop(2)
    score = dict()

    query = remove_stopwords(query)

    print(results)
    for i, result in enumerate(results):
        # score = dict()
        # source = urllib.request.urlopen(result).read()
        # soup = BeautifulSoup(source, 'lxml')
        result = remove_stopwords(result.description)
        print(result)
        for val in query.split():
            if i in score:
                if val in result:
                    # print(val, result)
                    score[i] += 1
            else:
                score[i] = 0

    print(score)
    print(query)


if __name__ == '__main__':
    stopwords = nltk.corpus.stopwords.words('english')
    stopwords.extend(string.punctuation)
    # stopwords.extend(['', '.', ','])
    stopwords = set(stopwords)
    lemmatizer = WordNetLemmatizer()
    search_query(input("Enter a search query: "))
