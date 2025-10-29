from flask import Flask,render_template,request 
app = Flask(__name__)
@app.route('/') 
def home():
    render_template('form.html')
@app.route('/result',methods='POST') 
def result():
    name = request.form['name']
    roll = request.form['roll']
    render_template('result.html',name,roll)
if __name__ == '__main__':
    app.run(host='0.0.0.5000',PORT=5000,debug=True)