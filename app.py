from distutils.log import debug
from flask import Flask 

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    return "lets start building the world with machine learning..."

if __name__=="__main__":
    app.run(debug=True)

