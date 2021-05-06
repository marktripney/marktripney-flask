from markdown import markdown
from flask import Flask, render_template, render_template_string, url_for
from flask_flatpages import FlatPages


# Customise render, incorporating fenced code block formatting. For details:
# https://flask-flatpages.readthedocs.io/en/v0.7.2/index.html#using-custom-html-renderers
def renderer(text):
    pre_rendered_body = render_template_string(text)
    return markdown(pre_rendered_body, extensions=["fenced_code"])


FLATPAGES_AUTO_RELOAD = True
FLATPAGES_EXTENSION = ".md"

app = Flask(__name__)
app.config.from_object(__name__)
app.config["FLATPAGES_HTML_RENDERER"] = renderer
pages = FlatPages(app)


@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html", title="Home")


@app.route("/writing/<path:path>.html")
def page(path):
    page = pages.get_or_404(path)
    return render_template("page.html", title="Writing", page=page)


@app.route("/work")
def work():
    return render_template("work.html", title="Work")


@app.route("/writing")
def writing():
    return render_template("writing.html", title="Writing", pages=pages)


@app.route("/contact")
def contact():
    return render_template("contact.html", title="Contact")
