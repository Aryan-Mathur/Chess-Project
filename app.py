from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "<b>Hello Aryan</b>"

@app.route('/polu')
def polu():
    return "<p>Hello polu<p>"
    
if __name__ == '__main__':
    app.run()
