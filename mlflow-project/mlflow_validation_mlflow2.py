from mlflow.models import validate_serving_input

model_uri = 'runs:/65928f0f02084877a3a8e0a304aaaae1/linear_regression_model_on_random_data'

# The logged model does not contain an input_example.
# Manually generate a serving payload to verify your model prior to deployment.
from mlflow.models import convert_input_example_to_serving_input

# Define INPUT_EXAMPLE via assignment with your own input example to the model
# A valid input example is a data instance suitable for pyfunc prediction

#added the blow line - by ram
INPUT_EXAMPLE=[[5]]
serving_payload = convert_input_example_to_serving_input(INPUT_EXAMPLE)

# Validate the serving payload works on the model
#validate_serving_input(model_uri, serving_payload)
print(validate_serving_input(model_uri, serving_payload))

# copied it from mlflow - artifacts - validate
# http://127.0.0.1:5000/#/experiments/0/runs/65928f0f02084877a3a8e0a304aaaae1