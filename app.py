from flask import Flask,render_template,request
import requests
from bs4 import BeautifulSoup
app = Flask(__name__)
@app.route("/",methods=['POST','GET'])
def index():
  if request.method =='POST':
    if request.values['send']=='送出':
      re=requests.get('https://www.cwb.gov.tw/V8/C/L/Mountain/Mountain.html')
      soup = BeautifulSoup(re.text, 'html.parser')
      return render_template('index.html',name=soup.title.text+request.values['city'])
  return render_template('index.html',name="")
if __name__ == "__main__":
  app.run()