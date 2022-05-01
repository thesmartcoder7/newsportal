from app import models
import urllib.request,json

Article = models.Article
Source = models.Source

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
