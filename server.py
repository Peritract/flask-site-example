"""Small example of Flask template stuff"""

from os import environ as env
import json

from dotenv import load_dotenv
from flask import Flask, send_file, render_template, redirect, request


app = Flask(__name__)


@app.get("/")
def returns_templated_html():

    url_links = [
        {"display": "Passive Loathing",
         "url": "http://www.lel.ed.ac.uk/~gpullum/passive_loathing.html"},
        {"display": "Don't make fun of renowned author Dan Brown",
         "url": "https://www.telegraph.co.uk/books/authors/dont-make-fun-of-renowned-dan-brown/"},
        {"display": "The Meteor Generation",
         "url": "https://eveninguniverse.com/fiction/the-meteor-generation.html",
         "author": "Heather Flowers"},
    ]  # What if these were loaded from a database of some kind? What then?

    # All variables passed in can be used in the template
    return render_template("index.html", heading="Home", links=url_links)


@app.get("/about")
def returns_static_page():
    return send_file("pages/about.html")


@app.route("/signpost")
def sends_you_elsewhere():
    return redirect("/about")


@app.get("/page/<topic>")
def dynamic_page(topic): # Another dynamic one!
    return render_template("page.html", topic=topic)


@app.route("/suggest", methods=["GET", "POST"])
def page_which_lets_you_submit_a_form_and_then_sends_you_elsewhere():

    if request.method == "GET":  # If you want to see the form
        return send_file("pages/submit.html")
    else:  # If the form has been submitted (POST)

        # Pull the data from the form
        topic = request.form.get("topic")

        # Redirect to a dynamic page!
        return redirect(f"/page/{topic}")

if __name__ == "__main__":

    load_dotenv()

    app.run(port=env["PORT"], debug=bool(int(env["DEBUG"])))
