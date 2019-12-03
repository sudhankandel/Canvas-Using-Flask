from flask import Flask,render_template,request
import re
import cv2
import base64
from PIL import Image
import io
import numpy as np
import matplotlib.pyplot as plt
import warnings
import matplotlib.pyplot as plt

app = Flask(__name__)
@app.route('/')
def index():
	return render_template("index.html")



@app.route('/predict/',methods=['GET','POST'])
def predict():
    imgData = request.get_data()
    print(imgData)
    imgData=str((imgData), 'utf-8')
    print(imgData)
    imgstr = re.search(r'base64,(.*)',imgData).group(1)
    print(imgstr)
    with open('output.png','wb') as output:
        output.write(np.fromstring(base64.b64decode(imgstr), np.uint8))
    return None
if __name__ == "__main__":
    app.run(debug=True)

