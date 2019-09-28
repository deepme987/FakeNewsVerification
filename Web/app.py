from flask import Flask, render_template, request, redirect
import pymongo

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
    print("news[0:10:1]")
    if request.method == 'POST':
        # print("Hi")
        title1= request.form['title']
        domain1=request.form['link']
        # print(domain1)
        # print(title1)
        return render_template('index.html', CONTEXT={'title': title1, 'do': domain1, 'news': news, 'flag':True})
    # return "hello world"
# def redirect():
#     message = request.form['title']
#     domain = request.form['link']
#     return(message)
# def run(message,domain):
#    return 'welcome %s' % name
    else:
        return render_template("index.html", CONTEXT={'news': news, 'flag': False})


if __name__ == '__main__':
    app.run(debug=True)
