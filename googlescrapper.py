
from googleapi import google
from nltk.stem import WordNetLemmatizer
import pickle


class Scrapper:
    def __init__(self):
        with open("Models/stopwords.pickle", 'rb') as file:
            self.stopwords = pickle.load(file)
        self.lemmatizer = WordNetLemmatizer()

    def remove_stopwords(self, title):
        title = set([x for x in title.split()]).difference(self.stopwords)
        title = " ".join(title).lower()
        for char in [',', '.', '\'', '!', ':']:
            title = title.replace(char, '')
        title = [self.lemmatizer.lemmatize(x) for x in title.split()]

        return " ".join(title)

    def search_query(self, query):
        print("Scrapping: ", query)
        results = [result for result in google.search(query, 1)]
        score = dict()

        query = self.remove_stopwords(query)

        for i, result in enumerate(results):
            result = self.remove_stopwords(result.description)
            for val in query.split():
                if i in score:
                    if val in result:
                        score[i] += 1
                else:
                    score[i] = 0

        try:
            avg, n = sum(score.values()) / len(score.values()), len(query.split())
        except ZeroDivisionError:
            return "Cannot fetch results, please try again after a while", -1

        if avg > n // 2:
            return "Real", avg / n
        else:
            return "Fake", avg / n


if __name__ == '__main__':
    sc = Scrapper()
    print("This is a sample example:")
    print(sc.search_query("Akshay: I will work with Sajid if he is acquitted"))


# def remove_stopwords(title):
#     global stopwords, lemmatizer
#
#     title = set([x for x in title.split()]).difference(stopwords)
#     title = " ".join(title).lower()
#     for char in [',', '.', '\'', '!', ':']:
#         title = title.replace(char, '')
#     title = [lemmatizer.lemmatize(x) for x in title.split()]
#
#     return " ".join(title)
#
#
# def search_query(query):
#     print("Searching for '{}' over internet".format(query))
#     results = [result for result in search(query, 1)]
#     # results.pop(2)
#     score = dict()
#
#     query = remove_stopwords(query)
#
#     print(results)
#     for i, result in enumerate(results):
#         # score = dict()
#         # source = urllib.request.urlopen(result).read()
#         # soup = BeautifulSoup(source, 'lxml')
#         result = remove_stopwords(result.description)
#         print(result)
#         for val in query.split():
#             if i in score:
#                 if val in result:
#                     # print(val, result)
#                     score[i] += 1
#             else:
#                 score[i] = 0
#
#     print(score)
#     print(query)
#
#
# if __name__ == '__main__':
#     stopwords = nltk.corpus.stopwords.words('english')
#     stopwords.extend(string.punctuation)
#     # stopwords.extend(['', '.', ','])
#     stopwords = set(stopwords)
#     lemmatizer = WordNetLemmatizer()
#     search_query(input("Enter a search query: "))
