from flask import render_template
from app import app
from .request import get_news

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    popular_news = get_news('popular')
    print(popular_news)
    title = 'Home - Welcome to The best News Review Website Online'
    return render_template('index.html', title = title, popular=popular_news)

@app.route('/source/<int:source_id>')
def source():

    '''
    View source page function that returns the source details page and its data
    '''
    title = 'Home - Welcome to The best News Review Website Online'
    return render_template('source.html', title = title)