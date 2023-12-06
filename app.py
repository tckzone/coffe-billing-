from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Heroku with Flask!'

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
