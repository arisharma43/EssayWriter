from flask import Flask, redirect, render_template, request, send_from_directory
import open_ai
import constants
from bs4 import BeautifulSoup
import os.path
import openai

app = Flask(__name__, static_url_path="")

print("flask works")


@app.route("/output/<path:path>")
def send_output(path):
    return send_from_directory("output", path)


@app.route("/", methods=["GET", "POST"])
def root():
    api_response = ""
    result = ""
    if request.method == "POST":
        user_input = request.form.get("user_input")
        prompt = user_input
        api_response = open_ai.openai_request(user_input)

        result = prompt + api_response
        with open("output/output.txt", "w+") as file:
            file.write(api_response)

    return render_template("index.html", api_response=result)
