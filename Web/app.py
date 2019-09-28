from flask import Flask, render_template, request
import pickle
from googlescrapper import Scrapper


app = Flask(__name__)

    
@app.route('/index', methods=['POST', 'GET'])
def index():
    print("Index")
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
        return render_template("index.html", CONTEXT={'flag': False})


if __name__ == '__main__':
    app.run(debug=True)
