"""
Basic ML pipeline placeholder.

Objective:
Demonstrate how ML workflows can integrate with cloud automation
and infrastructure-as-code principles.
"""

def preprocess_data(data):
    # Placeholder preprocessing logic
    return data

def train_model(data):
    # Placeholder training logic
    model = "trained_model_object"
    return model

def deploy_model(model):
    # Future integration with cloud deployment (AWS/Azure/GCP)
    print("Model ready for deployment pipeline")

if __name__ == "__main__":
    sample_data = [1, 2, 3]
    processed = preprocess_data(sample_data)
    model = train_model(processed)
    deploy_model(model)
