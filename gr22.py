import gradio as gr
import pickle
f=open("mymodel1.pkl",'rb')
salarymodel = pickle.load(f)
f.close()

f2=open("bulk_experiences.txt",'rb')

def bulk_prediction(items):
    item = item[0]
    salarymodel.predict([[item]])
def simmplet_interest_calculator(principal, years, interest_rate):
    return principal*years*interest_rate/100
app=gr.Interface(fn=simmplet_interest_calculator,inputs=["number", "number", "number"],outputs=["number"])
app.launch(share=True)