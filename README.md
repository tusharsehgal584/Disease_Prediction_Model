# Disease_Prediction_Model
This web-based Disease Prediction System uses machine learning to predict diseases from user-selected symptoms. Built with Python, Flask, and scikit-learn, it provides a simple interface for users to select symptoms and receive a prediction. It also helps users find doctors for their predicted condition.

Features
Symptom-based Prediction: Select up to 5 symptoms and get a disease prediction.

Machine Learning Model: Decision Tree Classifier trained on a medical dataset.

User-Friendly Web Interface: Built with Flask and HTML templates.

Doctor Finder: Integrated Google search for nearby doctors.

Easily Extensible: Add more symptoms or diseases by updating the dataset.

Project Structure
text
Disease-Prediction-system-using-Machine-Learning-and-Flask/
│
├── templates/
│   ├── includes/
│   │   └── default.html
│   ├── disease_predict.html
│   ├── find_doctor.html
│   ├── home.html
│
├── bg.jpg
├── logo.png
├── Testing.csv
├── Training.csv
├── app.py
├── diseaseprediction.py
├── README.md
└── ...
Getting Started
Prerequisites
Python 3.6 or above

pip (Python package installer)

Installation
Clone the repository:

bash
git clone https://github.com/tusharsehgal584/Disease-Prediction-system-using-Machine-Learning-and-Flask.git
cd Disease-Prediction-system-using-Machine-Learning-and-Flask
Install dependencies:

bash
pip install flask scikit-learn pandas numpy
Run the application:

bash
python app.py
The app will be available at http://127.0.0.1:8000.

Usage
Open your browser and go to http://127.0.0.1:8000.

Select up to 5 symptoms from the dropdown menus.

Click "Predict Disease" to see the prediction.

Use the "Find Doctor" feature to search for nearby doctors related to the prediction.

Dataset
Training.csv: Used to train the machine learning model.

Testing.csv: Used for extracting the list of symptoms and for model testing.

Model
Algorithm: Decision Tree Classifier (scikit-learn)

Training: The model trains automatically on app startup using Training.csv.

Contributing
Contributions are welcome! Please open an issue or submit a pull request for improvements or bug fixes.

License
This project is open source and available under the MIT License.

Author
Tushar Sehgal

Student at Amity University, Greater Noida
