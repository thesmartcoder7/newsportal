from app import models
import urllib.request,json

Article = models.Article
Source = models.Source

api_key = None
country_based_headlines = None
country_base_headlines_category = None
source_headlines = None
all_sources = None


def configure_request(app):
    global api_key, country_based_headlines, country_base_headlines_category, source_headlines, all_sources
    api_key = app.config['NEWS_API_KEY']
    country_based_headlines = app.config['COUTRY_BASED_HEADLINES']
    country_base_headlines_category = app.config['COUTRY_BASED_HEADLINES_CATEGORIES']
    source_headlines = app.config['TOP_HEADLINES_FROM_SOURCE']
    all_sources = app.config['GET_ALL_SOURCES']


def get_all_articles(url):
    with urllib.request.urlopen(url) as url:
        headline_data = url.read()
        headlines_response = json.loads(headline_data)

        headlines = []

        if headlines_response["articles"]:
           for item in list(headlines_response["articles"]):
               if item["source"] and item["source"] and item["author"] and item["title"] and item["description"] and item["url"] and item["urlToImage"] and item["publishedAt"]:
                    headlines.append(Article(item["source"]["name"], item["author"], item["title"], item["description"], item["url"], item["urlToImage"],item["publishedAt"]))

        
    return headlines


def get_headlines(country):
    headlines_url = country_based_headlines.format(country, api_key)
    return get_all_articles(headlines_url)                   


def get_source_headlines(source):
    headlines_url = source_headlines.format(source, api_key)
    return get_all_articles(headlines_url)


def get_category_headlines(courtry, category):
    headlines_url = country_base_headlines_category.format(courtry, category, api_key)
    return get_all_articles(headlines_url)


def get_sources():
    sources_url = all_sources.format(api_key)

    with urllib.request.urlopen(sources_url) as url:
        sources_data = url.read()
        sources_response = json.loads(sources_data)

        sources = []

        if sources_response["sources"]:
           for source in sources_response["sources"]:
               if source["id"] and source["name"] and source["url"]:
                   sources.append(Source(source["id"], source["name"], source["url"]))


        return sources
