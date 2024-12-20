from fastapi import FastAPI

app=FastAPI()

@app.get("/")
async def abcd():
    return {"message":"Hellow how are you?"}

#to run
#pip install fastapi uvicorn
#uvicorn fast1:app