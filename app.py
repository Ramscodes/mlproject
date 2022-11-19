from distutils.log import debug
from flask import Flask 
from housing.logger import logging
from housing.exception import HousingException
import sys

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    try:
        raise Exception("Raised exception for testing")
    except Exception as e:
        #raise HousingException(e,sys) from e
        housing = HousingException(e,sys)
        logging.info(housing.error_detail_message)
        logging.info("Testing the logging module")
    return "Hope!!!!..."

if __name__=="__main__":
    app.run(debug=True)

