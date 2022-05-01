from flask import render_template
from . import main
from ..requests import get_category_headlines, get_headlines, get_source_headlines, get_sources


@main.route("/")
def home():
    all_headlines = get_headlines("us")
    print(all_headlines)
    return render_template("index.html")