from flask import Flask, request, jsonify
from flask_cors import CORS
import cv2
import os

app = Flask(__name__)
CORS(app, origins='http://localhost:3000')

# Define the path to the pre-trained vehicle detection model
model_path = 'modules/haarcascade_car.xml'

def detect_and_count_vehicles(image_path):
    image = cv2.imread(image_path)
    if image is None:
        return {'error': 'No vehicles detected'}

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Load the pre-trained vehicle detection cascade classifier
    car_cascade = cv2.CascadeClassifier(model_path)

    # Detect vehicles in the image
    vehicles = car_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw bounding boxes around detected vehicles
    for (x, y, w, h) in vehicles:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Count the number of vehicles detected
    vehicle_count = len(vehicles)

    # Save the output image with bounding boxes 
    cv2.imwrite('output.jpg', image)

    return {'message': 'Vehicle detection successful', 'vehicle_count': vehicle_count, 'processed_image': 'output.jpg'}

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    
    file_path = os.path.join('uploads', file.filename)
    file.save(file_path)

    # Perform object detection and counting
    result = detect_and_count_vehicles(file_path)

    # Delete the temporary uploaded file
    os.remove(file_path)

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
