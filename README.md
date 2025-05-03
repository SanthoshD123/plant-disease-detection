# Plant Disease Detection

## 📋 Overview

This project is an AI-powered plant disease detection system that helps farmers and gardeners quickly identify common plant diseases. Using deep learning techniques, the system can analyze images of plant leaves and accurately diagnose various plant diseases affecting tomatoes, potatoes, and bell peppers.

## 🌱 Key Features

- **Real-time disease detection** from leaf images
- **High accuracy** classification using CNN architecture
- **User-friendly web interface** for easy interaction
- **Detailed predictions** with confidence scores
- **Support for multiple crops**: Tomato, Potato, and Bell Pepper
- **Detection of various diseases** including:
  - Bacterial Spot
  - Early Blight
  - Late Blight
  - Leaf Mold
  - Spider Mites
  - Septoria Leaf Spot
  - Yellow Leaf Curl Virus
  - Mosaic Virus
  - And identification of healthy plants

## 🔧 Technologies Used

- **Python** - Primary programming language
- **TensorFlow/Keras** - For creating and training the neural network
- **Flask** - Web framework for the application
- **HTML/CSS/JavaScript** - Front-end interface
- **Bootstrap** - For responsive UI components

## 📁 Project Structure

```
plant-disease-detection/
├── .idea/                      # IDE configuration files
├── archive/PlantVillage/       # Dataset directory
│   ├── Pepper_bell__Bacterial_spot/
│   ├── Pepper_bell__healthy/
│   ├── Potato__Early_blight/
│   ├── Potato__Late_blight/
│   ├── Potato__healthy/
│   ├── Tomato_Bacterial_spot/
│   ├── Tomato_Early_blight/
│   ├── Tomato_Late_blight/
│   ├── Tomato_Leaf_Mold/
│   ├── Tomato_Septoria_leaf_spot/
│   ├── Tomato_Spider_mites_Two_spotted_spider_mite/
│   ├── Tomato_Target_Spot/
│   ├── Tomato_Tomato_YellowLeaf_Curl_Virus/
│   ├── Tomato_Tomato_mosaic_virus/
│   └── Tomato_healthy/
├── static/                     # Static files (CSS, JS, uploads)
│   ├── uploads/                # For storing uploaded images
│   ├── script.js               # Frontend JavaScript
│   └── styles.css              # CSS styles
├── templates/                  # HTML templates
│   └── index.html              # Main page template
├── app.py                      # Flask application
├── main.py                     # Model training script
├── plant_disease_model.keras   # Trained model
└── README.md                   # Project documentation
```

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/SanthoshD123/plant-disease-detection.git
   cd plant-disease-detection
   ```

2. **Create a virtual environment and activate it**
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask application**
   ```bash
   python app.py
   ```

5. **Access the web interface**
   Open your browser and go to `http://127.0.0.1:5000/`

## 📊 Model Architecture

The plant disease detection model uses a Convolutional Neural Network (CNN) with the following architecture:

- Input layer accepting 100x100 RGB images
- Multiple convolutional layers with batch normalization and max pooling
- Dense layers with dropout for regularization
- Output layer with softmax activation for multi-class classification

The model was trained on the PlantVillage dataset with data augmentation techniques to improve generalization.

## 🖼️ Dataset

This project uses the PlantVillage dataset, which contains thousands of labeled images of healthy and diseased plant leaves across different species. The dataset includes multiple classes for various plant diseases and healthy samples.

## 📱 Usage

1. Open the web application in your browser
2. Click on the file input to upload an image of a plant leaf
3. Click the "Upload and Predict" button
4. Wait for the analysis to complete
5. View the prediction result and confidence score

## 🔄 Training Your Own Model

If you want to train the model on your own:

1. Organize your dataset in a similar structure to the PlantVillage dataset
2. Update the `base_dir` in `main.py` to point to your dataset
3. Run the training script:
   ```bash
   python main.py
   ```
4. The trained model will be saved as `plant_disease_model.keras`

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### 📸 Screenshots

#### Prediction Result
![Screenshot 2024-10-02 134924](https://github.com/user-attachments/assets/f2dfb970-7a1a-47bd-b079-10e1627dacca)

