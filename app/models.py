class Article:
    def __init__(self, source_name, author, title, description, url, image, date, content):
        self.source_name = source_name
        self.author = author 
        self.title = title
        self.description = description
        self.url = url
        self.image = image 
        self.date = date
        self.content = content


class Source:
    def __init__(self, id, name, url):
        self.id = id
        self.name = name
        self.url = url

