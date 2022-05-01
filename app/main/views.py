from flask import render_template
from . import main
from ..requests import get_category_headlines, get_headlines, get_source_headlines, get_sources


@main.route("/")
def home():
    overall = get_headlines("us")
    finance = get_category_headlines("us", "finance")
    entertainment = get_category_headlines("us", "entertainment")
    sources = get_sources()
    data = [overall, finance, entertainment, sources]

    return render_template("index.html", data =  data)