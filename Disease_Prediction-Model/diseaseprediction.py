from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import os

class DiseasePredictor:
    def __init__(self):
        self.model = None
        self.symptoms = []
        self.symptom_dict = {}
        self.load_and_train()
    
    def load_and_train(self):
        """Load data and train the model"""
        try:
            # Load training data
            data = pd.read_csv(os.path.join("data", "Training.csv"))
            df = pd.DataFrame(data)
            
            # Prepare features and target
            self.symptoms = df.columns.values[:-1]  # All columns except 'prognosis'
            X = df[self.symptoms]
            y = df['prognosis']
            
            # Create symptom to index mapping
            self.symptom_dict = dict(zip(self.symptoms, range(len(self.symptoms))))
            
            # Split data
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.3, random_state=42
            )
            
            # Train Decision Tree model
            self.model = DecisionTreeClassifier(random_state=42)
            self.model.fit(X_train, y_train)
            
            print(f"Model trained successfully!")
            print(f"Training accuracy: {self.model.score(X_train, y_train):.2f}")
            print(f"Testing accuracy: {self.model.score(X_test, y_test):.2f}")
            
        except Exception as e:
            print(f"Error loading/training model: {e}")
    
    def predict_disease(self, selected_symptoms):
        """Predict disease based on selected symptoms"""
        if not self.model:
            return "Model not trained"
        
        # Create input vector
        input_vector = [0] * len(self.symptoms)
        
        # Set 1 for selected symptoms
        for symptom in selected_symptoms:
            if symptom in self.symptom_dict:
                index = self.symptom_dict[symptom]
                input_vector[index] = 1
        
        # Reshape for prediction
        input_vector = np.array(input_vector).reshape(1, -1)
        
        # Make prediction
        prediction = self.model.predict(input_vector)
        return prediction[0]
    
    def get_all_symptoms(self):
        """Get list of all available symptoms"""
        return list(self.symptoms)

# Global predictor instance
predictor = DiseasePredictor()

def predict_disease_from_symptoms(symptoms_list):
    """Main function to predict disease"""
    return predictor.predict_disease(symptoms_list)

def get_all_symptoms():
    """Get all available symptoms"""
    return predictor.get_all_symptoms()
