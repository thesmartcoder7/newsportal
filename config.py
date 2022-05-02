import os

class Config:
    GLOBAL_SEARCH ='https://newsapi.org/v2/everything?q={}&apiKey={}'
    COUTRY_BASED_HEADLINES =  "https://newsapi.org/v2/top-headlines?country={}&apiKey={}"
    COUTRY_BASED_HEADLINES_CATEGORIES = "https://newsapi.org/v2/top-headlines?country={}&category={}&apiKey={}"
    TOP_HEADLINES_FROM_SOURCE = "https://newsapi.org/v2/top-headlines?sources={}&apiKey={}"
    GET_ALL_SOURCES = "https://newsapi.org/v2/top-headlines/sources?country=us&&language=en&apiKey={}"


    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}

