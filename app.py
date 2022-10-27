from distutils.log import debug
from flask import Flask 

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    return "lets start living life without worries # NO_REGRETS , # NO_WORRIES..."

if __name__=="__main__":
    app.run(debug=True)

