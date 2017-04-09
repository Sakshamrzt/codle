from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def infdex():
   return render_template('index.html')

@app.route('/login',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("index.html",username = username, password = password)

if __name__ == '__main__':
   app.run(debug = True)