from flask import Flask, request, jsonify, render_template
from PIL import Image
import io
import numpy as np
import tensorflow as tf  # If using TensorFlow/Keras

app = Flask(__name__)

# Load your ML model (e.g., TensorFlow/Keras)
# Replace 'model/model.h5' with your model's file path
model = tf.keras.models.load_model('model/model.h5')

def prepare_image(image, target_size=(224, 224)):
    # Resize the image to the target size and preprocess it
    image = image.resize(target_size)
    image = np.array(image)
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    image = image / 255.0  # Normalize the image
    return image

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['image']
    image = Image.open(io.BytesIO(file.read()))

    # Prepare the image for the model
    prepared_image = prepare_image(image)

    # Make a prediction using the ML model
    predictions = model.predict(prepared_image)
    predicted_class = np.argmax(predictions, axis=1)[0]

    # Example: Assuming your model is a classifier and returns a class label
    # Replace this with actual class names from your model
    classes = ['class1', 'class2', 'class3']  # Replace with your actual classes
    prediction = classes[predicted_class]

    return jsonify({"prediction": prediction})

if __name__ == '__main__':
    app.run(debug=True)
