### README: Simple Model Deployment with Flask

---

#### Project Overview

This project demonstrates a straightforward deployment of a machine learning model using Flask. The model accepts both drawings and photos for prediction. Users can interact with the application via an intuitive web interface, preview uploaded images, and receive real-time predictions. This project is a practical example of serving machine learning models in a web environment.

---

#### Features

- **Drawing Canvas**: Users can draw directly on the canvas, and the model predicts the drawn input.
- **Image Upload**: Users can upload a photo for prediction.
- **Image Preview**: Users can preview the uploaded image before submitting it.
- **Real-Time Predictions**: Predictions for both drawings and photos are displayed instantly.
- **Responsive Design**: Fully functional on desktop and mobile devices, including touch input.

---

#### Prerequisites

Before running the project, ensure you have the following installed:

- **Python 3.10+**
- **Docker**: For containerized deployment (optional).
- **Flask**: For the web application framework.
- **TensorFlow/Keras**: To load and run the machine learning model.
- **Gunicorn** (optional): For deploying in a production environment.

---

#### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/simple-model-deployment.git
   cd simple-model-deployment
   ```

2. **Set Up a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Prepare the Model**:
   Place your pre-trained model file (`minist_model.keras`) in the root directory.

5. **Directory Structure**:
   Ensure your project directory has the following structure:
   ```
   project/
   ├── main.py
   ├── requirements.txt
   ├── templates/
   │   └── upload.html
   ├── static/
   │   └── mycss.css
   ├── minist_model.keras
   ├── Dockerfile
   ```

---

#### Using Docker

1. **Build the Docker Image**:
   Ensure Docker is installed and running, then build the Docker image:
   ```bash
   docker build -t flask-mnist-app .
   ```

2. **Run the Docker Container**:
   Start a container from the built image:
   ```bash
   docker run -p 5000:5000 flask-mnist-app
   ```

3. **Access the Application**:
   Open a browser and navigate to:
   ```
   http://localhost:5000
   ```

---

#### Dockerfile

Here’s the `Dockerfile` used to containerize the application:
```dockerfile
# Use a Python base image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy project files into the container
COPY . .

# Install required system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    zlib1g-dev \
    libjpeg-dev \
    libpng-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN python -m venv /opt/venv && \
    . /opt/venv/bin/activate && \
    pip install --no-cache-dir -r requirements.txt

# Expose Flask's default port
EXPOSE 5000

# Use Gunicorn to serve the Flask application
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "main:app"]
```

---

#### Running the Application

1. **Start the Flask Server**:
   ```bash
   python main.py
   ```

2. **Access the Application**:
   Open your browser and go to:
   ```
   http://127.0.0.1:5000/
   ```

3. **Production Deployment**:
   Use Gunicorn or Docker to serve the app in a production-ready environment.

---

#### How to Use

1. **Drawing Input**:
   - Use the canvas to draw a number or object.
   - Click **Predict** to send the drawing for prediction.

2. **Image Upload**:
   - Upload a photo using the file input field.
   - Preview the image on the screen.
   - Click **Upload Photo** to get the prediction.

3. **View Predictions**:
   - The predicted class is displayed instantly on the page.

---

#### Key Files

- **`main.py`**: The Flask backend that handles image uploads, drawing input, and predictions.
- **`templates/upload.html`**: The frontend HTML file for the user interface.
- **`static/mycss.css`**: The CSS file for styling the interface.
- **`minist_model.keras`**: The pre-trained model used for predictions.
- **`Dockerfile`**: The Docker configuration for containerization.

---

#### Example Output

1. **Draw or upload a number or object.**
2. **The application processes the input and returns the result:**
   ```
   Predicted Class: 7
   ```

---

#### Customization

- **Model**: Replace `minist_model.keras` with your own trained model.
- **Classes**: Update the `labels` array in `main.py` to match your model's output classes.
- **Styling**: Edit `mycss.css` or HTML templates to customize the look and feel.

---

#### License

This project is licensed under the MIT License. Feel free to modify and use it for your projects.

---

#### Author

**Abdullah Yasser**  
📧 Email: [AbdullahYasser2506@gmail.com](mailto:AbdullahYasser2506@gmail.com)  
