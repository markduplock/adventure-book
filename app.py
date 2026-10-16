from flask import Flask, render_template

app = Flask(import_name=__name__)


@app.route(rule="/")
def index() -> str:
    return render_template(template_name_or_list="index.html")
