import gradio as gr
import pickle

# Load the model
with open("mymodel1.pkl", 'rb') as f:
    salarymodel = pickle.load(f)

# Read the bulk experiences file
def read_bulk_experiences(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    return [float(line.strip()) for line in lines]

# Prediction function
def bulk_prediction():
    experiences = read_bulk_experiences("bulk_experiences.txt")
    predictions = [salarymodel.predict([[exp]])[0] for exp in experiences]
    return predictions

# Gradio interface function
def simple_interest_calculator(principal, years, interest_rate):
    return principal * years * interest_rate / 100

app = gr.Interface(fn=simple_interest_calculator, inputs=["number", "number", "number"], outputs=["number"])
app.launch(share=True)

# Optionally, create another Gradio interface for bulk prediction
bulk_app = gr.Interface(fn=bulk_prediction, inputs=[], outputs=["json"])
bulk_app.launch(share=True)
