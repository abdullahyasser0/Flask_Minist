from flask import Flask,render_template,request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
from io import BytesIO

app = Flask(__name__)
model = load_model('minist_model.keras')

@app.route('/')
def form():
    return render_template('upload.html')


@app.route('/predict',methods=['POST'])
def predict():
    image = request.files['photo']
    imagearr=image_array(image)
    predictions = model.predict(imagearr)

    predicted_class = np.argmax(predictions, axis=1)

    return render_template('upload.html', prediction=predicted_class)


def image_array(image):
    image = load_img(BytesIO(image.read()), target_size=(28, 28), color_mode="grayscale")  
    image_array = img_to_array(image)  
    image_array = np.expand_dims(image_array, axis=0) 
    image_array = image_array / 255.0  

    return image_array



if __name__== '__main__':
    app.run()