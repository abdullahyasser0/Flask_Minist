from flask import Flask, render_template, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array,load_img
import numpy as np
from PIL import Image
import base64
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


@app.route('/predict-drawing', methods=['POST'])
def predict_drawing():
    data = request.json
    if 'image' not in data:
        return jsonify({'error': 'No image provided'}), 400

    image_data = data['image'].split(',')[1]
    image = Image.open(BytesIO(base64.b64decode(image_data))).convert('L')  
    image = image.resize((28, 28))  

    image_array = img_to_array(image) / 255.0
    image_array = np.expand_dims(image_array, axis=0)

    predictions = model.predict(image_array)
    predicted_class = np.argmax(predictions, axis=1)[0]

    return jsonify({'prediction': str(predicted_class)})

def image_array(image):
    image = load_img(BytesIO(image.read()), target_size=(28, 28), color_mode="grayscale")  
    image_array = img_to_array(image)  
    image_array = np.expand_dims(image_array, axis=0) 
    image_array = image_array / 255.0  

    return image_array



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)