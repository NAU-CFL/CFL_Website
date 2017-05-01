import subprocess
from app import app
from flask import render_template, make_response, redirect

# Route decorators to referance urls
@app.route('/')
def index():
    user = {'nickname': 'Kemal'}  # fake user
    posts = [  # fake array of posts
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)
@app.route('/scripts')
def scripts():
    return render_template('scripts.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/people')
def people():
    return render_template('people.html')

@app.route('/research')
def research():
    return render_template('research.html')

# Blog page will be linked to jekyll-markdown blog
@app.route('/blog')
def blog():
    return redirect('http://eneskemalergin.github.io')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# Error Handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
