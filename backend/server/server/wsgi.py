
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')

application = get_wsgi_application()
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')
application = get_wsgi_application()

# ML registry
import inspect
from apps.ml.registry import MLRegistry
from apps.ml.close_regressor.ann import ANNRegressor  # Adjust the import based on your actual implementation

try:
    registry = MLRegistry()  # create ML registry

    # ANN model
    ann = ANNRegressor()  # Adjust the class name based on your actual implementation

    # add to ML registry
    registry.add_algorithm(endpoint_name="close_regressor",
                            algorithm_object=ann,
                            algorithm_name="ann_model",
                            algorithm_status="production",
                            algorithm_version="0.0.1",
                            owner="Haj Harrouchi Balkis & Laroussi Nourchene",
                            algorithm_description="Your ANN algorithm description",
                            algorithm_code=inspect.getsource(ANNRegressor))

except Exception as e:
    print("Exception while loading the algorithms to the registry:", str(e))
