from flask import render_template
from app import app
from .requests import get_news

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    all_news = get_news('all')
    print(all_news)
    title = 'Home - Welcome to daily news center'
    return render_template('index.html', title = title, all = all_news)

@app.route('/news/<news_sources>')
def news(news_sources):

    '''
    View news page function that returns the news details page and its data
    '''
    return render_template('news.html',id = news_sources)


