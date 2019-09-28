<<<<<<< HEAD
from flask import Flask, render_template, request
=======
from flask import Flask, render_template, request, redirect
import pymongo
>>>>>>> 61f88a142f8b35f74569957ca4087082b552f851
import pickle
from googlescrapper import Scrapper


app = Flask(__name__)

@app.route('/index', methods=['POST', 'GET'])
def index():
    print("Index")
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    print("1")
    mydb = myclient["mydatabase"]
    print("2")
    FakeNews = mydb["Fake_News"]
    print("3")
    news = FakeNews.find({}, {"_id":0, "Title": 1, "Domain": 1})
    print(news[0:7])
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

        print("Scrapper: ", sc_result, sc_prob)

        result = sc_result

        return render_template('index.html', CONTEXT={'title': title1, 'do': domain1,
                                                      'flag': True, 'result': result, 'conf': sc_prob})

    else:
        return render_template("index.html", CONTEXT={'news': news, 'flag': False})


if __name__ == '__main__':
    app.run(debug=True)
