from flask import Flask,render_template,request
from step2 import result
app = Flask(__name__)
@app.route("/",methods=['POST','GET'])
def index():
  if request.method =='POST':
    if request.values['send']=='送出':
      return render_template('index.html',name=result+request.values['city']+request.values['percent'])
  return render_template('index.html',name="")
if __name__ == "__main__":
  app.run()