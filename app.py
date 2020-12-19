from flask import Flask,render_template,request
from step2 import result

app = Flask(__name__)

@app.route("/",methods=['POST','GET'])
def index():
  if request.method =='POST':
    return render_template('index.html',name=result,city=request.values['city'],percent=request.values['percent'])
  return render_template('index.html',name="")

if __name__ == "__main__":
  app.run(debug=True)