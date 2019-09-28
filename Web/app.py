from flask import Flask, render_template, request, redirect
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
        return render_template('index.html', CONTEXT={'title': title1, 'do': domain1, 'flag':True})
    # return "hello world"
# def redirect():
#     message = request.form['title']
#     domain = request.form['link']
#     return(message)
# def run(message,domain):
#    return 'welcome %s' % name
    else:
        return render_template("index.html", CONTEXT={'flag': False})


if __name__ == '__main__':
    app.run(debug=True)
