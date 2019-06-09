from flask import Flask, request, render_template
import os
import numpy as np
import pickle
import cv2
import json

app = Flask(__name__)
with open('C:/Users/win7/Desktop/hack/hack.json') as f:
    data = json.load(f)
videosrc='C:/Users/win7/Desktop/hack/video1.mp4'
@app.route('/')
def my_form():
	return render_template('123.html',data=data)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)