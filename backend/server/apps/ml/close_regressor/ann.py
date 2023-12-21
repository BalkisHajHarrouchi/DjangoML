import joblib
import pandas as pd
import numpy as np
from sklearn.neural_network import MLPRegressor

class ANNRegressor:
    def __init__(self):
        path_to_artifacts = "C:/Users/MSI/Desktop/DjangoML/research/"
        self.scaler = joblib.load(path_to_artifacts + "scaler.joblib")
        self.ann_regressor = joblib.load(path_to_artifacts + "ann_regressor.joblib")

    def preprocessing(self, input_data):
        input_df = pd.DataFrame([input_data])
        input_scaled = self.scaler.transform(input_df)
        return input_scaled

    def predict(self, input_data):
        return self.ann_regressor.predict(input_data)

    def postprocessing(self, input_data):
        try:
            # Your existing postprocessing logic
            # ...
            return {"prediction": input_data[0], "status": "OK"}
        except Exception as e:
            return {"status": "Error", "message": str(e)}

    def compute_prediction(self, input_data):
        try:
            input_scaled = self.preprocessing(input_data)
            prediction = self.predict(input_scaled)
            prediction = self.postprocessing(prediction)
        except Exception as e:
            return {"status": "Error", "message": str(e)}

        return prediction
