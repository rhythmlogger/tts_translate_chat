from googletrans import Translator
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
translator = Translator()
CORS(app, resources={r'*': {'origins': '*'}})


@app.route('/translate')
def translate():
    text = request.args.get('text')
    result = translator.translate(text, dest='en').text
    print('결과:'+result)
    return {'result': result}


if __name__ == '__main__':
    app.run('127.0.0.1', 5000, debug=True)
    app.run(debug=True)
