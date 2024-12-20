from fastapi import FastAPI

app=FastAPI()

def predict_salary(years):
    return 3 * years

@app.get("/predict/{years:float}")
async def abcd(years):
    return {"years":years,"predicted_salary":predict_salary(years)}

#to run
#uvicorn fast2:app --reload