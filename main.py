from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
  return render_template('index.html')

@app.route('/hello')
def hello():
	return render_template('hello.html')

@app.route('/hello/<name>')
def hello_name(name):
	return render_template('hello.html', name=name)

app.run(host='0.0.0.0', port=5000, debug=True)