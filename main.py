import flask from flask, redirect, request

app = Flask(__name__)
app.config['DEBUG']=True



@app.route('/')
def home():
    return "hello World"





app.run()
    
