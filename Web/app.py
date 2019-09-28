from flask import Flask, render_template, request, redirect
import pymongo
import pickle
import math
from googlescrapper import Scrapper


app = Flask(__name__)
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
FakeNews = mydb["Fake_News"]
title1 = None
result = ""

@app.route('/index', methods=['POST', 'GET'])
def index():
    global title1
    news = FakeNews.find({}, {"_id":0, "Title": 1, "Domain": 1})
    if request.method == 'POST':
        title1= request.form['title']
        domain1=request.form['link']
        with open("Models/NB.pickle", 'rb') as file:
            nb = pickle.load(file)

        with open("Models/cvec.pickle", 'rb') as file:
            cvec = pickle.load(file)

        nb_result = "Real" if nb.predict(cvec.transform([title1])) == [0] else "Fake"
        print("NB: ", nb_result)

        scrapper = Scrapper()
        sc_result, sc_prob = scrapper.search_query(title1)
        sc_prob = round(sc_prob, 4)
        print("Scrapper: ", sc_result, sc_prob)

        result = sc_result

        return render_template('index.html', CONTEXT={'title': title1, 'do': domain1,
                                                      'flag': True, 'result': result, 'conf': sc_prob * 100})

    else:
        return render_template("index.html", CONTEXT={'news': news, 'flag': False})


@app.route('/store', methods=['POST', 'GET'])
def button_press():
    global title1
    if request.method == 'POST':
        if result=="Real":
            FakeNews.insert_one({"Title": title1})
            return render_template('index.html', CONTEXT={})

    return redirect("/index")


if __name__ == '__main__':
    app.run(debug=True)
