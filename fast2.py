from fastapi import FastAPI
import pickle
f=open("mymodel1.pkl",'rb')
salarymodel = pickle.load(f)
f.close()
app=FastAPI()

def predict_salary(years):
    response = salarymodel.predict([[years]])
    return response[0]

@app.get("/predict/{years:float}")
async def abcd(years):
    return {"years":years,"predicted_salary":predict_salary(years)}

#to run
#uvicorn fast2:app --reload