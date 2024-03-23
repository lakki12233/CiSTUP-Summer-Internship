import React, { useState } from 'react';
import './App.css';

const App = () => {
  const [image, setImage] = useState(null);
  const [processedImage, setProcessedImage] = useState(null);
  const [error, setError] = useState(null);

  const handleImageUpload = async (e) => {
    const file = e.target.files[0];
    console.log('Selected file:', file);
    if (file) {
      try {
        const formData = new FormData();
        formData.append('file', file);

        const response = await fetch('http://localhost:5000/upload', {
          method: 'POST',
          body: formData,
        });

        if (response.ok) {
          const data = await response.json();
          console.log('Upload successful:', data);
          setImage(URL.createObjectURL(file));
          setProcessedImage(data.processed_image); // Update processed image URL
          setError(null); // Clear any previous errors
        } else {
          const errorText = await response.text();
          console.error('Upload failed:', errorText);
          setError('Error uploading file: ' + errorText);
        }
      } catch (error) {
        console.error('Error uploading file:', error);
        setError('Error uploading file: ' + error.message);
      }
    }
  };

  return (
    <div className="App">
      <nav className="navbar">My Image Processor</nav>
      <div className="container">
        <div className="upload-section">
          <h2>Upload Image</h2>
          <input type="file" accept="image/*" onChange={handleImageUpload} />
          {image && <img src={image} alt="Uploaded" className="uploaded-image" />}
        </div>
        <div className="processed-image-section">
          <h2>Processed Image</h2>
          {processedImage ? (
            <img src={`http://localhost:5000/${processedImage}`} alt="Processed" className="processed-image" />
          ) : (
            <p>No processed image available</p>
          )}
        </div>
        {error && <p className="error-message">{error}</p>}
      </div>
    </div>
  );
};

export default App;
