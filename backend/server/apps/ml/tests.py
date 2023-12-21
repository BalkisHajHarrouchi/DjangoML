# File: apps/ml/tests.py

from django.test import TestCase
from apps.ml.close_regressor.ann import ANNRegressor 
import inspect
from apps.ml.registry import MLRegistry


class MLTests(TestCase):
    def test_ann_algorithm(self):
        input_data = {
            "High": 0.5,
            "Low": 0.3,
            "Open_Price": 0.7,
            "Adj_Close": 0.6,
            "Volume": 0.8
            # Add other input features as needed for your ANN model
        }

        my_ann = ANNRegressor()  # Adjust the class name to match your actual implementation
        response = my_ann.compute_prediction(input_data)

        # Check for 'status' key in response
        self.assertTrue('status' in response)

        # Check if the 'status' is 'OK'
        self.assertEqual('OK', response['status'])

        # Check for 'prediction' key in response
        self.assertTrue('prediction' in response)

        # You can add more assertions based on your expected outcomes
  # Adjust the import based on your actual implementation
    def test_registry(self):
        registry = MLRegistry()
        self.assertEqual(len(registry.endpoints), 0)
        endpoint_name = "close_regressor"
        algorithm_object = ANNRegressor()  # Adjust the class name based on your actual implementation
        algorithm_name = "ann_model"
        algorithm_status = "production"
        algorithm_version = "0.0.1"
        algorithm_owner = "Haj Harrouchi Balkis & Laroussi Nourchene"
        algorithm_description = "Your algorithm description"  # Replace with the actual description
        algorithm_code = inspect.getsource(ANNRegressor)  # Adjust based on your actual implementation
        # Add to registry
        registry.add_algorithm(endpoint_name, algorithm_object, algorithm_name,
                               algorithm_status, algorithm_version, algorithm_owner,
                               algorithm_description, algorithm_code)
        # There should be one endpoint available
        self.assertEqual(len(registry.endpoints), 1)

    
