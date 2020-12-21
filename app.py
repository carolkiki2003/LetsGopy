from flask import Flask,render_template,request
# from step2 import searchMountain
# from step4 import searchArticle
import json

app = Flask(__name__)

# citys
with open('./citys.json',encoding="utf-8") as json_file:
  cityList=json.load(json_file)

# chance of rain
percentList=[]
for chance in range(0,110,10):
  percentList.append(chance)

@app.route("/",methods=['POST','GET'])
def index():
  if request.method =='POST':
    # mountain="馬望曾呂山"
    # articleList=searchArticle(mountain)
    # print(searchMountain(request.values['city'],request.values['percent']))
    return render_template('index.html',name='result',citys=cityList,percents=percentList,city=request.values['city'],percent=request.values['percent'])
  return render_template('index.html',name="",citys=cityList,percents=percentList)

if __name__ == "__main__":
  app.run(debug=True)