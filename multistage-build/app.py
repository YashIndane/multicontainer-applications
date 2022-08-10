#!/usr/bin/python3

from flask import Flask, render_template, request
from keras.models import load_model
from keras.preprocessing import image
from base64 import b64decode
from PIL import Image
from io import BytesIO
import numpy as np

app = Flask("cat-dog-detection")

#The homepage
@app.route("/input")
def input():
    return render_template("input.html")


#CNN detection
@app.route("/predict", methods=["GET"])
def detect():

     uri_string = request.args.get("ur")
     uri_string = uri_string[uri_string.index(",") + 1:]
     im = Image.open(BytesIO(b64decode(uri_string)))
     im.save("input.png", 'PNG')

     #Loading the image
     test_image = image.load_img("input.png", target_size=(64, 64))
     test_image = image.img_to_array(test_image)
     test_image = np.expand_dims(test_image, axis=0)
     
     #Prediction
     result = model.predict(test_image)

     return "Dog" if result[0][0] == 1 else "Cat"


if __name__ == "__main__":
    model = load_model("cat-dog-final.h5")
    app.run(host="0.0.0.0", port=1556)
