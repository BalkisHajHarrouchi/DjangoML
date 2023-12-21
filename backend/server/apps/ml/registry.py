from ..endpoints.models import Endpoint
from ..endpoints.models import MLAlgorithm
from ..endpoints.models import MLAlgorithmStatus
from ..endpoints.models import ANNModel  # Adjust the import statement
from ..endpoints.models import ANNModelStatus  # Adjust the import statement

class MLRegistry:
    def __init__(self):
        self.endpoints = {}

    def add_algorithm(self, endpoint_name, algorithm_object, algorithm_name,
                      algorithm_status, algorithm_version, owner,
                      algorithm_description, algorithm_code):
        # get or create endpoint
        endpoint, _ = Endpoint.objects.get_or_create(name=endpoint_name, owner=owner)

        # get or create algorithm
        algorithm_instance, algorithm_created = MLAlgorithm.objects.get_or_create(
            name=algorithm_name,
            description=algorithm_description,
            code=algorithm_code,
            version=algorithm_version,
            owner=owner,
            parent_endpoint=endpoint
        )
        if algorithm_created:
            status = MLAlgorithmStatus(status=algorithm_status,
                                       created_by=owner,
                                       parent_mlalgorithm=algorithm_instance,
                                       active=True)
            status.save()

        # add to registry
        self.endpoints[algorithm_instance.id] = algorithm_object

    def add_ann_algorithm(self, endpoint_name, ann_object, ann_name,
                          ann_status, ann_version, owner,
                          ann_description, ann_code, hidden_layer_sizes):
        # get or create endpoint
        endpoint, _ = Endpoint.objects.get_or_create(name=endpoint_name, owner=owner)

        # get or create ANN
        ann_instance, ann_created = ANNModel.objects.get_or_create(
            name=ann_name,
            description=ann_description,
            code=ann_code,
            version=ann_version,
            owner=owner,
            hidden_layer_sizes=hidden_layer_sizes,
            parent_endpoint=endpoint
        )
        if ann_created:
            status = ANNModelStatus(status=ann_status,
                                    created_by=owner,
                                    parent_annmodel=ann_instance,
                                    active=True)
            status.save()

        # add to registry
        self.endpoints[ann_instance.id] = ann_object
