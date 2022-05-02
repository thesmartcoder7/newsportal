from flask import render_template
from . import main
from ..requests import get_category_headlines, get_headlines, get_source_headlines, get_sources


@main.route("/")
def home():
    overall = get_headlines("us")
    finance = get_category_headlines("us", "business")
    entertainment = get_category_headlines("us", "entertainment")
    technology = get_category_headlines("us", "technology")
    sports = get_category_headlines("us", "sports")
    sources = get_sources()
    data = [overall, finance, entertainment, sources, technology, sports]

    return render_template("index.html", data =  data)


# this is a simplet test route in case of a server overload
# @main.route("/")
# def home():
#     return render_template("test.html")


@main.route("/source/<title>")
def category(title):
    headlines = get_source_headlines(title)

    return render_template("category.html", headlines = headlines,  title = title)