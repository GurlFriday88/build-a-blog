from flask import Flask, request, request, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['DEBUG']=True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:haibane@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

#database model
class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    subtitle = db.Column(db.String(120))
    author = db.Column(db.String(30))
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text)

    def __init__(self, title, subtitle, author, date, content):
        self.title = title
        self.subtitle = subtitle
        self.author = author
        self.date = date
        self.content = content

#routes
@app.route('/index')
def index():
    current_posts = Blog.query.order_by(Blog.id.desc()).all()
    return render_template('index.html', current_posts=current_posts)

@app.route('/post/<int:new_post_id>')
def post(new_post_id):
    new_post = Blog.query.filter_by(id=new_post_id).first_or_404()
    return render_template('post.html', new_post=new_post)

#processes post form and adds entry to database
@app.route('/add_post', methods=['GET','POST'])
def add_post():
    if request.method == 'POST':
        new_title = request.form['title']    
        if not new_title:
            error = "Please enter a title."
            return render_template('add_post.html', error=error)

        new_subtitle = request.form['subtitle']
        new_author = request.form['author']
        new_content = request.form['content']
        date = datetime.now()
        new_post = Blog(new_title, new_subtitle, new_author, date, new_content)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('index'))
                
    return render_template('add_post.html')




if __name__ == '__main__':
    app.run()
