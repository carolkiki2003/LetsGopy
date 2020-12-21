from flask import Flask,render_template,request
from step1 import result

cityList=["臺北市","新北市","桃園市","新竹市","新竹縣","苗栗縣","臺中市","南投縣","嘉義縣","高雄市","屏東縣","宜蘭縣","花蓮縣"]

# chance of rain
percentList=[]
for chance in range(0,110,10):
  percentList.append(chance)

app = Flask(__name__)

@app.route("/",methods=['POST','GET'])
def index():
  if request.method =='POST':
    return render_template('index.html',name=result,citys=cityList,percents=percentList,city=request.values['city'],percent=request.values['percent'])
  return render_template('index.html',name="",citys=cityList,percents=percentList)

if __name__ == "__main__":
  app.run(debug=True)