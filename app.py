from os import environ
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

gplinkapi = environ.get('gplinkapi')
shrinkme = environ.get('shirnkmeapi')

@app.route("/")
def home():
    return render_template("main.html")

@app.route('/shrinkme',methods=['GET','POST'])
def id():
    w = request.args.get('url')
    base_url = f"https://shrinkme.io/api?api="+shrinkme+"&url="+(w)
    torrent_results = requests.get(url=base_url).json()
    data = torrent_results
    shturl = data['shortenedUrl']
    web = "https://gplinks.in/"
    return render_template("main.json",web=web,shturl=shturl,w=w)
    
@app.route('/gplink',methods=['GET','POST'])
def ids():
    w = request.args.get('url')
    base_url = f"https://gplinks.in/api?api="+gplinkapi+"&url="+(w)
    torrent_results = requests.get(url=base_url).json()
    data = torrent_results
    return data['shortenedUrl']


if __name__ == "__main__":
    app.run(host="0.0.0.0",port= 5000)
