#!/usr/bin/python3

from flask import Flask, render_template, request
import requests

app = Flask("docker_compose_application")

@app.route("/home")
def homepage():
    return render_template("home.html")


@app.route("/storeindb", methods=["GET"])
def api_call():
    uname = request.args.get("uname")
    lname = request.args.get("lname")
    #sending data to backecnd server
    req = requests.get(
            "http://backend:80/cgi-bin/mysql-save.py",
            params = [
                ('uname', uname),
                ('lname', lname)
            ])

    return req.text        
    

if __name__ == "__main__":
    app.run(host="0.0.0.0.", port=3499)

