from flask import Flask, render_template, request, redirect
import pymongo
import pickle


app = Flask(__name__)
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
print("4")
mydb = myclient["mydatabase"]
print("5")
FakeNews = mydb["Fake_News"]
title1 = None

@app.route('/index', methods=['POST', 'GET'])
def index():
    global title1
    news = FakeNews.find({}, {"_id":0, "Title": 1, "Domain": 1})
    print(news[0:7])
    if request.method == 'POST':
        # print("Hi")
        title1= request.form['title']
        domain1=request.form['link']
        # print(domain1)
        # print(title1)
        with open("NaiveBayes/NB.pickle", 'rb') as file:
            nb = pickle.load(file)

        with open("NaiveBayes/cvec.pickle", 'rb') as file:
            cvec = pickle.load(file)

        result = "Real" if nb.predict(cvec.transform([title1])) == [0] else "Fake"
        print(result)
        return render_template('index.html', CONTEXT={'title': title1, 'news' : news,'do': domain1, 'flag': True, 'result': result})
    else:
        return render_template("index.html", CONTEXT={'news': news, 'flag': False})


@app.route('/store', methods=['POST', 'GET'])
def button_press():
    global title1
    if request.method == 'POST':
        FakeNews.insert_one({"Title": title1})
        return render_template('index.html', CONTEXT={})


if __name__ == '__main__':
    app.run(debug=True)
