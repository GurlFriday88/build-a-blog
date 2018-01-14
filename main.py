from flask import Flask, request, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG']=True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:haibane@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    subtitle = db.Column(db.String(50))
    author = db.Column(db.String(30))
    content = db.Column(db.Text)

    def __init__(self, title, subtitle, author, content):
        self.title = title
        self.subtitle = subtitle
        self.author = author
        self.content = content


@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/post')
def post():

    return render_template('post.html')


@app.route('/add_post', methods=['GET','POST'])
def add_post():
    if request.method == 'POST':
        new_title = request.form['title']
        new_subtitle = request.form['subtitle']
        new_author = request.form['author']
        new_content = request.form['content']
        
        new_post = Blog(new_title, new_subtitle, new_author, new_content)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_post.html')




if __name__ == '__main__':
    app.run()
