from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename
from ChickenDiseaseClassification.pipeline.predict import PredictionPipeline

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)

class ClientApp:
    def __init__(self, filename):
        self.pipeline = PredictionPipeline(filename)

c1App = ClientApp(filename=None)

@app.route('/', methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')

@app.route('/train', methods=['GET','POST'])
@cross_origin()
def trainRoute():
    os.system("python main.py") # or dvc repro
    return "Training Completed Successfully!"

@app.route('/predict', methods=['POST'])
@cross_origin()
def predictRoute():
    # Check if the POST request has a file part
    if 'image' not in request.files:
        return jsonify({'error': 'No file part'})

    image_file = request.files['image']
    if image_file.filename == '':
        return jsonify({'error': 'No selected file'})

    # Save the uploaded image securely
    filename = secure_filename(image_file.filename)
    image_path = os.path.join(app.root_path, 'uploads', filename)
    image_file.save(image_path)

    # Predict using the uploaded image
    c1App = ClientApp(filename=image_path)  # Pass the filename to the ClientApp
    result = c1App.pipeline.predict()

    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True) # AWS & LocalHost
    # app.run(host='0.0.0.0', port=80, debug=True) # Azure
