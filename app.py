from flask import Flask,render_template,request
from step1 import result
# from step2 import searchMountain
# from step4 import searchArticle
# import json

# citys
# with open('./citys.json',encoding="utf-8") as json_file:
#   cityList=json.load(json_file)
# cityList=["臺北市","新北市","桃園市","新竹市","新竹縣","苗栗縣","臺中市","南投縣","嘉義縣","高雄市","屏東縣","宜蘭縣","花蓮縣"]
# chance of rain
# percentList=[0,1,2]
# for chance in range(0,110,10):
#   percentList.append(chance)

app = Flask(__name__)

@app.route("/",methods=['POST','GET'])
def index():
  if request.method =='POST':
    # mountain="馬望曾呂山"
    # articleList=searchArticle(mountain)
    # print(searchMountain(request.values['city'],request.values['percent']))
    return render_template('index.html',name=result,city=request.values['city'],percent=request.values['percent'])
  return render_template('index.html',name="")

if __name__ == "__main__":
  app.run(debug=True)