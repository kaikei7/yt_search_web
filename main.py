"""from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello, World! bangke</br>bangke'
@app.route('/<name>')  
def hello_name(name):
   return 'Hello %s!' % name
app.run(host='0.0.0.0', port=8080)"""
from bs4 import BeautifulSoup
import requests

def weather(city):
  
                city = city.replace(" ", "+")
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',"Accept-Language": "id-ID,id;q=0.5",  'referer':'https://www.google.com/'}
                res = requests.get(f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
                soup = BeautifulSoup(res.text, 'html.parser')
                location = soup.select('#wob_loc')[0].getText().strip()
                time = soup.select('#wob_dts')[0].getText().strip()
                info = soup.select('#wob_dc')[0].getText().strip()
                weather = soup.select('#wob_tm')[0].getText().strip()
                temp = (int(weather)-32)*(5/9)
                result = f"{location}\n{time}\n{info}\n{int(temp)}°C"
                return result

from youtubesearchpython import VideosSearch
def searvid(que):
  try:
    query = que
    videosSearch = VideosSearch(query)
    ls = []
    tries = 0
    for x in videosSearch.result()["result"]:
      tries += 1
      title = x["title"]
      link = x["link"]
      duration = x["duration"]
      views = x["viewCount"]["text"]
      channel = x["channel"]["name"]
      pub = x["publishedTime"]
      ls.append(f"#{tries}</br>* {title} : {link}</br>* Duration : {duration}</br>* Views : {views}</br>* Channel : {channel}</br>* Pulished time : {pub}</br>")
    rst = "</br>".join(ls)
    return rst
  except Exception as e:
    return e
    
from flask import Flask, render_template, request, make_response
from threading import Thread

app = Flask(__name__)
@app.route('/')
def index():
   return render_template('index.html')

@app.route('/search', methods = ['POST', 'GET'])
def search ():
   if request.method == 'POST':
      user = request.form['nm']
     
   return searvid(user)
  
def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()
keep_alive()