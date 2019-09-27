import bs4 as bs
import requests
from googlesearch import search


def search_query(query):
    print("Searching for '{}' over internet".format(query))

    for result in search(query, tld="co.in", num=10, stop=10):
        print(result)

    


if __name__ == '__main__':
    search_query(input("Enter a search query: "))
