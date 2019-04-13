# from app import app
import urllib.request,json
from .models import Source,Articles

# Defining api urls and api_key
api_key = None
base_url = None
news_headlines_base_url = None
article_url= None

def configure_request(app):
    global api_key,base_url,article_url,news_headlines_base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['SOURCE_API_BASE_URL']
    article_url = app.config["ARTICLES_BASE_URL"]
    news_headlines_base_url = app.config['TOP_HEADLINES_BASE_URL']


def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_results(sources_results_list)
    return sources_results

def process_results(newsource_list):
    '''
    Function  that processes the new source result and transform them to a list of Objects
    Args:
        newsource_list: A list of dictionaries that contain news source details
    Returns :
        newsource_results: A list of newsource objects
    '''
    newsource_results = []
    for news_item in newsource_list:
        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')
        category = news_item.get('category')
        country = news_item.get('country')

        newsource_object = Source(id,name,description,url,category,country)
        newsource_results.append(newsource_object)

    return newsource_results

def get_source(source_id,limit):
    '''
    Function that gets the json response to our url request
    '''
    get_articles_url = article_url.format(source_id,limit,api_key)
    print(get_articles_url)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)
        
 
        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_articles(articles_results_list)

    return articles_results


def process_articles(source):
    source_articles = []
    for item_article in source:
        author = item_article.get('author')
        title = item_article.get('title')
        description = item_article.get('description')
        url = item_article.get('url')
        urlToImage = item_article.get('urlToImage')
        publishedAt = item_article.get('publishedAt')
        if urlToImage:
            articles_object = Articles(author,title,description,url,urlToImage,publishedAt)
            source_articles.append(articles_object)
    return source_articles


def get_headlines(size):

    get_headlines_url = news_headlines_base_url.format(size,api_key)

    with urllib.request.urlopen(get_headlines_url) as url:
        headlines_data = url.read()
        headlines_response = json.loads(headlines_data)
        
        headlines_results= None

        if headlines_response['articles']:
            headlines_list = headlines_response['articles']
            headlines_results = process_articles(headlines_list)

    return headlines_results

def search_article(article_name):
    search_article_url = search_artice_baseurl.format(article_name,api_key)
    with urllib.request.urlopen(search_article_url) as url:
        search_article_data =  url.read()
        search_article_response = json.loads(search_article_data)
        search_article_results = None
        if search_article_results['articles']:
            search_article_list= search_article_response['']
            search_article_results = process_artles(search_article_list)

    return search_article_results


