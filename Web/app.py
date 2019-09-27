from flask import Flask, render_template, request, redirect
app = Flask(__name__)

    
@app.route('/index', methods=['POST', 'GET'])
def index():
    print("Index")
    if request.method == 'POST':
        print("Hi")
        title1= request.form['title']
        domain1=request.form['link']
        print(domain1)
        print(title1)
        return render_template('index.html', CONTEXT={'test': title1, 'do': domain1})
    # return "hello world"
# def redirect():
#     message = request.form['title']
#     domain = request.form['link']
#     return(message)
# def run(message,domain):
#    return 'welcome %s' % name
    return render_template("index.html", CONTEXT=None)


if __name__ == '__main__':
    app.run(debug=True)
