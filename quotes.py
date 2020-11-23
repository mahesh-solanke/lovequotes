from flask import Flask , render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:mahesh@localhost/quotes'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://vevyyahweqgmvh:22d7b2245650a666f5ac6dfa33ff2b83c40d62972072f852c4f538424b46bdfc@ec2-3-213-106-122.compute-1.amazonaws.com:5432/ddva9hvf1boseh'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Lovequotes(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    author = db.Column(db.String(40))
    quote = db.Column(db.String(2000))


@app.route('/')
def index():
    result = Lovequotes.query.all()
    return render_template('index.html',result=result)


@app.route('/quotes')
def quotes():
    return render_template('quotes.html')

@app.route('/process',methods = ['POST'])
def process():
    author = request.form['author']
    quote = request.form['quote']
    quotedata = Lovequotes(author=author,quote=quote)
    db.session.add(quotedata)
    db.session.commit()

    return redirect(url_for('index'))
