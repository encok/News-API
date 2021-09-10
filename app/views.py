from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    bbc = 'Hello World'
    return render_template('index.html',bbc = bbc)

@app.route('/source/<int:source_id>')
def source(source_id):

    '''
    View source page function that returns the source details page and its data
    '''
    return render_template('source.html',id = source_id)