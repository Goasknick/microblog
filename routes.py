from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = { 'username' : 'Nick' }
    posts = [
            {
                'author':{'username':'John'},
                'body':'Beautiful day in the desert'
                },
            {
                'author':{'username':'Mary'},
                'body':'I love programming and making cool things'
                }
            ]

    return render_template('index.html', title='Home', user=user, posts=posts)


