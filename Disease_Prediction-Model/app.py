from flask import Flask, render_template, request, jsonify
import diseaseprediction
import csv
import os

app = Flask(__name__)

# Load symptoms from Testing.csv
def load_symptoms():
    """Load symptoms from Testing.csv file"""
    symptoms = []
    try:
        with open(os.path.join('data', 'Testing.csv'), 'r') as file:
            reader = csv.reader(file)
            header = next(reader)
            symptoms = header[:-1]  # Exclude 'prognosis' column
    except FileNotFoundError:
        # Fallback: get symptoms from ML module
        symptoms = diseaseprediction.get_all_symptoms()
    
    return symptoms

# Load symptoms at startup
SYMPTOMS = load_symptoms()

@app.route('/')
def home():
    """Home page with symptom selection"""
    return render_template('includes/default.html', symptoms=SYMPTOMS)

@app.route('/predict', methods=['POST'])
def predict_disease():
    """Predict disease based on selected symptoms"""
    try:
        # Get selected symptoms from form
        selected_symptoms = []
        
        for i in range(1, 6):  # Support up to 5 symptoms
            symptom = request.form.get(f'Symptom{i}')
            if symptom and symptom != "" and symptom not in selected_symptoms:
                selected_symptoms.append(symptom)
        
        if not selected_symptoms:
            return render_template('disease_predict.html', 
                                 error="Please select at least one symptom",
                                 symptoms=SYMPTOMS)
        
        # Predict disease
        predicted_disease = diseaseprediction.predict_disease_from_symptoms(selected_symptoms)
        
        return render_template('disease_predict.html',
                             disease=predicted_disease,
                             selected_symptoms=selected_symptoms,
                             symptoms=SYMPTOMS)
    
    except Exception as e:
        return render_template('disease_predict.html',
                             error=f"Prediction error: {str(e)}",
                             symptoms=SYMPTOMS)

@app.route('/find_doctor', methods=['POST'])
def find_doctor():
    """Find doctor page"""
    location = request.form.get('location', '')
    disease = request.form.get('disease', '')
    
    return render_template('find_doctor.html',
                         location=location,
                         disease=disease,
                         symptoms=SYMPTOMS)

@app.route('/api/symptoms')
def api_symptoms():
    """API endpoint to get all symptoms"""
    return jsonify(SYMPTOMS)

@app.route('/api/predict', methods=['POST'])
def api_predict():
    """API endpoint for disease prediction"""
    try:
        data = request.get_json()
        symptoms = data.get('symptoms', [])
        
        if not symptoms:
            return jsonify({'error': 'No symptoms provided'}), 400
        
        prediction = diseaseprediction.predict_disease_from_symptoms(symptoms)
        
        return jsonify({
            'prediction': prediction,
            'symptoms': symptoms
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("Starting Disease Prediction System...")
    print(f"Loaded {len(SYMPTOMS)} symptoms")
    app.run(debug=True, host='0.0.0.0', port=8000)
