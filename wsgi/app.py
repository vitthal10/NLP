from flask import Flask , jsonify, render_template
from textblob import TextBlob
from textblob import Word

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/api/v1/sentiment/<message>')
def sentiment(message):
	text = TextBlob(message)
	response = {'polarity' : text.polarity , 'subjectivity' : text.subjectivity}
	return jsonify(response)
	
@app.route('/api/v1/pos/<message>')
def pos(message):
	text = TextBlob(message)
	response = {'pos' : text.tags}
	return jsonify(response)

@app.route('/api/v1/lem/<message>')
def lem(message):
	defnn = ''.join(Word(message).definitions)
	response = {'defn' : defnn}
	return jsonify(response)
	
@app.route('/api/v1/langtrans/<message>')
def langtrans(message):
	text = TextBlob(message)
	response = {'french' : str(text.translate(to='fr')), 'spanish' : str(text.translate(to='es'))}
	return jsonify(response)
	
@app.route('/api/v1/spellcheck/<message>')
def spellcheck(message):
	text = TextBlob(message)
	cc = ''+text.correct()
	response = {'crt' : cc}
	return jsonify(response)

if __name__ == "__main__":
	app.run(debug=True)
