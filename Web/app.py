from flask import Flask, render_template, request, redirect
import pickle


app = Flask(__name__)

    
@app.route('/index', methods=['POST', 'GET'])
def index():
    print("Index")
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
        return render_template('index.html', CONTEXT={'title': title1, 'do': domain1, 'flag': True, 'result': result})
    else:
        return render_template("index.html", CONTEXT={'flag': False})


if __name__ == '__main__':
    app.run(debug=True)
