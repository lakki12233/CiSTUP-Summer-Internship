# CiSTUP-Summer-Internship
## Vehicle Detection Web Application

This web application allows users to upload images for vehicle detection and counting using a pre-trained Haar Cascade classifier model. Below are the instructions for setting up, running, and testing the application locally.

### Installation Instructions

1. Clone the repository to your local machine:

   ```
   git clone https://github.com/your-username/vehicle-detection-web-app.git
   ```

2. Navigate to the project directory:

   ```
   cd vehicle-detection-web-app
   ```

3. Install the required Python packages using pip:

   ```
   pip install -r requirements.txt
   ```

### Running the Application

1. Start the Flask backend server:

   ```
   python app.py
   ```

2. The backend server should start running at `http://localhost:5000`.

3. Open a new terminal window and navigate to the frontend directory:

   ```
   cd frontend
   ```

4. Install the frontend dependencies:

   ```
   npm install
   ```

5. Start the React development server:

   ```
   npm start
   ```

6. The frontend server should start running at `http://localhost:3000`.

### Testing the Application

1. Open your web browser and go to `http://localhost:3000`.

2. You will see the web application interface with options to upload an image and view the processed image.

3. Click on the "Choose File" button and select an image file (e.g., JPEG, PNG) containing vehicles.

4. Click on the "Upload" button to initiate vehicle detection and counting.

5. Wait for the processing to complete. The processed image with bounding boxes around detected vehicles will be displayed, along with the vehicle count.

6. If there are any errors during the upload or processing, an error message will be shown on the screen.

### Dependencies

- Python 3.x
- Flask
- Flask-Cors
- OpenCV (cv2)
- Node.js
- React

### Additional Notes

- Ensure that both the frontend and backend servers are running simultaneously for the application to work correctly.
- The Haar Cascade model for vehicle detection is included in the `modules` directory (`haarcascade_car.xml`).
- Uploaded files are temporarily saved in the `uploads` directory and deleted after processing.
- Debug mode is enabled in the Flask backend (`app.run(debug=True)`) for development purposes. Change it to `app.run(debug=False)` for production deployment.

Feel free to reach out for any further assistance or issues related to the application. Happy vehicle detection! 🚗🔍
